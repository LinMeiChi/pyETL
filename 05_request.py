#from  urllib import request
import  requests
from bs4 import BeautifulSoup

#少Header會出錯,故加上header(後面的網址類似瀏覽器的身分)
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

res = requests.get(url,headers=headers)

#print(res)      #2開頭代表訪視成功(,3開頭不一定,4一定失敗,5代表伺服器有問題例如200)
print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
print(soup)