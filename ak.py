# import akshare as ak
# import pandas as pd

# # 获取2023年沪深300的日K线数据
# df = ak.stock_zh_index_daily_em(symbol="sh000300", start_date="20200101", end_date="20230810") 

# # 将数据输出到CSV文件
# df.to_csv("sh000300_2023.csv", index=False)



# import time
# import akshare as ak
# from snownlp import SnowNLP
 
# stock_code = '600887'
# date = time.strftime("%Y%m%d", time.localtime())
# stock_news_em_df = ak.stock_news_em(symbol=stock_code)
 
# positive = 0
# negative = 0
# for i in stock_news_em_df.values[:, 1]:
#     text = str(i)
#     s = SnowNLP(text)
#     for sentence in s.sentences:
#         print(sentence, SnowNLP(sentence).sentences)
#     #print(s.sentiments)
#     #print(s.keywords(3))
#     #print(s.summary(3))
#     # 小于0.4的为悲观，否则为乐观
#     if s.sentiments < 0.4:
#         print('##########悲观', i)
#         negative += 1
#     elif s.sentiments >= 0.4:
#         print('##########乐观', i)
#         positive += 1
 
# print("乐观:悲观 比例 {}:{}".format(positive, negative))



# import akshare as ak
# import pandas as pd

# # 获取沪深300当前成分股
# zz500_stocks = ak.stock_zh_index_cons(index="600887") 

# # 搜索标题包含"沪深300"的新闻
# news_list = []
# for stock in zz500_stocks['cons']:
#     print(f"获取{stock}相关新闻...")
#     news = ak.stock_zh_a_spot()
#     news = news[news['title'].str.contains(stock)]
#     news_list.append(news)
    
# news_df = pd.concat(news_list, ignore_index=True)

# 显示结果
# print(news_df)



# import akshare as ak
# stock_news_em_df = ak.stock_news_em("000300")
# print(stock_news_em_df)




# import requests
# from bs4 import BeautifulSoup


# resp = requests.get('https://finance.eastmoney.com/a/202308102809157722.html')
# soup = BeautifulSoup(resp.text, 'html.parser')

# title = soup.title
# print(title.text)



import requests
from bs4 import BeautifulSoup

url = 'https://finance.eastmoney.com/a/czqyw.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

news_list = soup.find('div', class_='newsList')
a_tags = news_list.find_all('a')

for a in a_tags:
    print(a.text)