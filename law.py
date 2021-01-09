from time import sleep
from selenium import webdriver
import requests


#url = "https://www.courts.go.jp/app/hanrei_jp/list1?filter%5Btext1%5D=%E7%9F%A5%E8%B2%A1&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=&filter%5Btext8%5D=&filter%5Btext9%5D=&filter%5BjudgeGengoFrom%5D=&filter%5BjudgeYearFrom%5D=&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=&filter%5BjudgeYearTo%5D=&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&action_search=%E6%A4%9C%E7%B4%A2"
#response = requests.get(url)
#print(response.text[:500])

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
driver.get('https://www.courts.go.jp/app/hanrei_jp/search1')
search_bar = driver.find_element_by_name("filter[text1]")
search_bar.send_keys("GPS")
search_bar.submit()

#Xpathで要素を抽出し、formatでtr[]の値を変更する
#それをクリックしてページ表示
for i in range(1,11):
    x_path = "//*[@id='main-contents']/div[2]/div/div[3]/div[5]/table/tbody/tr[{0}]/td[2]/a".format(i)
    driver.find_element_by_xpath(x_path).click()

#ページ遷移させる
#i = 0
#while True:
    #i = i + 1
    #sleep(1)
    #next_link = driver.find_element_by_xpath("//a[@title='検索結果を次のページへ移動']").click()
    #if i > 10:
        #break
