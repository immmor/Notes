import random


with open('data.txt', 'w') as f:
    # 循环生成10万条数据
    for i in range(100000000):
        # 生成随机字符串作为数据
        data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        # 将数据写入文件
        f.write(data + '\n')