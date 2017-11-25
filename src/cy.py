# coding:utf-8
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image

# 好友个性签名词云
itchat.login()
friends = itchat.get_friends(update=True)[0:]  # 获取所有好友列表
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)


text = "".join(tList)
# 分词
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# 字体存放路径
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         max_font_size=40, random_state=42,
                         font_path='windows/Fonts/Arial Unicode.ttf').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
