from selenium import webdriver
from bs4 import BeautifulSoup
import time

# #filename = "datalab_word.xlsx"
# #sheetname = input("시트명을 입력해 주세요. :")
# driver =  webdriver.Chrome("C:/chromedriver.exe")
# url="https://datalab.naver.com/"
# driver.get(url)
# # xpath 규칙 찾아보기
# soup=BeautifulSoup(driver.page_source,'lxml')
# word = driver.find_elements_by_css_selector("span.title")
# list=[]
# for one in word:
#     word_all = one.text
#     list.append(word_all)
#     print(word_all)
# print(list)


driver = webdriver.Chrome('C:/chromedriver.exe')
url = "https://datalab.naver.com/"
driver.get(url)

for j in range(1,13,1):
    date = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div['+ str(j) +']/div/div/ul/li/a/span'
    keyword_all = []
    for i in range(1,11):
        sel_base = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div['+str(j)+']/div/div/ul/li['+ str(i) +']/a/span'
        sel_element = driver.find_element_by_xpath(sel_base)
        print(sel_element.text)
        dat = sel_element.text
        keyword_all.append(dat)
    print(keyword_all)
    time.sleep(5)