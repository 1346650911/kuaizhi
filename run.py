from get_job import get_job
from push import handle_job


def run():
    print("推送开始")
    print("开始获取任务----------")
    job_list = get_job()
    print("任务获取结束----------")
    print("开始进行推送----------")
    handle_job(job_list)


if __name__ == '__main__':
    run()
