# 教我用asyncio写代码
import asyncio
import time # 导入时间模块
import random
async def get_html(url):
    print('正在爬取%s'%url)
    await asyncio.sleep(random.randint(1,3)) # 模拟网络延迟
    return url