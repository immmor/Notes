import requests
import json
from bs4 import BeautifulSoup

# 定义文章ID范围
start_id = 50000000
end_id = 50000005

# 设置请求的 URL 模板
url_template = "http://floor.huluxia.com/post/detail/ANDROID/4.2.2?platform=2&gkey=000000&app_version=4.3.1.3&versioncode=391&market_id=tool_web&_key=A990199D6A3E7A054B58B28ACCF5B9CDEF0FB80904E095BD3551A7E53BA09074B55417BF3773869C5FEDFB65395B3617B41B2CDBC065B2DF&device_code=%5Bd%5D8ee9cfe9-59bb-4b3f-a447-63199f767772&phone_brand_type=MI&hlx_imei=&hlx_android_id=a413cd40b1fa7502&hlx_oaid=96441e53487bde7b&post_id={}&page_no=1&page_size=20&doc=1"

# 设置请求头
headers = {
    "Connection": "close",
    "Host": "floor.huluxia.com",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.8.1"
}

# 循环遍历文章ID
for post_id in range(start_id, end_id + 1):
    try:
        # 格式化 URL
        url = url_template.format(post_id)

        # 发送 GET 请求，添加 headers
        response = requests.get(url, headers=headers)

        # 如果请求成功
        if response.status_code == 200:
            # 将响应内容解析为 JSON
            data = response.json()

            # 提取 "title" 和 "detail"
            post_info = data.get('post', {})  # Get the post object, default to empty dict if not found
            title = post_info.get('title', '无标题')
            detail_raw = post_info.get('detail', '无内容')

            # 提取分类信息
            category_info = post_info.get('category', {})  # 获取分类信息
            category_title = category_info.get('title', '无分类')

            # 打印文章信息
            print(f"文章ID: {post_id}")
            print(f"分类: {category_title}")
            print(f"标题: {title}")

            # 跳过标题为 "/* 话题已删除 */" 的文章
            if title == "/* 话题已删除 */":
                print(f"文章ID {post_id} 的标题为 '/* 话题已删除 */'，跳过。\n")
                continue

            # 只处理分类为 "技术分享" 的文章
            if category_title == "技术分享":
                # 使用 BeautifulSoup 清理 HTML 标签
                soup = BeautifulSoup(detail_raw, 'lxml')
                detail = soup.get_text(separator="\n").strip()  # 提取纯文本

                # 保存文章数据到文本文件
                extracted_data = {"title": title, "detail": detail}  # 创建字典

                # 将提取的数据保存到相应的文件
                with open(f"{post_id}.txt", "w", encoding="utf-8") as f:
                    f.write(json.dumps(extracted_data, ensure_ascii=False, indent=4) + "\n")  # 保存为格式化的 JSON 字符串

                print(f"文章ID {post_id} 提取完成，已保存到 {post_id}.txt\n")
            else:
                print(f"文章ID {post_id} 分类不是 '技术分享'，跳过。\n")

        else:
            print(f"错误: 状态码 {response.status_code}（文章ID: {post_id}）")

    except Exception as e:
        print(f"异常: {e}（文章ID: {post_id}）")

print("数据提取完成")