from pydantic import BaseModel, Field
from typing import List,Literal
#价 格
# maxPrice
# minPrice
# 等级
# maxSection1
# minSection1
class GoodsModel(BaseModel):
    keywords: List[Literal["段位】黑铁","段位】青铜","段位】白银","段位】黄金","段位】铂金","段位】钻石","段位】超凡","段位】神话"]] = Field(..., description="搜索的关键字 例如 段位】黄金 只能选择一个")
    minPrice: str = Field(description="搜索的最低价格",default="")
    maxPrice: str = Field(description="搜索的最高价格",default="")
    minSection1: str = Field(description="搜索的最低等级",default="")
    maxSection1: str = Field(description="搜索的最高等级",default="")
# class Crad_model(BaseModel):
#     url: int = Field(...,description="显示图片的url")
#     price: float = Field(...,description="价格")
#     data: List[DailyModel] = Field(description="返回的数据",default=[])
