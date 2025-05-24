from dotenv import load_dotenv
load_dotenv()
from deal_mcp.models import GoodsModel
from fastmcp import FastMCP
import os
from spider.pzds.get_data import Pzds_spider
from spider.database.Cmongo import DBOperation

mcp = FastMCP("account assistant")

db_pzds = DBOperation("pzds")
db_px  = DBOperation("px")
# 1. 获取所有的交易记录  231为 无畏契约 
pzds_spider= Pzds_spider(db_pzds,231)

@mcp.tool()
async def search(p:GoodsModel) -> dict:
    
    '''
    搜索正在出售的账号
    :param p:搜索的参数

    :return:搜索到的json字符串
    '''

    info=await pzds_spider.get_search(p.model_dump())
    return info


@mcp.tool()
async def deal_record(p:GoodsModel) -> str:
    """
    搜索交易完成的账号
    """
    pass
    print(p)
    return "dsfdsf"

@mcp.prompt()
async def tt() -> str:

    return "dsfdsf"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=9998, path="/mcp")
