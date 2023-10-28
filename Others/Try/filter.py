import re
from tools import get_json_data

rawNodes = get_json_data('nodes.json')
filtered_texts = [] 
pattern = re.compile(r'[\u4e00-\u9fff]+')
pattern_exclude = re.compile(r'美国')

# if pattern.search(text) and not pattern_exclude.search(text):
for i in rawNodes:
#   if pattern.search(i['ps']) and pattern_exclude.search(i['ps']):
  if '美国' in i['ps']:
    filtered_texts.append(i)
# for k in filtered_texts:
  
print(filtered_texts)

# result = [s for s in rawNodes if re.match(r'^[美国][\w-]+$', s['ps'])]

# 输出结果
# print(result)