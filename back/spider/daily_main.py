from database.Cmongo import DBOperation
from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
from pzds.get_data import Pzds_spider
import asyncio
import os

logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
    handlers=[
        logging.StreamHandler() , # 输出到控制台
        TimedRotatingFileHandler(os.path.join("logs","daily_main.log"), when='D', interval=10, backupCount=0, delay=False, utc=False,encoding="utf-8")
    ]
)


async def  main():
    try:
        logging.info("开始执行 每日采集任务")
        db_pzds = DBOperation("pzds")
        db_px  = DBOperation("px")
        # 1. 获取所有的交易记录  231为 无畏契约 
        pzds_spider= Pzds_spider(db_pzds,231)
        await pzds_spider.get_all_transaction_records(True,sleep_time=0) 
    finally:
        db_pzds.close()
        db_px.close()

if  __name__ == "__main__":
    asyncio.run(main())

