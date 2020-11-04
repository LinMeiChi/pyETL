import requests
from bs4 import BeautifulSoup
import  os
import re
if not os.path.exists('ptthomework'):  #如果沒有資料夾,就自己創一個
    os.mkdir('ptthomework')        #創一個資料夾存文章內容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'        #要爬蟲的網址
ss = requests.session()
ss.cookies['over18'] = '1'

for i in range(0,10):
    res =ss.get(url,headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')

    title_list = soup.select('div.title')

    for title_soup in title_list:
        try:
            title = title_soup.select('a')[0].text
            title_url = "https://www.ptt.cc" + title_soup.select('a')[0]["href"]
            illegal = ['\\', '/', ':', '*', '?', '"', "'", '<', '>', '|']
            for i in illegal:  # 換掉所有非法字元
                title = title.replace(i, '_')

            #print(title)
            print(title_url)
            res_article = ss.get(title_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, "html.parser")
            article_content_list = soup_article.select('#main-content')
            articles_content = article_content_list[0].text.split("--")[0]
            print(articles_content)


            article_select_up = soup_article.select('span[class="hl push-tag"]')
            push_up = 0
            for up in article_select_up:
                push_up += 1
            print("推:", push_up)

            article_select_down = soup_article.select('span[class="f1 hl push-tag"]')
            push_down = 0
            for down in article_select_down:
                if down.text[0] == "噓":
                    push_down += 1
            print("噓:", push_down)

            article_select_author = soup_article.select('span[class="article-meta-value"]')[0].text
            print("作者:", article_select_author)

            article_select_time = soup_article.select('span[class="article-meta-value"]')[3].text
            print("時間:", article_select_time)
            try:
                with open('./ptthomework/%s.txt' % (title), 'w', encoding="utf-8") as f:
                    f.write(articles_content)
                    print("---split---",file=f)
                    print("推:", push_up, file=f)
                    print("噓:", push_down, file=f)
                    print("作者:", article_select_author, file=f)
                    print("標題:", title, file=f)
                    print("時間:", article_select_time, file=f)
            except OSError as e_t:
                print(e_t)
                print(title)

                with open('./ptthomework/%s.txt'% (re.sub('["\\","/",":","*","?","<",">","|"]','',title)), 'w',encoding='utf-8') as f:    #去除特殊字元
                    f.write(articles_content)
                    print("---split---", file=f)
                    print("推:", push_up, file=f)
                    print("噓:", push_down, file=f)
                    print("作者:", article_select_author, file=f)
                    print("標題:", title, file=f)
                    print("時間:", article_select_time, file=f)

        except IndexError as e:
            print(e)
            print(title_soup)






    page_url_soup = soup.select('a[class="btn wide"]')[1]
    last_page_url = 'https://www.ptt.cc' + page_url_soup['href']
    url = last_page_url