__author__ = 'jinfeng'

from jenkinsapi.jenkins import Jenkins
import time

job_name = 'first_blood'

def get_last_build(jen):
    my_job = jen.get_job(job_name)
    job_detail = my_job.get_last_build()
    print job_detail
    print job_detail.get_status()

def build_job(jen):
    my_job = jen.get_job(job_name)
    jen.build_job(job_name)
    time.sleep(5)
    print my_job.get_last_build()

def jenkins_test():
    url = 'http://192.168.146.65:8080'
    jen = Jenkins(url, 'admin', 'admin')
    get_last_build(jen)
    build_job(jen)

if __name__ == '__main__':
    jenkins_test()


