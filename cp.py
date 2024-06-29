from mitmproxy import ctx
import json

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://tattoo186225345941:Qwerty7788421@cluster0.cf73hmy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['test']


def request(flow):
    # 记录请求信息
    # ctx.log.info(f"Request: {flow.request.method} {flow.request.url}")
    pass

def response(flow):
    # 需要匹配的目标 URL
    target_url = "https://apapia.manmanbuy.com/weixin/i.ashx"

    # 如果请求的 URL 匹配目标 URL，则记录响应信息
    if flow.request.url.startswith(target_url):
        # ctx.log.info(f"Response: {flow.response.status_code} {
        #             flow.request.url}")
        str_info = flow.response.text
        # print("str_info: ", str_info)
        j_s = json.loads(str_info)
        # print("j_s: ", j_s)
        print(j_s['data']['session_3rd'])
        if json.loads(str_info)['data']['session_3rd']:
            print("j_s['data']['session_3rd']: ", j_s['data']['session_3rd'])
            data = {
                'session_3rd': j_s['data']['session_3rd'],
                'status': 'canbeused',
                'count': 50,
                'lasttime': 0
            }
            db['session_3rd'].insert_one(data)
            print("success")
