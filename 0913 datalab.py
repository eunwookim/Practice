import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/chromedriver.exe')
url = "https://datalab.naver.com/"
driver.get(url)
page = driver.page_source
soup=BeautifulSoup(page,'lxml')

# 날짜 화면 왼쪽, 오른쪽 부분 보기 xpath
left_click_xpath= '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[1]/span'
right_click_xpath = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span'
left_click = driver.find_element_by_xpath(left_click_xpath)
right_click = driver.find_element_by_xpath(right_click_xpath)
# 날짜 가져오기
dates = soup.find_all("span", class_='title_cell')
for i in range(8):
    # 화면을 왼쪽 끝으로 이동시키기
    left_click.click()
    time.sleep(3)
    # 검색어 리스트로 만들기
lists = []
for day in range(1, 13):
    # 날짜 기록하기
    tmp_date = dates[day-1].text
    lists.append(tmp_date)
    # 하루의 검색어 10개 입력하기
    for num in range(1, 11):
        xpath_s = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div['+str(day)+']/div/div/ul/li['+str(num)+']/a/span'
        one_ele = driver.find_element_by_xpath(xpath_s)
        lists.append(one_ele.text)
    right_click.click()
    time.sleep(3)

print(lists)