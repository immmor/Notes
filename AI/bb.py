import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 示例数据集
documents = [
    "苹果是一种水果",
    "香蕉是一种水果",
    "苹果和香蕉都是水果",
    "桃子是一种水果",
    "橙子是一种水果",
]

# 使用TF-IDF向量化文档
vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(documents)

# 用户查询
query = "我想吃水果"

# 将查询向量化
query_vector = vectorizer.transform([query])

# 计算查询向量与文档向量的相似度
similarities = cosine_similarity(query_vector, document_vectors).flatten()

# 根据相似度进行排序
sorted_indices = np.argsort(similarities)[::-1]

# 打印相似的文档
for index in sorted_indices:
    print(f"相似度：{similarities[index]:.2f}，文档：{documents[index]}")