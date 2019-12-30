# -*- coding: utf-8 -*-
import os
LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

text = '元芳你怎么看'
text = '張忠謀住在台北市信義區附近'

from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
words = segmentor.segment(text)  # 分词
print ('\t'.join(words))
segmentor.release()  # 释放模型