# no-cookie-Secure
optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     请输入url,例如：https://www.example.com
  -f FILE, --file FILE  请在urls.txt中添加需要扫描的目标域名

存在漏洞的URL保存在vulnerable_urls.txt中
不存在漏洞的URL保存在security_urls.txt中

环境：python3.x
依赖库：argparse、urllib、http

Tips：该版本验证根据Response包中cookie值是否包含Secure字符串来判断
误报较高，仅供参考
