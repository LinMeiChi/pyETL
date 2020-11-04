#
import requests
from bs4 import BeautifulSoup
import  os
import re

if not os.path.exists('pttmovie'):  #如果沒有資料夾,就自己創一個
    os.mkdir('pttmovie')        #創一個資料夾存文章內容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'        #要爬蟲的網址


for i in range(0,5):
    res =requests.get(url,headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')

    title_list = soup.select('div.title')
    #print(title_list)


    for title_soup in title_list:
        #print(title_soup)
        try:
            title = title_soup.select('a')[0].text
            title_url = "https://www.ptt.cc" + title_soup.select('a')[0]["href"]

            # Get article content   取得文章內容 -以下到print是複製09
            res_article = requests.get(title_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, "html.parser")
            # print(soup_article)
            article_content_list = soup_article.select('#main-content')
            articles_content = article_content_list[0].text.split("※ 發信站")[0]
            try:
                with open('./pttmovie/%s.txt'%(title), 'w',encoding="utf-8") as f:
                    f.write(articles_content)
            except FileNotFoundError as  e:
                print(e)
                print(title)
                with open('./pttmovie/%s.txt'%(title.replace('/','-')), 'w',encoding='utf-8') as f:
                    f.write(articles_content)
            except OSError as  e_t:
                print(e_t)
                print(title)
                with open('./pttmovie/%s.txt'% (re.sub('["\\","/",":","*","?","<",">","|"]','',title)), 'w',encoding='utf-8') as f:    #去除特殊字元
                    f.write(articles_content)

            print(title)
            print(title_url)
            print(articles_content)
            print('------------------------')
        except  IndexError as e:
            print(title_soup)
    #取得上一頁網址
    page_url_soup = soup.select('a[class="btn wide"]')      #從最舊取得class="btn wide   (無規律地可以從這找,07為有規律的寫法)
    #print(page_url_soup)
    last_page_url = 'https://www.ptt.cc' + page_url_soup[1]['href'] #再挑出要得(第一個是我要的,故取[1])
    #print(last_page_url)
    url = last_page_url