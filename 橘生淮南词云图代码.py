# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:41:25 2019

@author: Administrator
"""
import matplotlib.pyplot as plt
import wordcloud
#from wordcloud import ImageColorGenerator
import jieba

# 1.图片遮罩层  将图片转化为 nd-array 形式
mask_pic=plt.imread('D:\PythonSpyder\橘生淮南词云图\枳.jpg')

    #实例化
w = wordcloud.WordCloud(font_path="D:\PythonSpyder\橘生淮南词云图\华康少女文字体7.otf", #设置字体
                        background_color = 'white',  # 设置图片背景颜色
                        max_words = 120,            # 设置最大词数
                        mask = mask_pic)
    #导入文本
txt = open(r'D:\PythonSpyder\橘生淮南词云图\橘生淮南.txt',encoding = 'utf-8').read()

    # 导入停用词
jieba.load_userdict(r'D:\PythonSpyder\橘生淮南词云图\停用词.txt')
# 2.分词
txt_cut = jieba.cut(txt)
    # 去停用词
newlist = [i for i in txt_cut if i not in open(r'D:\PythonSpyder\橘生淮南词云图\去停用词.txt',encoding = 'utf-8')]
#newlist = [i for i in txt_cut if i not in ['的', '他', '她','，','。','；','：','不','时候']]
txt1 = ' '.join(newlist)

w.generate(txt1)
# 3.生成图片
image=w.to_image()
# 4.显示图片
image.show()
# 5.保存图片
w.to_file('D:\PythonSpyder\橘生淮南词云图\枳词云图.jpg')

# 也可用 plt 来显示图片
    #plt.figure('橘生淮南')   #图片显示的名字
    #plt.imshow(w)
    #plt.axis('off')        #关闭坐标
    #plt.show()
