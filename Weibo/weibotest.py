__author__ = 'jinfeng'

import sys
import httplib
import urllib2
from weibo import APIClient

app_key = '1081233493'
app_secret = '39ae50fa6a13270893fe26cfbcaeadd1'
callback_url = 'https://github.com/jinkerry'


def auth():
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    url = client.get_authorize_url()
    print url

    resp = urllib2.urlopen(url)
    print resp

    # action = '/oauth2/authorize?redirect_uri=https;//github.com/jinkerry&response_type=code&client_id=1081233493'
    # conn = httplib.HTTPSConnection('api.weobo.com')
    # conn.request('post', action)
    # resp = conn.getresponse()

def fwb():
    code = 'eceb8e3ebc772f931f86ba1398c63de2'
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in

    client.set_access_token(access_token, expires_in)

    #print client.statuses.user_timeline.get()
    print client.statuses.update.post(status=u'Hello Black QA')


if __name__ == "__main__":
    print 'begin'
    auth()
    #fwb()