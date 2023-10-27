from concurrent.futures import ThreadPoolExecutor
from Web.Notes.tools import claude_ai

def execute_code(code):
    result = claude_ai(code)
    return result

# 定义要执行的代码列表
code_list = [
    '1+1等于几',
    '3+1等于几',
    '2+1等于几',
    '1+5等于几'
]

# 创建线程池
with ThreadPoolExecutor() as executor:
    # 提交任务给线程池并获取Future对象
    futures = [executor.submit(execute_code, code) for code in code_list]

    # 获取并打印执行结果
    for future in futures:
        result = future.result()
        print(result)