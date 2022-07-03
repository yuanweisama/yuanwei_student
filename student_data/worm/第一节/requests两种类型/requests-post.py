import requests

url = 'http://www.alang.run:8080/house/enter'

dat = {

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
}
resp = requests.post(url=url, data=dat, headers=headers)

print(resp.text)
