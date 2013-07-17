
from fabric import tasks
from fabric.api import env, run
from fabric.context_managers import settings

env.hosts = ['qa26.server.163.org']
env.port = 1046
env.user = 'jinfeng' 
env.key_filename = ['E:/jinfeng/key/jinfeng']
env.password = 'jin169'           


def show_config():
    print env.hosts
    print env.user
    
def task_exec():
    with settings(host_string = env.hosts[0]):
        out = run('pwd', quiet = True)
        print out
        out = run('sudo -iu qatest pwd', quiet = True)
        print out
    
if __name__ == '__main__':
    #show_config()
    task_exec()
