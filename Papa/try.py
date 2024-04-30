from DrissionPage import SessionPage
from re import search

# 以s模式创建页面对象
page = SessionPage()
# 访问目标网页
page.get('https://www.starbucks.com.cn/menu/')

# 获取所有class属性为preview circle的元素
divs = page.eles('.preview circle')
# 遍历这些元素
for div in divs:
    # 用相对定位获取当前div元素后一个兄弟元素，并获取其文本
    name = div.next().text

    # 在div元素的style属性中提取图片网址并进行拼接
    img_url = div.attr('style')
    img_url = search(r'"(.*)"', img_url).group(1)
    img_url = f'https://www.starbucks.com.cn{img_url}'

    # 执行下载
    page.download(img_url, r'.\imgs', rename=name)