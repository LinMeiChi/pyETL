#需重聽(5/30)
import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#url和data都是從F12 - Network - admin-ajax.php取得(因為網頁不斷往下滑,伺服器會一直不斷產生相同名稱,故觀察每個,發現其內容相關,page也是不斷增加)
url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'       #用POST的方式訪問網址

data={"action": "fm_ajax_load_more",
      "nonce": "d8c08f1381",
      "page": "1"}      #page數目前只有第一頁,想抓多頁,可使用迴圈

res = requests.post(url, headers=headers, data=data) #用POST方式取得request(帶入POST data)
json_data = json.loads(res.text)

# print(json_data)
# print(json_data.keys())
# print(json_data["data"]) #html string

soup = BeautifulSoup(json_data["data"],"html.parser")       #將html字串轉成BeautifulSoup(可定位)型態,即可取自己想要的內容
title_list = soup.select('a[class="post-thumbnail nljf"]')
#print(title_list)
for t in title_list:
     print(t)
     print(t["onclick"])