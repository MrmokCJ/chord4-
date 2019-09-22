import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
#把自己想分析的文本都粘到下面这个文件吧
with open('movie.txt','r',encoding='utf-8') as f:
    string_data = f.read()
    
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
string_data = re.sub(pattern, '', string_data)

seg_list_exact = jieba.cut(string_data, cut_all = False)
object_list = []
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要','\xa0',r'/',u'\D{0,3}']

for word in seg_list_exact: 
    if word not in remove_words: 
        object_list.append(word)

word_counts = collections.Counter(object_list) 
word_counts_top10 = word_counts.most_common(10) 


mask = np.array(Image.open(r'D:\Daliy PS\莫承健.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='‪C:\Windows\Fonts\msyh.ttc', # 设置字体格式
    mask=mask, # 设置背景图
    max_words=150, # 最多显示词数
    max_font_size=1000, # 字体最大值
    background_color='white',
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像