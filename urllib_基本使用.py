#使用urllib获取seclimax首页源码
import urllib.request

#(1)定义一个url
#url = 'https://20.climaxfun.pw/forum.php'
url = 'https://20.climaxfun.pw/'
#url = 'http://www.baidu.com'
#url = 'http://www.sina.com.cn'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

#(2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#(3)获取响应中的页面源码
#read返回是二进制数据
#二进制-->字符串 解码 decode()
content = response.read().decode('utf-8')

#(4)打印内容
print(content)