from pydantic import BaseModel, Field
from typing import List

class DailyModel(BaseModel):
    key: List[str] = Field(..., description="搜索的关键字")
    min_price: str = Field(description="搜索的最低价格",default="")
    max_price: str = Field(description="搜索的最高价格",default="")



# class Crad_model(BaseModel):
#     url: int = Field(...,description="显示图片的url")
#     price: float = Field(...,description="价格")
#     data: List[DailyModel] = Field(description="返回的数据",default=[])