# -*- coding:utf-8 -*-
print 'hell0'
import urllib2, urllib, cookielib
__author__ = 'pipiday'

class BaiduLogin:
    baidu_user = 'pipilamb@163.com'
    baidu_pwd = '4rf3ed2ws1qa'

    baidu_frontpage_url = 'http://www.baidu.com'
    baidu_login_url = 'https://passport.baidu.com/?login'

    baidu_LWP_cookie_file = "baidu3LWPcookie.txt"

    def __init__(self):
        print 'init BaiduLogin ... ...'

    def loginAndSaveCookieJar(self):
        #cookie jar
        #cj = cookielib.MozillaCookieJar("baidu3cookie.txt")
        cj = cookielib.LWPCookieJar(self.baidu_LWP_cookie_file)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

        params = urllib.urlencode(dict(username=self.baidu_user, password=self.baidu_pwd))
        print params
        aa = opener.open(self.baidu_login_url, params)
        for cookiess in cj:
            print cookiess

        cj.save(ignore_discard=True, ignore_expires=True)
        #if not 'k' in [cookie.name for cookie in cj]:
        #    raise ValueError, "Login failed"

        # try secured page
        resp = opener.open(self.baidu_frontpage_url)
        html = resp.read()
        if -1 == html.find(self.baidu_user):
            raise ValueError, 'Login Failed'
        else:
            print 'LOGIN SUCCESSFUL: '+ self.baidu_user

        #print html

        resp.close()




if __name__ == '__main__':
    bdLogin = BaiduLogin()
    bdLogin.loginAndSaveCookieJar()
