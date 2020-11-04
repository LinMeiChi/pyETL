from  urllib import request
from bs4 import BeautifulSoup

#少Header會出錯,故加上header(後面的網址類似瀏覽器的身分)
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

#進行reques時,一同將header代入
req =request.Request(url=url,headers=headers)
res = request.urlopen(req)

#print(res.read().decode('utf-8'))


soup =BeautifulSoup(res.read(),'html.parser')   #將html字串轉換成html BeautifulSoup的型別

#print(soup.select('a'))
title = soup.select('div.title')        #定位div class="title"(即要取得結果的上一層標籤)
print(title[0])
print('------------------------------')
print(title[0].select('a'))
print(title[0].select('a')[0])
print(title[0].select('a')[0].text)

print('https://www.ptt.cc/' + title[0].select('a')[0]['href'])