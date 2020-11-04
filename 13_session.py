import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url ='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'       #是否滿18歲頁面

ss = requests.session()

# Session1
#res = requests.get(url,headers=headers)
res = ss.get(url,headers=headers)            #目的在讓request在同一個session內
soup = BeautifulSoup(res.text,'html.parser')
button = soup.select('button[class="btn-big"]')[0]
print(button)
print(button['name'])               #取button(postdata)的key(name)
print(button['value'])              #取button(postdata)的value
print(ss.cookies)

hidden = soup.select('input')           #尋找hidden
print(hidden)

data = {}
data[button['name']] = button['value']
for k in hidden:                    #將值帶入
    data[k['name']] = k['value']
print(data)

# Session2
target_url = 'https://www.ptt.cc/ask/over18'
#res_target = requests.post(target_url,data=data,headers=headers)
res_target = ss.post(target_url,data=data,headers=headers)      #目的在讓request在同一個session內

# Session3
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
#final_res = requests.get(final_url,headers=headers)
final_res = ss.get(final_url,headers=headers)           #目的在讓request在同一個session內
print(final_res.text)

print(ss.cookies)           #可看到cookie內的東西
