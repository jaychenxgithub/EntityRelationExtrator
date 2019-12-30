# -*- coding: utf-8 -*-
import os
LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']

# ====================================================


arcs = parser.parse(words, postags)  # 句法分析

print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))


#===========================================
text = '張忠謀住在台北市信義區附近, 應該是帝寶大廈, 而且已經從台積電退休了'
text = '張忠謀住在帝寶大廈, 而且已經從台積電退休了'

from pyltp import Postagger
from pyltp import Segmentor
from pyltp import NamedEntityRecognizer

pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

postagger = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path, './model/lexicon')  # 加载模型, 及自定外部詞典
#postagger.load(pos_model_path)  # 加载模型, 及自定外部詞典

segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path, './model/lexicon') # 加载模型，第二个参数是您的外部词典文件路径
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型

words = segmentor.segment(text)
postags = postagger.postag(words)  # 词性标注
netags = recognizer.recognize(words, postags)  # 命名实体识别

arcs = parser.parse(words, postags)  # 句法分析

print ('=' * 30)
print ('\t'.join(words))
print ('\t'.join(postags))
print ('\t'.join(netags))
print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))


postagger.release()
segmentor.release()
recognizer.release()  # 释放模型

parser.release()  # 释放模型