from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://www.amazon.com/'
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get(url)
# //*[@id="lnb.searchForm"]/fieldset/input[1] # 검색 내용
# //*[@id="lnb.searchForm"]/fieldset/button/span # 검색
# text_today_main_news_801001 > li:nth-child(1) > div > a > strong
# selected_xpath = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
# selected_xpath_search = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
# selected_xpath.send_keys('computer')
# #print(selected_xpath.tag_name)
# print(selected_xpath.text)
# selected_xpath_search.click()
#
# #현재 페이지 소스 가져오기
# page=driver.page_source - 현재 페이지 정보 전달
# soup=BeautifulSoup(page,'html.parser')
#
# #현재 url 가져오기
# current_url = driver.current_url
# print(current_url)
#
# #현재 페이지에서 첫 상품 가져오기(전체 상품에 관한 태그 가져오고
# # 거기서 인덱스로[] 첫번째 요소 값을 가져온다.
# tmp = soup.find_all('h2',class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")[0]
# print(tmp.a.attrs['href'])
#


#아마존 리뷰 가져오기
url = 'https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/dp/B0849GZCQR/ref=sr_1_2?dchild=1&keywords=computer&qid=1631254252&sr=8-2'
driver.get(url)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_r = soup.find_all("span", class_="a-size-base review-text review-text-content")

all_review = []
for one in all_r:
    tmp = one.text
    review = tmp.strip()
    all_review.append(review)

print(all_review)

