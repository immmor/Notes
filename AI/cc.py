from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 示例中文文本数据
documents = [
    "这是第一篇文档",
    "这个文档是第二篇文档",
    "这是第三个文档",
    "这是第一篇文档吗？"
]

# 使用TaggedDocument对文本进行标记和分词
tagged_documents = [TaggedDocument(words=jieba.lcut(document), tags=[str(i)]) for i, document in enumerate(documents)]

# 构建Doc2Vec模型
model = Doc2Vec(tagged_documents, vector_size=100, window=5, min_count=1, workers=4, epochs=20)

# 获取句子向量
sentence_vectors = [model.infer_vector(jieba.lcut(document)) for document in documents]

# 计算句子间的相似度矩阵
similarity_matrix = cosine_similarity(sentence_vectors)

# 绘制相似度矩阵的热力图
plt.imshow(similarity_matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Similarity Matrix')
plt.show()