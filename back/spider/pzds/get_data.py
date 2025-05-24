
import json
import execjs
import aiohttp
import asyncio
import os
from spider.core.base import Spider_base
from spider.models.daily import DailyModel

class Pzds_spider(Spider_base):
    def __init__(self, db,game_id:int):
        self._game_id = game_id
        super().__init__(db)
        try:
            with open(os.path.join("back","spider","pzds","tt.js"), "r", encoding="utf-8") as f:
                js_code = f.read()
                self._ctx_sign = execjs.compile(js_code)

            with open(os.path.join("back","spider","pzds","decode_1174.js"), "r", encoding="utf-8") as f:
                js_code = f.read()
                self._ctx_decode_1174= execjs.compile(js_code)
        except Exception as e:
            self._logger.error(f"读取JS文件失败: {e}")
            raise e


    async def get_search(self,dic:dict) -> dict:
        cookies = {
        "_c_WBKFRo": "X4MRamkS7Oscjhm7HnkWZJhmAFEizHn5gs51zXON",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219651d021d210a-01f52f2060a410a-26011c51-1638720-19651d021d31af7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NTFkMDIxZDIxMGEtMDFmNTJmMjA2MGE0MTBhLTI2MDExYzUxLTE2Mzg3MjAtMTk2NTFkMDIxZDMxYWY3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
        "Hm_lvt_8e2c03f98f8af83cf09317d232baf903": "1745163964,1745200328,1745282157,1745499313",
        "HMACCOUNT": "F68CCF36A3EBADF0",
        "acw_tc": "ac11000117455018065397813e00c3b991c8ae53cd7504a642a25e557e02f9",
        "Hm_lpvt_8e2c03f98f8af83cf09317d232baf903": "1745502632",
        "ssxmod_itna": "YqfxBQit0=LOG7DzxUqWKiQ0CDRDL=DB4WYG=CbidDniiDDuio0QipLpbPXEDlxri4DZDGKGFDQeDvm7Cpxzq+xuaN7ub6Bc+zo3ZSvFUdbDE5BAbDCPGnDB9jxSBxYYpDt4DTD34DYDiroDj4GmDGY4EqDFSk0qTjXMjDDwDB=DmqG2jANDm4DfDDL/IgpXSdND4qDBDGU3H=bDG4GfDlPD0Mp1vb3DbENqOMbdRjcOQe4YSqDMnDGXYBgHSkaAp/PK=eOpZ6vMfjbDtqD9BmiyRQeD1erSlavaSOGamY3qmGGsf2GeFgpOCqoj+xeh4tqqem4CD4W4YnXCQxzYrOxhHQxl=qxD",
        "ssxmod_itna2": "YqfxBQit0=LOG7DzxUqWKiQ0CDRDL=DB4WYG=CbidDniiDDuio0QipLpbPXD62NV3xD/I67KGa8ZS72biQYeidYw8GgDhdwbB89wTMf1PuO45lpMjhitR/2du5HU8B4gQh7/lRO7ojXdYIEmMSTf4YQ3YYG6azr6btlj60T3k/4oqwRUAturdXwGYEjuUY==j36Wqc3ulF8UeFMAuIOIaeSoIBqL8t+2UK7Qc4CoYB=yX7kDqOqj8+dF+UkPADn02fcXwYniUGG=AoeCRe+dM0I9mG4oNhqZR6+XlKqgor=gAb0no648ag4xFi/CvifHGUHpIekj2iWaB0RO05b0HBb4CBT78wKueFQ9Sl+9l4b/mPkKTnB7/nbeodXBYsEdHESfFYdHEBR3KB5cnO77oG47ITivme5pu8Wir8QV+rxp+74Wnb83wF8WzG3Wh2Tq5Bl+FoiRK8nS4bi9xdERS4HGfhbWHvKWHrzDnvKwFwmOdL8LoGePO=W1h4k7OQl4q=QWH9DWxND07d7DKDH5M3ebvjoRTtHilRd0=rfRP2TPDNXiiCIortop/7qjRq0xn+DmCri7=dT9PDo44daFvHF7Cq46YcDvcw2Dd0q7DtPrgg8P4D=="
        }
        url = "https://api.pzds.com/api/web-client/v2/public/goodsPublic/page"

        data ={
        #从上架时间维度倒序，最后上架的在最前面
        "order": "DESC",
        "sort": "onStandTime",
        "page": 1,
        "pageSize": 21,#每页数量 第一页都一个一般是广告
        "action": {
            "gameId": self._game_id,
            "goodsCatalogueId": 6,
            "merchantMark": None, #商户标识，一般为商户名字
            "keywords": [], #d段位会出现在这里
            "searchWords": [],
            "searchPropertyIds": [],
            "unionGameIds": [],
            "goodsSearchActions": [],
            **dic
        }
    }
        data = json.dumps(data, separators=(',', ':'))
        decode_1174=self._ctx_decode_1174.call("decode_1174", data)
        signature = self._ctx_sign.call("get_signatrue", data)

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://www.pzds.com",
            "PZOs": "windows",
            "PZPlatform": "pc",
            "PZTimestamp": str(signature["Timestamp"]),
            "PZVersion": "1.0.0",
            "PZVersionCode": "1",
            "Pragma": "no-cache",
            "Random": str(signature["Random"]),
            "Referer": "https://www.pzds.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sign":  signature["strMd5"],
            "Skey": "CLIENT",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "channelInfo": "{\"channelCode\":null,\"tag\":null,\"channelType\":null,\"searchWord\":\"null\"}",
            "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "x-oss-forbid-overwrite": "true"
        }
        params = {
            "decode__1174": decode_1174
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, cookies=cookies,headers=headers, params=params,data=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result
                    # self._logger.info(f"爬取成功")
                else:
                    self._logger.error(f"爬取失败{response.status}",)
        return {}


    async def get_all_transaction_records(self,witer = False,sleep_time=1):
        '''
        获取昨天的交易记录
        :param witer: 是否写入数据库
        :param sleep_time: 每次请求的间隔时间
        '''
        data = {
        "action": {
            "gameId": self._game_id,
        },
        "page": 1,
        "pageSize": 10
        }
        
        cookies = {
        "_c_WBKFRo": "X4MRamkS7Oscjhm7HnkWZJhmAFEizHn5gs51zXON",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219651d021d210a-01f52f2060a410a-26011c51-1638720-19651d021d31af7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NTFkMDIxZDIxMGEtMDFmNTJmMjA2MGE0MTBhLTI2MDExYzUxLTE2Mzg3MjAtMTk2NTFkMDIxZDMxYWY3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
        "acw_tc": "ac11000117458539370361717e006ce793507bf8713e369eaf11318202062a",
        "Hm_lvt_8e2c03f98f8af83cf09317d232baf903": "1745760604,1745800175,1745811545,1745853959",
        "HMACCOUNT": "F68CCF36A3EBADF0",
        "Hm_lpvt_8e2c03f98f8af83cf09317d232baf903": "1745853992",
        "ssxmod_itna": "iqmx2D9Gi=DQn0Dl4C5AQG7GgDmxFwD0PwietoqGkKFD0Ox7KGCm=FK8ikhrxBuF4DZDGKGFDQeDvmWCiLCezB72+ztBEfrfzRinA5+WRSo9iXXgKYx0aDbqGk0YYofeDxpe0rD74irDDxDWb4DLDYoDYRiMDGpV3Q2PVdNdD0YDzqDgD7Qd/qDEDG3D0SN780LV9qG0DDtDAMRFveDADA3xkDDl8AHE+4GW/q29Rn+=sPKe=0GVD0t=DBLP+UhV8a8fk0reaIOGMoXdXeGuDG=N=l6=qriYantGEkGzGi4A8r+fQDKq8rKCDqeAI4n4qiG1l4SipHGDVcPWYhWe2KidqnGoGDWYD===",
        "ssxmod_itna2": "iqmx2D9Gi=DQn0Dl4C5AQG7GgDmxFwD0PwietoqGkKFD0Ox7KGCm=FK8ikhx8wH/xD/FYqxGaWpRAjW08ejhrD6iGGr7K4b1fjL0nU73jLen8AcWn7c4kjWqFkLpiyyrha/6aEwHd=lF=EcrbEFFbav=zx9W5gyzK7mGP39a5fAWt/ckD801griWW=DOuEesm+57FPoxdGii01a7Lhvr6mSDqPPCtIPx5hiHLhI8pr779lamXa8spIl159aApRHWqmSIeAmTFypxEIamEFIvKZOi0D7Csai8pfbwiNagx656OPaWMedSYxq1rfIEfTcvRjNmm6xOmBmpU1P7hGZiDcm+7a2Em48ZPh=pfAeNOq6iqPf=uYNqGPdEpFn6YEfyGK/0brPoIDPm7eCQvY1U7UDs8Q6m4nYdVm44ZulQGT=jleUN862mt36PgiTEpuI1GdKo/c+MOuBOd64hwCvpxwOKvwZN7DLA03YedpiLRm6EDuRB3Z4yK9+DkIx3UCRdOlPnmtbpUXzLvB7eAd5kDBBXZt5OQuc6mIbW9xQmB4eA3enfICdKQbeh9EzeMOpMftpmt+CdLiDB3wxTfH2bf0LhF=QTrmnGPee4cv2aCa=isKU6/bKpEsujBnGx0qDQFpuKRNHi5TeQ8B7rj+mBygOmmHgPEyOqAIlhjNhNtSb3KyvjbxiwLC+xYjfQRAVRAFDxlDQAxeD="
        }
        url = "https://api.pzds.com/api/web-client/v2/homepage/public/yesterday/deal/game/detail"
        data = json.dumps(data, separators=(',', ':'))
        signature =self._ctx_sign.call("get_signatrue", data)
        headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.pzds.com",
        "PZOs": "windows",
        "PZPlatform": "pc",
        "PZTimestamp": str(signature["Timestamp"]),
        "PZVersion": "1.0.0",
        "PZVersionCode": "1",
        "Pragma": "no-cache",
        "Random": str(signature["Random"]),
        "Referer": "https://www.pzds.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sign":  signature["strMd5"],
        "Skey": "CLIENT",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "channelInfo": "{\"channelCode\":null,\"tag\":null,\"channelType\":null,\"searchWord\":\"null\"}",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-oss-forbid-overwrite": "true"
        }
        decode_1174=self._ctx_decode_1174.call("decode_1174", data)
        params = {
            "decode__1174": decode_1174
        }
        async with aiohttp.ClientSession() as session:
            self._logger.info(f"请求数据: {data}")

            async with session.post(url, headers=headers, cookies=cookies, params=params, data=data) as response:
                if response.status == 200:
                    result = await response.json()
                    totalPages=result["data"]["totalPages"]
                    self._logger.info(f"爬取成功")
                    if witer:
                        #TODO: 写入数据库
                        docs = []
                        for item in result["data"]["records"]:
                            docs.append(DailyModel(game_id=self._game_id,
                                                    price=item.get("price", 0),
                                                    good_no=item.get("goodsNo", ""),
                                                    game_name=item.get("gameName", ""), 
                                                    good_title=item.get("title", ""),
                                                    goods_type=item.get("goodsCatalogueName", ""),
                                                    server_name=item.get("simpleMessage", ""), 
                                                    goods_img=[item.get("goodsImg", "")],
                                                    # other=item["other"], 
                                                    good_create_time=item.get("onStandTime",""),
                                                    deal_time=item.get("createTime", ""),
                                                    update_time=item.get("updateTime", ""),
                                                    merchant_mark=item.get("merchantMark", "")
                                                    ).model_dump())
                        # docs = [DailyModel(**item) for item in result]
                        await self._db.insert_multiple_records(docs)
                else:
                    self._logger.error(f"Error: {response.status}")
                    return None
        async with aiohttp.ClientSession() as session:
            for page in range(2, totalPages + 1):
                await asyncio.sleep(sleep_time)
                data = {
                "action": {
                    "gameId": self._game_id,
                },
                "page": page,
                "pageSize": 10
                }
                
                cookies = {
                "_c_WBKFRo": "X4MRamkS7Oscjhm7HnkWZJhmAFEizHn5gs51zXON",
                "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219651d021d210a-01f52f2060a410a-26011c51-1638720-19651d021d31af7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2NTFkMDIxZDIxMGEtMDFmNTJmMjA2MGE0MTBhLTI2MDExYzUxLTE2Mzg3MjAtMTk2NTFkMDIxZDMxYWY3In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
                "acw_tc": "ac11000117458539370361717e006ce793507bf8713e369eaf11318202062a",
                "Hm_lvt_8e2c03f98f8af83cf09317d232baf903": "1745760604,1745800175,1745811545,1745853959",
                "HMACCOUNT": "F68CCF36A3EBADF0",
                "Hm_lpvt_8e2c03f98f8af83cf09317d232baf903": "1745853992",
                "ssxmod_itna": "iqmx2D9Gi=DQn0Dl4C5AQG7GgDmxFwD0PwietoqGkKFD0Ox7KGCm=FK8ikhrxBuF4DZDGKGFDQeDvmWCiLCezB72+ztBEfrfzRinA5+WRSo9iXXgKYx0aDbqGk0YYofeDxpe0rD74irDDxDWb4DLDYoDYRiMDGpV3Q2PVdNdD0YDzqDgD7Qd/qDEDG3D0SN780LV9qG0DDtDAMRFveDADA3xkDDl8AHE+4GW/q29Rn+=sPKe=0GVD0t=DBLP+UhV8a8fk0reaIOGMoXdXeGuDG=N=l6=qriYantGEkGzGi4A8r+fQDKq8rKCDqeAI4n4qiG1l4SipHGDVcPWYhWe2KidqnGoGDWYD===",
                "ssxmod_itna2": "iqmx2D9Gi=DQn0Dl4C5AQG7GgDmxFwD0PwietoqGkKFD0Ox7KGCm=FK8ikhx8wH/xD/FYqxGaWpRAjW08ejhrD6iGGr7K4b1fjL0nU73jLen8AcWn7c4kjWqFkLpiyyrha/6aEwHd=lF=EcrbEFFbav=zx9W5gyzK7mGP39a5fAWt/ckD801griWW=DOuEesm+57FPoxdGii01a7Lhvr6mSDqPPCtIPx5hiHLhI8pr779lamXa8spIl159aApRHWqmSIeAmTFypxEIamEFIvKZOi0D7Csai8pfbwiNagx656OPaWMedSYxq1rfIEfTcvRjNmm6xOmBmpU1P7hGZiDcm+7a2Em48ZPh=pfAeNOq6iqPf=uYNqGPdEpFn6YEfyGK/0brPoIDPm7eCQvY1U7UDs8Q6m4nYdVm44ZulQGT=jleUN862mt36PgiTEpuI1GdKo/c+MOuBOd64hwCvpxwOKvwZN7DLA03YedpiLRm6EDuRB3Z4yK9+DkIx3UCRdOlPnmtbpUXzLvB7eAd5kDBBXZt5OQuc6mIbW9xQmB4eA3enfICdKQbeh9EzeMOpMftpmt+CdLiDB3wxTfH2bf0LhF=QTrmnGPee4cv2aCa=isKU6/bKpEsujBnGx0qDQFpuKRNHi5TeQ8B7rj+mBygOmmHgPEyOqAIlhjNhNtSb3KyvjbxiwLC+xYjfQRAVRAFDxlDQAxeD="
                }
                url = "https://api.pzds.com/api/web-client/v2/homepage/public/yesterday/deal/game/detail"
                data = json.dumps(data, separators=(',', ':'))
                signature =self._ctx_sign.call("get_signatrue", data)
                headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Origin": "https://www.pzds.com",
                "PZOs": "windows",
                "PZPlatform": "pc",
                "PZTimestamp": str(signature["Timestamp"]),
                "PZVersion": "1.0.0",
                "PZVersionCode": "1",
                "Pragma": "no-cache",
                "Random": str(signature["Random"]),
                "Referer": "https://www.pzds.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sign":  signature["strMd5"],
                "Skey": "CLIENT",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                "channelInfo": "{\"channelCode\":null,\"tag\":null,\"channelType\":null,\"searchWord\":\"null\"}",
                "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "x-oss-forbid-overwrite": "true"
                }
                decode_1174=self._ctx_decode_1174.call("decode_1174", data)
                params = {
                    "decode__1174": decode_1174
                }

                async with session.post(url, headers=headers, cookies=cookies, params=params, data=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        if witer:
                            docs = []
                            for item in result["data"]["records"]:
                                docs.append(DailyModel(game_id=self._game_id,
                                                        price=item.get("price", 0),
                                                        good_no=item.get("goodsNo", ""),
                                                        game_name=item.get("gameName", ""), 
                                                        good_title=item.get("title", ""),
                                                        goods_type=item.get("goodsCatalogueName", ""),
                                                        server_name=item.get("simpleMessage", ""), 
                                                        goods_img=[item.get("goodsImg", "")],
                                                        # other=item["other"], 
                                                        good_create_time=item.get("onStandTime",""),
                                                        deal_time=item.get("createTime", ""),
                                                        update_time=item.get("updateTime", ""),
                                                        merchant_mark=item.get("merchantMark", "")
                                                        ).model_dump())
                            # docs = [DailyModel(**item) for item in result]
                            await self._db.insert_multiple_records(docs)
                    else:
                        self._logger.error(f"Error: {response.status}")
                        return None
                