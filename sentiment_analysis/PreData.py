# Predict Model
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import pickle
import jieba

# 获取停用词
def StopWords():
        with open('/Users/superchen/Qt_Project/TestPyQt/sentiment_analysis/train_data/stopwords.txt','r',encoding = 'utf-8') as f:
                lines = f.readlines()
        stopWords = []
        for line in lines:
                stopWords.append(line)
        return stopWords
# 读取训练数据，并去除停用词

# 读取训练数据，并去除停用词
def read_data(input_sen):
	sentence = []
	trans = list(jieba.cut(input_sen.strip(), cut_all=False))

	for word in trans:
		if word not in stopWords:
			sentence.append(word)
	return sentence
	
def words2Array(line):
	linesArray = []
	wordsArray = []
	steps = []

	t = 0
	p = 0
	for i in range(MAX_SIZE):
		# 如果小于MAX_SIZE 则用0.0的矩阵补齐
		if i < len(line):
			try:
				wordsArray.append(word2vec_model.wv.word_vec(line[i]))
				p = p + 1
			except KeyError:
					# 如果在词向量模型中没有找到对应词的向量
				t = t + 1
				continue
		else:
			wordsArray.append(np.array([0.0] * vector_size))

	for i in range(t):
		wordsArray.append(np.array([0.0] * vector_size))
	steps.append(p)
	linesArray.append(wordsArray)

	linesArray = np.array(linesArray)
	steps = np.array(steps)
	return linesArray, steps

stopWords = StopWords()
word2vec_path = '/Users/superchen/Qt_Project/TestPyQt/sentiment_analysis/word2vec/word2vec.pkl' # 词向量地址
file = open(word2vec_path, 'rb')
word2vec_model = pickle.load(file )
vector_size=word2vec_model.vector_size # 词向量的维度
# 将输入数据处理成向量矩阵
MAX_SIZE=25 # 句子的统一长度

def run(input_words):
        if input_words == "":
                return "请输入想要测试的文本后重试！"
	#Input
        input_sen = input_words
        # 分词和去除停用词
        imput_data = read_data(input_sen)
        # 构造好输入数据
        data, steps = words2Array(imput_data)
        num_nodes = 128  #
        batch_size = 1 #一次喂给训练器的数据条数
        output_size = 2 #输出的维度

        with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                saver = tf.train.import_meta_graph('/Users/superchen/Qt_Project/TestPyQt/sentiment_analysis/model/model-senti.meta')
                saver.restore(sess, tf.train.latest_checkpoint("/Users/superchen/Qt_Project/TestPyQt/sentiment_analysis/model/"))
                prediction = tf.get_collection('pred_network')[0]

                graph = tf.get_default_graph()

                input_x = graph.get_operation_by_name('input_x').outputs[0]
                input_steps = graph.get_operation_by_name('steps').outputs[0]

                pre = sess.run(prediction, feed_dict={input_x:data, input_steps: steps})

        output = "所需要预测的句子为:\n" + input_words + "\n"
        if pre[0][0] > pre[0][1]:
                output += "句子的情感极性: 积极"
        else:
                output += "句子的情感极性: 消极"
        return output
