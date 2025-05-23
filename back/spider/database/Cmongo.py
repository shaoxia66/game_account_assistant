import json
import os
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import datetime
import logging

class DBOperation:
    def __init__(self,platform,url="192.168.1.6",port=27017):
        try:
            self.client = AsyncIOMotorClient(f"mongodb://mongo_wjw:w315316428@{url}:{port}/autoLive?authSource=admin")
            if self.client is None:
                logging.error("数据库连接失败")
                raise Exception("数据库连接失败")
            self.db = self.client['game_deal']
            self.deal_records = self.db['deal_records']
            self._platform = platform
        except Exception as e:
            logging.error(e)
    def close(self):
        self.client.close()
    async def insert_multiple_records(self, records):
        re_records = [{**record,"timestamp":datetime.datetime.now(),"platform":self._platform} for record in records]
        try:
            logging.info(f"插入数据: {len(re_records)}条")
            result = await self.deal_records.insert_many(re_records)
            return result.inserted_ids
        except Exception as e:
            logging.error(f"插入数据失败: {e}")
            return None



    


            





