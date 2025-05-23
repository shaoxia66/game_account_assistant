from pydantic import BaseModel, Field,model_validator
from typing import Optional, List
class DailyModel(BaseModel):
    
    game_id: int= Field(..., description="Game ID")
    price: float = Field(..., description="Price")
    good_no:str = Field(..., description="商品编号")
    game_name: str = Field(..., description="Game name")
    good_title: str = Field(..., description="商品标题")
    goods_type: str = Field(..., description="商品类型")
    server_name: str = Field(..., description="服务器名字")
    goods_img: List[str] = Field( description="图片地址列表",default=[])
    other: dict = Field(description="Other data",default={})
    good_create_time: str = Field(..., description="OnStandTime")
    deal_time: str = Field(..., description="Deal time")
    update_time: str = Field(..., description="Update time")
    merchant_mark: Optional[str] = Field(..., description="标记")
    count: int = Field(description="数量",default=1)
    unit_price: Optional[float] = Field(default=None, description="单价")
    @model_validator(mode='after')
    def set_defaults(self):
        if self.unit_price is None:
            object.__setattr__(self, "unit_price", self.price)
        return self