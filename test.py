import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns #sns는 기본적으로 sns(x데이터,y데이터,hue데이터,data=참고할 데이터

fg = sns.load_dataset("flights")
fgpiovt=fg.pivot("month","year","passengers")
sns.heatmap(fgpiovt,annot=True,fmt='d')
plt.show()

