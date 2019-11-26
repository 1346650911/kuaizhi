import json
import datetime
import time

import requests

url = "http://ef.zhiweidata.com/index/indexUp.do"

headers = {
    'Host': "ef.zhiweidata.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
    'Accept': "application/json, text/plain, */*",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Accept-Encoding': "gzip, deflate",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Referer': "http://ef.zhiweidata.com/",
    'Cookie': "td_cookie=18446744073022057754; gr_user_id=32ea27ac-365a-4072-92e4-ccabd8405fbd; "
              "grwng_uid=267dcfdb-4b93-4801-953d-1af6ec22fd49; eventsMuseum=A3A28B5756E1FE4526EA73883AE0872A; "
              "UM_distinctid=16ea52e84173cd-02d841af19f17e-4c302a7b-1fa400-16ea52e8418299; "
              "CNZZDATA1276835865=1992413645-1574725304-null%7C1574741637; "
              "Hm_lvt_2ed01d2d0278f62aa71273d3e3eb52b4=1574729320; "
              "Hm_lpvt_2ed01d2d0278f62aa71273d3e3eb52b4=1574746169; "
              "9fe943ff4326aa51_gr_session_id_c79df93e-f969-401b-bae6-cc888424f22e=true; "
              "9fe943ff4326aa51_gr_session_id=c79df93e-f969-401b-bae6-cc888424f22e",
    'Cache-Control': "max-age=0",
    'Postman-Token': "3f140bf2-42da-4734-9fab-2bdfdaa8865e,6e105042-78d0-427e-ae85-a2241d314e3a",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
results = []
texts = response.json()
textss = texts['data']['rankHour'][-1]['info']


def timechange(time_sj):  # 传入参数
    data_sj = time.localtime(time_sj / 1000)
    time_str = time.strftime("%m-%d %H:%M", data_sj)  # 时间戳转换正常时间
    return time_str


def get_results():
    for info in textss:
        if info['name'] == '其他':
            break
        # print(local+' '+info['name'])
        local = timechange(info['startTime'])
        result = '[ 热度：' + str(int(info['hE'])) + ']   ' + info['name']
        results.append(result)
    return results
