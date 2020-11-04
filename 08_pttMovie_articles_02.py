import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'        #要爬蟲的網址

for i in range(0,5):
    res =requests.get(url,headers=headers)      #requests = html字串

    soup = BeautifulSoup(res.text,'html.parser')

    title_list = soup.select('div.title')
    #print(title_list)


    for title_soup in title_list:
        #print(title_soup)
        try:
            title = title_soup.select('a')[0].text  #以a標籤進行定位,在取第0個的標題


            title_url = 'https://www.ptt.cc' +title_soup.select('a')[0]['href']
            print(title)
            print(title_url)
        except IndexError as e:
            print(title_soup)

    #取得上一頁網址
    page_url_soup = soup.select('a[class="btn wide"]')      #從最舊取得class="btn wide   (無規律地可以從這找,07為有規律的寫法)
    #print(page_url_soup)
    last_page_url = 'https://www.ptt.cc' + page_url_soup[1]['href'] #再挑出要得(第一個是我要的,故取[1])
    #print(last_page_url)
    url = last_page_url