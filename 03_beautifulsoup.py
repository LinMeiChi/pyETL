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
#print(soup)

#定位有兩種方式
#第一種:findAll寫法
#logo = soup.findAll('a',{'id' : 'logo'}) #第一個參數是標籤(a),第二個參數是以字典的方式帶入屬性。回傳的東西會是一個List
#logo = soup.findAll('a',id='logo')

#第二種:select寫法(結果和findAll一樣)
#logo = soup.select('a[id="logo"]')         #標籤[完整屬性]
logo = soup.select('a#logo')

print(logo)
print(logo[0])
print(logo[0].text)  #取標籤以外的東西(內容)
print('https://www.ptt.cc/bbs/' + logo[0]['href']) #取href的字串(網址)= 屬性值
