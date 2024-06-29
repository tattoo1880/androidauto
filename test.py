import requests
import json
from selenium import webdriver
import time
headers = {
    'Host': 'app.dewu.com',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-platform': '"macOS"',
    'traceparent': '00-f5943bf0667b8aba9942425106093a7a-ab37ac5bfd1052b5-01',
    'sec-ch-ua-mobile': '?0',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk5NzU3MDAsInVzZXJJZCI6MTU5MDk4MDA1LCJ1c2VyTmFtZSI6IiIsInYiOjE3MTkwNDAyNTMzMzAsInR5cGUiOjAsInJvbGUiOiJib21fbWVyY2hhbnQifQ.l27mq14mjScE9Nc0_kVv_rRhiHkfXB_Qh9hZO5jJWv4',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-xdw-video-flag': 'true',
    'appVersion': '4.69.0',
    'Accept': '*/*',
    'Origin': 'https://gravity.dewu.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://gravity.dewu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = {
    'keyword': '田少tt',
    'sign': 'd93ff45ad04e0b78d4ab290795a96286',
}

response = requests.get('https://app.dewu.com/sns-bom/v1/common/platform/merchant/user-search', params=params, headers=headers)


print("response: ", response.text)
obj = json.loads(response.text)
if obj.get("data"):
    print("data: ", obj.get("data"))
    userid = obj.get("data").get("list")[0].get("userId")
    if userid:
        print("userid: ", userid)
        # 打开网页
        driver = webdriver.Chrome()
        driver.get(f'https://gravity.dewu.com/talent?userId={userid}')
        time.sleep(1000000)
