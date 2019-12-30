# -*- coding: utf-8 -*-
import os
LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

from pyltp import CustomizedSegmentor
customized_segmentor = CustomizedSegmentor()  # 初始化实例
#customized_segmentor.load(cws_model_path, '/path/to/your/customized_model') # 加载模型，第二个参数是您的增量模型路径
#customized_segmentor.load(cws_model_path, '/path/to/your/customized_model') # 加载模型，第二个参数是您的增量模型路径

customized_segmentor.load_with_lexicon(cws_model_path, '/path/to/your/customized_model', './model/lexicon') # 加载模型

words = customized_segmentor.segment('亚硝酸盐是一种化学物质')
print ('\t'.join(words))
customized_segmentor.release()