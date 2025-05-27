from dotenv import load_dotenv
load_dotenv()
import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,SystemMessage,ToolMessage
import re
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langfuse.callback import CallbackHandler
from langchain_core.output_parsers import PydanticOutputParser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from deal_mcp.models import Assess_lv


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，生产环境建议改为具体域名如 ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)
client = MultiServerMCPClient(
        {
            "goods_info": {
                "url": "http://localhost:9998/mcp",
                "transport": "streamable_http",
            }
        }
    )




chat=ChatOpenAI(
    model=os.getenv("NIM_MODEL"),
    temperature=0.6,
    api_key=os.getenv("NIM_KEY"),
    base_url=os.getenv("NIM_HOST"),
)


@app.get("/assess")
async def assess(metadata: str):
    handler = CallbackHandler(
    session_id="test",
    tags=["assess"]
    )
    output_parser = PydanticOutputParser(pydantic_object=Assess_lv)
    format_instructions = output_parser.get_format_instructions()
    system_message = f"你是一个账号购买的评估大师。你会根据账号价格和其他信息，给出账号的评估结果是否值得购买。输出的结构为 {format_instructions}"
    user_message = metadata

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message),
        ]
    chain = chat | output_parser
    print(chain)
    try:
        return await chain.ainvoke(messages,config={"callbacks":[handler]})

    except Exception as e:
        return await chain.ainvoke(messages,config={"callbacks":[handler]})
    

@app.get("/chat")
async def goods_info(query: str):
    tools = await client.get_tools()
    llm_with_tools=chat.bind_tools(tools)
    handler = CallbackHandler(
        session_id="test",
        user_id="s"
    )

    system_message = "你是账号搜索助手，可以搜索网站售卖的账号和交易完成的账号。你可以使用search或deal_record工具来获取账号信息。一次只能使用一个工具。用function-call来调用工具。"
    user_message = query

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message),
        ]
    

    response=await llm_with_tools.ainvoke(messages,config={"callbacks":[handler]})
    # 容易出现这种工具调用的范式 末尾少一个}
    #<TOOLCALL>[{"name": "deal_record", "arguments": {"p": {"keywords": ["段位】铂金"], "maxPrice": "100"}}]</TOOLCALL>
    pattern = r'<TOOLCALL>(.*?)</TOOLCALL>'
    match = re.search(pattern, str(response.content), re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            json_obj = json.loads(json_str)
        except json.JSONDecodeError as e:
            json_obj = json.loads(json_str[:-1]+"}]")
        tool_call = json_obj
        tool_name=tool_call[0]["name"]
        tool_args=tool_call[0]["arguments"]
        selected_tool = {t.name.lower(): t for t in tools}[tool_name]
        tool_result = await selected_tool.ainvoke(tool_args)
        print("TOOLCALL:", tool_result)
        return tool_result
    elif (hasattr(response, "tool_calls") and response.tool_calls):
    # 7. 执行所有工具调用，生成对应的 ToolMessage
        for tool_call in response.tool_calls:
             tool_name = tool_call["name"].lower()
             tool_args = tool_call["args"]
             selected_tool = {t.name.lower(): t for t in tools}[tool_name]
             tool_result =await selected_tool.ainvoke(tool_args)
             print("response type:", type(response))
             print("tool_calls:", tool_result)
             return tool_result
            #  client.
            # # 根据工具名找到对应工具
            # tool_name = tool_call["name"].lower()
            # tool_args = tool_call["args"]
            # selected_tool = {t.name.lower(): t for t in tools}[tool_name]
            # tool_result =await selected_tool.ainvoke(tool_args)
            # # 生成 ToolMessage，传回模型
            # tool_msg = ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
            # messages.append(tool_msg)
        # 8. 把工具调用结果传回模型，生成最终回答
        # final_response = llm_with_tools.invoke(messages,config={"callbacks":[handler]})
        # print("Final answer:", final_response.content)
    else:
        print("Answer:", response.content)
        return ""
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
