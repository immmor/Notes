# import jieba

# # 精确模式分词
# text = "我喜欢使用jieba库进行中文分词"
# seg_list = jieba.cut(text, cut_all=False)
# print("精确模式分词：", "/ ".join(seg_list))

# # 全模式分词
# seg_list = jieba.cut(text, cut_all=True)
# print("全模式分词：", "/ ".join(seg_list))

# # 搜索引擎模式分词
# seg_list = jieba.cut_for_search(text)
# print("搜索引擎模式分词：", "/ ".join(seg_list))



import jieba

# 添加自定义词典
jieba.add_word("自然语言处理")
jieba.add_word("文本分析")

text = "我喜欢使用jieba库进行中文分词和自然语言处理"
seg_list = jieba.cut(text)
print("分词结果：", "/ ".join(seg_list))





# import jieba.analyse

# text = "自然语言处理是人工智能领域的重要研究方向之一"
# keywords = jieba.analyse.extract_tags(text, topK=3)
# print("关键词提取：", keywords)