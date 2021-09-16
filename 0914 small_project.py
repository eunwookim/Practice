import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/chromedriver.exe')
url = "https://comic.naver.com/webtoon/weekday"
driver.get(url)
page = driver.page_source
soup=BeautifulSoup(page,'lxml')

def webtoon_top(i):
    for num in range(1, 4):
        one = driver.find_element_by_xpath('//*[@id="content"]/div[4]/div['+str(i)+']/div/ul/li[' + str(num) + ']/a')
        webtoon.append(one.text)
    return webtoon
def click(j):
    click = driver.find_element_by_xpath('//*[@id="content"]/div[4]/div['+str(j)+']/div/ul/li[1]/a')
    click.click()
    click1 = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr['+str(j+1)+']/td[2]/a')
    click1.click()


webtoon = []
day = input("TOP3 웹툰 요일을 선택해주세요. :")
day_all = driver.find_element_by_css_selector('div.list_area').text
if day == 'mon':
    date = driver.find_element_by_css_selector("h4.mon").text
    mon = webtoon_top(1)
    print(date)
    print(mon)
    click(1)
elif day=='tue':
    date = driver.find_element_by_css_selector("h4.tue").text
    tue = webtoon_top(2)
    print(date)
    print(tue)
    click(2)
elif day=='wed':
    date = driver.find_element_by_css_selector("h4.wed").text
    wed = webtoon_top(3)
    print(date)
    print(wed)
    click(3)
elif day=='thu':
    date = driver.find_element_by_css_selector("h4.thu").text
    thu = webtoon_top(4)
    print(date)
    print(thu)
    click(4)
elif day=='fri':
    date = driver.find_element_by_css_selector("h4.fri").text
    fri = webtoon_top(5)
    print(date)
    print(fri)
    click(5)
elif day=='sat':
    date = driver.find_element_by_css_selector("h4.sat").text
    sat = webtoon_top(6)
    print(date)
    print(sat)
    click(6)
elif day=='sun':
    date = driver.find_element_by_css_selector("h4.sun").text
    sun = webtoon_top(7)
    print(date)
    print(sun)
    click(7)
elif day=='all':
    for num1 in range(1,8):
        for num in range(1,3):
            xpath_all = '//*[@id="content"]/div[4]/div['+str(num1)+']/div/ul/li['+str(num)+']/a'
            one = driver.find_element_by_xpath(xpath_all)
            list + webtoon
            webtoon.append(one.text)
    print(webtoon)
else :
    print("요일을 다시 입력해주세요. :")










