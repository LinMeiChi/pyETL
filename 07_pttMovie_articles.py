# P.40 將其他頁的標題也爬下來
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'        #要爬蟲的網址

page = 8974 #建立起始值(ptt上一頁的起始是由8974開始)

#只有有規律的網址才能包在一起(08為無規律的寫法)
for i in range(0,5):
    res =requests.get(url.format(page),headers=headers)      #requests = html字串

    soup = BeautifulSoup(res.text,'html.parser')

    title_list = soup.select('div.title')
    #print(title_list)


    for title_soup in title_list:
        #print(title_soup)
            title = title_soup.select('a')[0].text  #以a標籤進行定位,在取第0個的標題
            print(title)
            title_url = 'https://www.ptt.cc' +title_soup.select('a')[0]['href']
            print(title_url)


    page -= 1   #每按一次上一頁,數值都會減1(8794-8973-8972......)
