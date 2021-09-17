# -*- coding:utf-8 -*-
"""
# 日期: 2021/09/12 13:10
# 作者：1stPeak
# 版本：V1.0
# 用途：测试没有设置安全标志的Cookie
"""
import argparse
from urllib import request
from http import cookiejar


parser = argparse.ArgumentParser()
parser.add_argument("-u" , "--url" , help = "请输入url,例如：https://www.example.com")
parser.add_argument("-f" , "--file" , help = "请在urls.txt中添加需要扫描的目标域名")
args = parser.parse_args()


if __name__ == '__main__':
    print("********安全标志Cookie验证脚本V1.0********[Author:1stPeak]")
    if args.url:
        headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        cookie = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        try:
            response = opener.open(args.url)
            response.encoding = "utf-8"
            reqcookie2 = ""
            for item in cookie:
                reqcookie1 = ('%s' % item.name + item.value)
                reqcookie2 += reqcookie1
            if "Secure" in reqcookie2:
                print("[+]" + args.url + "已设置安全标志的Cookie")
                with open('vulnerable_urls.txt', 'a') as f:
                    f.write(args.url + '\n')
            else:
                print("[+]" + args.url + "：未设置安全标志的Cookie")
                with open('security_urls.txt', 'a') as f:
                    f.write(args.url + '\n')
        except:
            print("[+]" + args.url + "无法访问")

    if args.file:
        fopen = open("urls.txt", 'r')
        lines = fopen.readlines()
        for args.url in lines:
            args.url = args.url.strip()
            headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
            cookie = cookiejar.CookieJar()
            handler = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(handler)
            try:
                response = opener.open(args.url)
                response.encoding = "utf-8"
                reqcookie2 = ""
                for item in cookie:
                    reqcookie1 = ('%s' % item.name + item.value)
                    reqcookie2 += reqcookie1
                if "secure" in reqcookie2:
                    print("[+]" + args.url + "已设置安全标志的Cookie")
                    with open('vulnerable_urls.txt', 'a') as f:
                        f.write(args.url + '\n')
                else:
                    print("[+]" + args.url + "：未设置安全标志的Cookie")
                    with open('security_urls.txt', 'a') as f:
                        f.write(args.url + '\n')
            except:
                print("[+]" + args.url + "无法访问")