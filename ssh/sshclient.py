'''
Created on 2013-4-23

@author: Administrator
'''

import paramiko

def dssconnect():
    #paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    host = 'qa26.server.163.org'
    port = 1046
    username = 'jinfeng'
    
    ssh_client = paramiko.SSHClient()
    mykey = paramiko.DSSKey.from_private_key_file('e:/jinfeng/key/jinfeng',password='xxxxxx')
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, pkey=mykey)
    stdin, stdout, stderr = ssh_client.exec_command('pwd')
    for x in stdout.readlines():
        print x,  
    
    stdin, stdout, stderr = ssh_client.exec_command('sudo -iu qatest pwd')
    for x in stdout.readlines():
        print x,
        
    ssh_client.close()


if __name__ == '__main__':
    dssconnect()