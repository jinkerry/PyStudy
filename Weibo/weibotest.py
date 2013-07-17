import urllib2

__author__ = 'jinfeng'

import sys
from weibo import APIClient

app_key = '1081233493'
app_secret = '39ae50fa6a13270893fe26cfbcaeadd1'
callback_url = 'http://blog.163.com'


def auth():
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    url = client.get_authorize_url()
    print url

def send_microblog():
    f = open('code.txt', 'r')
    code = f.readline()
    print 'code: ' + code
    f.close()

    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in

    client.set_access_token(access_token, expires_in)

    print client.statuses.update.post(status=u'Hello Black QA')


if __name__ == "__main__":
    print 'begin'
    auth()
    raw_input('Click the URL, the press any key to continue...')
    send_microblog()
