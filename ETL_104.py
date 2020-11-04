import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import re

file_data = (r'./104homework')
if not os.path.exists(file_data):
    os.mkdir(file_data)

headers = {
    "User=Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url_fir = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={}&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc"

df = pd.DataFrame(
    columns=['網址', '公司名稱', '職稱', '工作內容', '工作待遇', '工作性質', '上班地點', '管理責任', '出差外派', '上班時段', '休假制度', '可上班日', '需求人數', '工作經歷',
             '學歷要求', '科系要求', '語言條件', '工作技能', '福利制度'])

keyword = input("輸入關鍵字", )

page = 1    #頁數起始值
json_final = []         #用來將每一篇的資訊裝入同一個list中,才能存入
for q in range(0, 10):  #頁數迴圈
    res_fir = requests.get(url_fir.format(keyword, page), headers=headers)
    soup_fir = BeautifulSoup(res_fir.text, "html.parser")

    position = soup_fir.select('h2.b-tit')
    json_list = []
    json_list_try = []
    h_append = []
    g_append = []

    for title_soup in position:
        if title_soup.select('a.js-job-link') != []:
            title_url = title_soup.select('a.js-job-link')[0]["href"]
            # print(title_url)

            # 正常網址
            url_w = "https:" + title_url
            url_a = url_w.split("?", 1)[0]

            headerss = {
                "User=Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                "Referer": url_w,
            }

            # 從F12 - Network - XHR - 6開頭 - Request URL 查詢(才這裡才爬的到東西) 104比較特別,才需要用這種方式,一般不需要用這種方式就能爬的到資料
            w = url_a.split("b/", 1)[0]
            q = url_a.split("b/", 1)[1]
            url = w + "b/ajax/content/" + q
            # print(url)
            res = requests.get(url, headers=headerss)
            json_array = json.loads(res.text)

            # print(json_array)

            store_details = {'custUrl': '', 'custName': '', 'jobNam': '', 'jobDescription': '', 'salary': '',
                             'jobType': '', 'address': '', 'manageResp': '', 'businessTrip': '', 'workPeriod': '',
                             'vacationPolicy': '', 'startWorkingDay': '', 'needEmp': '', 'workExp': '', 'edu': '',
                             'major': '', 'language': '', 'skill': '', 'welfare': ''}  # 字典 dic={key:value}

            store_details['custUrl'] = json_array['data']['header']['custUrl']  # 網址
            store_details['custName'] = json_array['data']['header']['custName']  # 公司名稱
            store_details['jobNam'] = json_array['data']['header']['jobName']  # 職稱
            store_details['jobDescription'] = json_array['data']['jobDetail']['jobDescription'].replace("\r\n",
                                                                                                        " ").replace(
                "•\t", "")  # 工作內容
            store_details['salary'] = json_array['data']['jobDetail']['salary']  # 工作待遇
            store_details['jobType'] = json_array['data']['jobDetail']['jobType']  # 工作性質
            store_details['address'] = json_array['data']['jobDetail']['addressRegion'] + \
                                       json_array['data']['jobDetail']['addressDetail']  # 上班地點
            store_details['manageResp'] = json_array['data']['jobDetail']['manageResp']  # 管理責任
            store_details['businessTrip'] = json_array['data']['jobDetail']['businessTrip']  # 出差外派
            store_details['workPeriod'] = json_array['data']['jobDetail']['workPeriod']  # 上班時段
            store_details['vacationPolicy'] = json_array['data']['jobDetail']['vacationPolicy']  # 休假制度
            store_details['startWorkingDay'] = json_array['data']['jobDetail']['startWorkingDay']  # 可上班日
            store_details['needEmp'] = json_array['data']['jobDetail']['needEmp']  # 需求人數
            store_details['workExp'] = (json_array['data']['condition']['workExp'])  # 工作經歷
            store_details['edu'] = (json_array['data']['condition']['edu'])  # 學歷要求
            store_details['major'] = (json_array['data']['condition']['major'])  # 科系要求
            store_details['language'] = json_array['data']['condition']['language']  # 語言條件
            store_details['skill'] = (json_array['data']['condition']['skill'])  # 工作技能
            store_details['welfare'] = json_array['data']['welfare']['welfare']  # 福利制度

            # print(store_details['welfare'])
            # print(store_details[])

            # 科系要求
            if store_details['major'] == []:
                store_details['major'] = '無要求'

            # 工作性質(1為全職、2為兼職)
            if store_details['jobType'] == 1:
                store_details['jobType'] = '全職'
            if store_details['jobType'] == 2:
                store_details['jobType'] = '兼職 - 長期工讀'

            # 語言條件
            if store_details['language'] == []:
                store_details['language'] = '無要求'
            else:
                language = []
                for l in store_details['language']:
                    a = l['language']
                    b = l['ability']
                    store_details['language'] = a + ':' + b

            # 工作技能
            if store_details['skill'] == []:
                store_details['skill'] = '無要求'
                # print(store_details['skill'])
            else:
                j_append = []       #將多值的工作技能裝到同一個list中(不可放入for迴圈中,會產生累加)
                for i_append in store_details['skill']:
                    j_append.append(i_append['description'])
                    g_append = '、'.join(j_append)
                store_details['skill'] = g_append

            json_list_try = list(store_details.values())        #取store_details中的值,放入list中,代表一個工作的內容
            json_list.append(json_list_try)     #將一整頁中每個工作包在一個list,代表一整頁所有工作的內容
    json_final += (json_list)     #將所有查詢頁數的工作內容包在同一個list中,才會符合csv格式


    page += 1
print(json_final)

dff=df.append(pd.DataFrame(json_final,columns=['網址','公司名稱','職稱','工作內容','工作待遇','工作性質','上班地點','管理責任','出差外派','上班時段','休假制度','可上班日','需求人數','工作經歷','學歷要求','科系要求','語言條件','工作技能','福利制度']))
dff.to_csv(r'./104homework/104.csv',index=False,encoding="utf-8-sig")
