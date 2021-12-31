import urllib.request

#将API调用并存储响应
url="https://www.douban.com/"
data=urllib.request.urlopen(url).read()
data=data.decode('UTF-8')
print(data)