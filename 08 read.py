import wordcloud
from wordcloud import WordCloud
from matplotlib import rc
import matplotlib.pyplot as plt

print(wordcloud.__version__)

f = open("네이버 영화 리뷰.csv", encoding = "utf-8")
text = f.read()
print(text)
f.close()

rc('font', family = "NanumGothic")

wcloud = WordCloud("C:/data/D2Coding.ttf",
                   max_words=1000,
                   relative_scaling=0.2).generate(text)

plt.figure(figsize=(7,7))
plt.imshow(wcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
plt.savefig('myfig.png')
