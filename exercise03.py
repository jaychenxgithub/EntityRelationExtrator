import os
LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

text = '亚硝酸盐是一种化学物质'
text = '張忠謀住在台北市信義區附近, 應該是帝寶大廈, 而且已經從台積電退休了'

from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path, './model/lexicon') # 加载模型，第二个参数是您的外部词典文件路径
words = segmentor.segment(text)
print ('\t'.join(words))
segmentor.release()