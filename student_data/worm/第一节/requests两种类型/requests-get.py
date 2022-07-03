import requests

url = 'https://movie.douban.com/j/chart/top_list'

parm = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
}  # 浏览器信息
resp = requests.get(url=url, params=parm, headers=headers)
with open('../top-movie.txt', 'a+', encoding='utf-8') as top:
    top.write(str(resp.json()))  # 写入文件
    top.close()
print(resp.json())
resp.close()  # 关闭resp
