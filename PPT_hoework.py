import requests
from bs4 import BeautifulSoup
import  os
import re

if not os.path.exists('pttmovie'):  #如果沒有資料夾,就自己創一個
    os.mkdir('pttmovie')        #創一個資料夾存文章內容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'        #要爬蟲的網址
ss = requests.session()
ss.cookies['over18'] = '1'

for i in range(0,2):
    res =ss.get(url,headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')

    title_list = soup.select('div.title')
    print(title_list)


    for title_soup in title_list:
        print(title_soup)
