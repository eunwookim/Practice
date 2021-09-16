from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

## 1~50페이지 가져오기
## 댓글 1페이지의 댓글 전체 가져오기-10개
basic_url = 'https://movie.naver.com/movie/bi/mi/review.naver?code=167638&page='
comments = []
for i in range(1,51,1):
    real_url = basic_url+str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_='title')
    for one in comment_all:
        temp = list(one.children)[6].strip()
        comments.append(temp)



dat_dict={'영화 리뷰': comments}

dat=pd.DataFrame(dat_dict)
dat.to_csv("네이버 영화 리뷰.csv",index=False)
dat.to_excel("네이버 영화 리뷰.xlsx",index=False)
