from pandas import Series,DataFrame
import pandas as pd
# score = Series([1000,14000,3000],
#                index=['2019-05-01','2019-05-02','2019-05-03'])
# score = Series(['a','b','c'],
#                index=['2021-09-16','2021-09-17','2021-09-18'])
#
#
# idx=pd.date_range('2021-09-10',"2021-09-12").tolist()
# date=Series(['a','b','c'],
#             index=idx)
# idx=pd.date_range('2021-07-01','2021-09-28').tolist()
# day=range(1,91)
# date=Series(day,index=idx)
# print(date)

# dat = {'col1':[1,2,3,4],
#        'col2':[10,20,30,40],
#        'col3':['A',"B",'C','D']}
# dt=DataFrame(dat)
# print(list(dt.index))

#DataFrame에서 슬라이싱 인덱싱 이용
from pandas import DataFrame

team_score = { "toto":[1500,3000,5000,7000,5500],
               "apple":[4000,5000,6000,5500,4500],
               "gildong":[2000,2500,3000,4000,3000],
               "catanddog":[7000,5000,3000,5000,4000]}

team_df = DataFrame(team_score)
# print(team_df)
# #변수에 넣어서 선택-원하는 행과 열 넣어서 가져오기
# set = {"apple":[4000,5000,6000,5500,4500],
#        "gildong":[2000,2500,3000,4000,3000]}
# #[[]]써서 -열선택 행선택 가능
# #loc,iloc사용 -시리즈 형태로 가져오기(loc[0,:],데이터프레임 형태로 가져오기([[0],[]]),-열선택 행선택 가능

import seaborn as sns
t=sns.load_dataset('titanic')
print(t)
mean=t['Fare'].mean()
