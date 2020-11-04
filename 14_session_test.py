import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'http://e5918cb4.ngrok.io/practice/9'

ss = requests.session()         #設session訪問才夠快

res = ss.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
key = soup.select('input')[1]['name']
value = soup.select('input')[1]['value']
print(key,value)

data = {key:value,'pwd':'name123'}
res = ss.post(url,data=data,headers=headers)
print(res.text)