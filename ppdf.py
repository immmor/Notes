import json, os
from tools import claudeAI, get_json_data, write_json_data

prompt = """
直接用python创建一个bb.txt文件，不要说别的，直接给我代码。
"""
rawData = claudeAI(prompt)
# pattern = re.compile(r'[{](.*)[}]', re.S)  #贪婪匹配
# afterREResult = re.findall(pattern, result)
k = rawData.strip()
print(k)
result = k.strip('"')
# jsonResult = json.loads(result)
# print(jsonResult)

# content = get_json_data('essayEnglish.json')
# content['essay'].append(jsonResult)
# print(content['essay'])
write_json_data(result, 'hh.txt')
# cmd = os.system('python hh.py')
# print(cmd)