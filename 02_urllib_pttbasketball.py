from  urllib import request


#少Header會出錯,故加上header(後面的網址類似瀏覽器的身分)
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

#進行reques時,一同將header代入
req =request.Request(url=url,headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))