# -*- coding: utf-8 -*-
from gensim.models import word2vec

#中文训练词向量需要多加这一步
sentences = word2vec.Text8Corpus(u'./datasets/train.txt')
#size是神经网络的隐藏层单元数，也就是后续每个词向量的维度，默认为100
model = word2vec.Word2Vec(sentences, size=50, min_count=1)

print(model.most_similar([u'公路'], topn=3))
print(model[u'距离'])