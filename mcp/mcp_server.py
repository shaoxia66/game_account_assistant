from dotenv import load_dotenv
load_dotenv()
from models import DailyModel
from fastmcp import FastMCP
import os

mcp = FastMCP("account assistant")


@mcp.tool()
async def search(p:DailyModel) -> str:
    '''
    :param p:搜索的参数
    :type p: DailyModel
    :return:json字符串
    '''
    print(p)
    return "dsfdsf"


@mcp.tool()
async def deal_record(p:DailyModel) -> str:
    """

    """
    pass
    return "dsfdsf"



if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=9998, path="/mcp")
