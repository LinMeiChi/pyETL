from selenium.webdriver import Chrome

driver = Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)

driver.find_element_by_class_name('board-name').click()         # P.100 會跳出18禁的網站頁面
driver.find_element_by_class_name('btn-big').click()            # P.101 利用滿18歲的button(btn-big),成功進入的頁面

cookie = driver.get_cookies()       #取得cookie資訊
print(cookie)




