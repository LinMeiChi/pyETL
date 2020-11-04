#抓文章內容

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

title_url = 'https://www.ptt.cc/bbs/movie/M.1590058721.A.C94.html'

res_article = requests.get(title_url,headers=headers)

soup_article = BeautifulSoup(res_article.text,'html.parser')
#print(soup_article)
article_content_list = soup_article.select('#main-content')
#取第0個(text是取所有內容),再以※ 發信站進行分割,分割後取第0個
print(article_content_list[0].text.split('※ 發信站')[0])