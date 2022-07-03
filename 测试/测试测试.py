import requests
import re

from urllib.request import urlopen

url = "https://tieba.baidu.com//p/7897236887?pn=1"  # 打开一个网址
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}
resp = requests.get(url, headers=header)  # 获取一个响应
obj_txt = re.compile(
    r'style="margin-right:3px">(?P<post_number_of_replies>.*?)</span>'
    r'class="d_post_content j_d_post_content " style="display:;">(?P<post_text>.*?)</div><br>',
    re.S)  # 正则匹配  # 正则匹配的内容返回
result_txt = obj_txt.finditer(resp.text)
for it in result_txt:
    print(it.group('post_number_of_replies'))
