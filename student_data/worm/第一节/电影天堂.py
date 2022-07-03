import requests
import re

movies_magnet = []
domain = 'http://dytt89.com/'
resp = requests.get(domain)
resp.encoding = 'gb2312'  # 指定字符集
# print(resp.text)

# 拿到ul里面的li
re_movies = re.compile(r'2022必看热片.*?<ul>(?P<movie_name>.*?)</ul>', re.S)
movie_magnet = re.compile(r"<a href='(?P<magnet>.*?)' title", re.S)
movie_name = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                        r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result_movies = re_movies.finditer(resp.text)
for it in result_movies:
    movies = it.group('movie_name')

    # 提取子页面链接
    result_movie_magnet = movie_magnet.finditer(movies)
    for itt in result_movie_magnet:
        # 拼接子页面内容：域名+子页面地址
        url = domain + itt.group('magnet').strip("/")  # strip去掉前面的/
        movies_magnet.append(url)
        continue
# 提取子页面内容
for magnet in movies_magnet:
    resp_magnet = requests.get(magnet)
    resp_magnet.encoding = 'gb2312'
    result_name = movie_name.search(resp_magnet.text)
    print(result_name.group('movie'))
    print(result_name.group('download'))
    # break  # 测试

# print(movies_magnet)
