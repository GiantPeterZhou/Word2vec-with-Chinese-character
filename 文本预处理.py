# -*- coding: utf-8 -*-
import pandas as pd
raw_data = pd.read_csv('./datasets/ChnSentiCorp_htl_all.csv')

#观察数据分布
#print('评论总数：%d' % raw_data.shape[0])
#print('积极评论：%d' % raw_data[raw_data.label==1].shape[0])
#print('负面评论：%d' % raw_data[raw_data.label==0].shape[0])

#得到文本数据
#text = raw_data.drop(['label'], axis=1)
text = []
for i in range(raw_data.shape[0]):
    text.append(str(raw_data.review[i]))

comment = '\n'.join(text)

#清洗文本数据-用正则表达式删去数字、字母、标点符号、特殊符号等
import re
symbols = "[A-Za-z0-9\!\%\[\]\,\。\.\，\、\~\?\(\)\（\）\？\！\“\”\:\：\;\"\"\；\……&\-\_\|\．\Ａ．Ｂ．Ｃ\*\^]"
comments = re.sub(symbols, '', comment)

#分词
import jieba
comments_list = jieba.cut(comments)#精确模式
#comments_list = jieba.cut_for_search(comments)#搜索引擎模式
x_train = ' '.join([x for x in comments_list]) #用空格连接分好的词

#保存数据
open('./datasets/train.txt', 'w+',encoding='utf8').write(x_train) 
