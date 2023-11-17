import akshare as ak
import pandas as pd

# 获取2023年沪深300的日K线数据
df = ak.stock_zh_index_daily_em(symbol="sh000300", start_date="20200101", end_date="20230810") 

# 将数据输出到CSV文件
df.to_csv("sh000300_2023.csv", index=False)



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




import requests
from bs4 import BeautifulSoup


resp = requests.get('https://finance.eastmoney.com/a/202308102809157722.html')
soup = BeautifulSoup(resp.text, 'html.parser')

title = soup.title
print(title.text)



# import requests
# from bs4 import BeautifulSoup

# url = 'https://finance.eastmoney.com/a/czqyw.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')

# news_list = soup.find('div', class_='newsList')
# a_tags = news_list.find_all('a')

# for a in a_tags:
#     print(a.text)



# import akshare as ak
# stock_zh_a_alerts_cls_df = ak.stock_zh_a_alerts_cls()
# print(stock_zh_a_alerts_cls_df)
# stock_telegraph_cls = ak.stock_telegraph_cls()
# print(stock_telegraph_cls)



# import akshare as ak
# news_economic_baidu = ak.news_economic_baidu('20230802')
# print(news_economic_baidu)



# import akshare as ak

# symbol = "sh000300"
# # start_date = "2022-01-01"
# # end_date = "2022-12-31"

# data = ak.stock_zh_a_minute(symbol=symbol)
# print(data)
# # 将数据输出到CSV文件
# data.to_csv("sh000300_1min.csv", index=False)





# import pandas as pd
# import matplotlib.pyplot as plt

# # 读取数据
# df = pd.read_csv('sh000300_1min.csv')  

# # 绘制开盘收盘最高最低价折线图
# plt.plot(df['open'], label='Open')
# plt.plot(df['close'], label='Close')
# plt.plot(df['high'], label='High')
# plt.plot(df['low'], label='Low')
# plt.legend(loc='best')

# # 绘制交易量柱状图  
# plt.figure()
# plt.bar(df.index, df['volume'])

# # 计算并绘制MACD
# exp1 = df['close'].ewm(span=12, adjust=False).mean()
# exp2 = df['close'].ewm(span=26, adjust=False).mean() 
# macd = exp1-exp2
# exp3 = macd.ewm(span=9, adjust=False).mean()
# plt.figure()
# plt.plot(macd, label='MACD')  
# plt.plot(exp3, label='Signal Line')
# plt.legend(loc='best')

# # 计算并绘制RSI
# delta = df['close'].diff()
# up = delta.clip(lower=0)
# down = -1*delta.clip(upper=0)  
# ema_up = up.ewm(com=13, adjust=False).mean()
# ema_down = down.ewm(com=13, adjust=False).mean()  
# rs = ema_up/ema_down
# df['RSI'] = 100 - (100/(1 + rs))
# plt.figure()
# plt.plot(df['RSI'], label='RSI')
# plt.legend(loc='best')

# # 显示所有图表
# plt.show()
