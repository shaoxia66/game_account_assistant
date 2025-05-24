




from fastmcp import Client
import asyncio
import json
async def main():
    # Connect via stdio to a local script
    # async with Client("my_server.py") as client:
    #     tools = await client.list_tools()
    #     print(f"Available tools: {tools}")
    #     result = await client.call_tool("add", {"a": 5, "b": 3})
    #     print(f"Result: {result.text}")
    # {key: List[Literal["段位】黑铁","段位】青铜","段位】白银","段位】黄金","段位】铂金","段位】钻石","段位】超凡","段位】神话"]] = Field(..., description="搜索的关键字 例如 段位】黄金")
    # minPrice: str = Field(description="搜索的最低价格",default="")
    # maxPrice: str = Field(description="搜索的最高价格",default="")
    # minSection1: str = Field(description="搜索的最低等级",default="")
    # maxSection1: str = Field(description="搜索的最高等级",default="")}
    # Connect via SSE
    async with Client("http://localhost:9998/mcp") as client:
        # ... use the client
        # result =  await client.list_tools()
        # print(f"Available tools: {result}")
        py= {
            "p": {
            "keywords": ["段位】黄金"],   # 必填
            "minPrice": "100",   # 可选（默认空字符串）
            "maxPrice": "500",   # 可选
        }
}
        
        print(await client.call_tool("search", py))

asyncio.run(main())