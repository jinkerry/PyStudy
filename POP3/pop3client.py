#coding: utf-8
__author__ = 'jinfeng'

import string
import poplib
import StringIO
import rfc822


servername = "pop3.126.com"
username = "jinkerry"
passwd = "password"


def receive_mail():
    pop = poplib.POP3(servername)
    pop.set_debuglevel(1)
    pop.user(username)
    pop.pass_(passwd)

    num, total_size = pop.stat()

    hdr, text, octet = pop.retr(num)

    #保存为eml格式的文件
    text = string.join(text, "\n")
    fh = open('f:/mail.eml', 'w')
    fh.write(text)
    fh.flush()
    fh.close()

    #mail headers
    file = StringIO.StringIO(text)
    message = rfc822.Message(file)
    for k, v in message.items():
        print k, "=", v

    print message.fp.read()


if __name__ == '__main__':
    receive_mail()