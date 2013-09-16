__author__ = 'jinfeng'

import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def jenkins_test():
    url = 'http://192.168.146.65:8080'
    jen = Jenkins(url)

    job_list = jen.get_jobs_list()
    print job_list

    jobname = 'first_blood'
    myjob = jen.get_job(jobname)
    jen.build_job(myjob)

    build = myjob.get_last_build()
    print build




