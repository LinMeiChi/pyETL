# P.64
import requests
import  json
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
import re


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'

res = requests.get(url,headers=headers)

#print(res.text)

json_data = json.loads(res.text)    #將外面的字串拿進來轉換成串列或字典

'''查看規則
print(json_data[0])
print(json_data[1])
print(json_data[2])
'''

'''#查看字典內有哪些key
for k in json_data[0]:      
    print(k)
'''

#取得標題
for t in json_data:         #每個t都是一個字典(例如:json_data[0]、json_data[1]......)
    title_name = t['title']
    print(title_name)
    #取網址
    article_url = 'https://www.dcard.tw/f/job/p' + str(t['id'])  #因為python不同型別不能相加(網址是字串、id是數字),故用str轉換id的型別
    print(article_url)      #印出會得到文章內所有的圖片網址(['https://imgur.dcard.tw/Sy04ugV.png', 'https://imgur.dcard.tw/Sy04ugV.png'])
    # P.68 抓每篇文章內的圖片
    image_url_list = [img['url'] for img in t['mediaMeta']]        #取得圖片網址(mediaMeta是圖片網址放置的地方)
    print(image_url_list)
    for image_url in image_url_list:
        # requests.urlretrieve(image_url,'./dcardimg/') + image_url.split('/')[-1])
        res_img = requests.get(image_url,headers=headers)       #訪問圖片的網址
        img_content= res_img.content #取下來像文字
        try:
            with open('./dcardimg/' + image_url.split('/')[-1],'wb') as f:
                f.write(img_content)
        except OSError as e:
            with open('./dcardimg/' + (re.sub('["\\","/",":","*","?","<",">","|"]', '', image_url.split('/')[-1])),'wb') as f:     #出錯,例外處理(去除特殊字元)

                f.write(img_content)



