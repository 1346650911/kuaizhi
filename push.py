import json
import requests

from config import get_job_url, push_msg_url
from get_result import get_results

header = {
    "Content-Type": 'application/json'
}



def get_result():
    results = get_results()
    outputs = ''
    i = 1
    for result in results:
        result = str(i) + '、  ' + result + '\n'
        outputs = outputs + result
        i = i + 1
    return outputs


def _msg(job_id):
    text = get_result()

    msg = {
        "job_id": job_id,
        "cards": [
            {

                "title": "今日事件",
                "text": text,
                "url": "http://ef.zhiweidata.com/#!/index"
            },

        ]

    }
    return msg


def push_to_job(job):
    print("获取请求头----")
    msg = _msg(job)
    print("当前请求头是"+str(msg))
    data = json.dumps(msg)
    response = requests.post(push_msg_url, data=data, headers=header)


def handle_job(job_id_list):
    for job in job_id_list:
        push_to_job(job)
