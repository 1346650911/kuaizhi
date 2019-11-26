import requests

from config import get_job_url

job_id_list = []


def is_new_job(job_id):
    if job_id in job_id_list:
        return False
    else:
        return True


def update_job():
    job_id_list.clear()
    has_new_job = True
    while has_new_job:
        job_results = requests.get(get_job_url).json()
        errno = job_results['errno']
        errmsg = job_results['errmsg']
        if errno == 0:
            job_id = job_results['job']['job_id']
            has_new_job = is_new_job(job_id)
            if has_new_job:
                job_id_list.append(job_id)
            else:
                has_new_job = False


def get_job():
    update_job()
    return job_id_list
