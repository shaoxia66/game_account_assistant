import requests
import json
from urllib.parse import quote
import  time
def post_phone_check(mobile):
    url = 'http://apis.apikonghao.com/Api/PhoneCheck'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        'mobile': mobile,
        'code': ''
    }

    try:
        # 发送 POST 请求并设置超时时间为 15 秒
        response = requests.post(url, json=data, headers=headers, timeout=15)
        response.raise_for_status()  # 自动处理 HTTP 错误状态码
        print(response.text)

        # 解析 JSON 响应
        result = response.json()
        if result.get('Tag') == 1:
            check_id = result.get('Data', {}).get('CheckId')
            if check_id:
                # 对参数进行 URL 编码
                encoded_mobile = quote(mobile)
                encoded_check_id = quote(check_id)
                target_url = 'http://120.27.122.177:8080'+f"/search.html?mobile={encoded_mobile}&checkId={encoded_check_id}"
                print(target_url)
                response = requests.post(url, json=data, headers=headers, timeout=15)
                headers = {
                    "Accept": "*/*",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Content-Type": "application/json",
                    "Origin": "http://120.27.122.177:8080",
                    "Pragma": "no-cache",
                    "Proxy-Connection": "keep-alive",
                    "Referer": "http://120.27.122.177:8080/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
                }
                url = "http://apis.apikonghao.com/Api/MarkCheckResult"
                data = {
                    "checkId": encoded_check_id
                }
                data = json.dumps(data, separators=(',', ':'))
                response = requests.post(url, headers=headers, data=data, verify=False)
                jsons=response.json()
                while jsons["Data"]["State"]!=2:
                    time.sleep(1)
                    response = requests.post(url, headers=headers, data=data, verify=False)
                    jsons=response.json()
                    print(jsons)

            else:
                print("查询失败：响应中缺少 CheckId")
        else:
            error_msg = result.get('Message', '未知错误')
            print(f"查询失败：{error_msg}")

    except requests.exceptions.Timeout:
        print("请求超时，请检查网络或稍后重试")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误 ({e.response.status_code})：{e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"网络连接失败：{str(e)}")
    except json.JSONDecodeError:
        print("错误：服务器返回了非 JSON 格式的响应")

    return None

# 使用示例
if __name__ == "__main__":
    phone_number = "17002866146"  # 替换为要查询的手机号
    result_url = post_phone_check(phone_number)
    if result_url:
        # 如果需要自动打开浏览器，可以取消以下注释（需安装 webbrowser 库）
        # import webbrowser
        # webbrowser.open(result_url)
        pass