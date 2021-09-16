from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup=BeautifulSoup(page,"lxml")

title = soup.find_all("dt",class_="tit")

list_all=[]
for one in title:
    title_one=one.find("a").text
    list_all.append(title_one)


score = soup.find_all("dl",class_="info_star")
#print(score[0].find("span",class_='num').text)

all_score=[]
for one in score:
    one_score = one.find("span",class_="num").text
    all_score.append(one_score)

exp = soup.find_all("div",class_="star_t1 b_star")
all_exp=[]
for one in exp:
    one_exp=one.text
    all_exp.append(one_exp)

person = soup.find_all("span",class_="num2")
list=[]
for one in person:
    person_one = one.text
    list.append(person_one)



#파일 만들기(타이틀, 평점, 참여명수,예매율)

import pandas as pd
# dict_dat = {"영화제목":list_all,
#             "평점":all_score,
#             "참여명수":all_exp,
#             "예매율":list}
# dat = pd.DataFrame(dict_dat)
# print(dat)


