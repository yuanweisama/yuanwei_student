from urllib.request import urlopen

url = "http://www.baidu.com"  # 打开一个网址
resp = urlopen(url)  # 获取一个响应
with open("baidu.html", "w", encoding='utf-8') as f:
    f.write(resp.read().decode())
print('ok')  # 从响应中读取内容
