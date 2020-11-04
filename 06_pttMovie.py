import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'        #要爬蟲的網址

res =requests.get(url,headers=headers)      #requests = html字串

soup = BeautifulSoup(res.text,'html.parser')

title_list = soup.select('div.title')
#print(title_list)

#用迴圈取出所有物件
for title_soup in title_list:
    #print(title_soup)

    title = title_soup.select('a')[0].text  #以a標籤進行定位,在取第0個的標題
    print(title)

# 連網址一起取出
    title_url = 'https://www.ptt.cc' +title_soup.select('a')[0]['href']
    print(title_url)