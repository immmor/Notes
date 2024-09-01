import requests
from bs4 import BeautifulSoup
import os

# 创建保存图片的文件夹
if not os.path.exists('images'):
    os.makedirs('images')

# 设置要爬取的网页URL模板
url_template = 'https://pic.netbian.com/new/index_{}.html'

def download_image(img_url):
    try:
        img_data = requests.get(img_url).content
        img_name = os.path.join('images', img_url.split('/')[-1])
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
        print(f'已下载图片: {img_name}')
    except Exception as e:
        print(f'下载图片失败: {img_url} - 错误: {e}')

def main():
    for page_num in range(2, 3):  # 遍历所有页面，从第2页到第1048页
        url = url_template.format(page_num)
        try:
            # 获取网页内容
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找所有图片标签
            img_tags = soup.find_all('img')

            # 下载并保存图片
            for img in img_tags:
                img_url = img.get('src')
                if img_url:
                    # 获取图片的完整URL
                    img_url = img_url if img_url.startswith('http') else 'https://desk.3gbizhi.com' + img_url
                    download_image(img_url)

            print(f'已完成爬取: {url}')
        except requests.exceptions.RequestException as e:
            print(f'请求失败: {e}')

if __name__ == '__main__':
    main()
