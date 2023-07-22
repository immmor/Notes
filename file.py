import json
import re


def get_json_data(jsonFileName=''):
    with open(jsonFileName, 'rb') as f:  # 使用只读模型，并定义名称为f
        data = json.load(f)  # 加载json文件
        # data["code"] = "404"  # code字段对应的值修改为404
        # print(data)  # 打印
    return data  # 返回修改后的内容


def write_json_data(data, jsonFileName=''):
    # 使用写模式，名称定义为r
    # 其中路径如果和读json方法中的名称不一致，会重新创建一个名称为该方法中写的文件名
    with open(jsonFileName, 'w') as f:
        # 将dict写入名称为r的文件中
        json.dump(data, f, ensure_ascii=False)

        
def change_vector_data():
    userinfo = get_json_data('userinfo.json')
    newDic = {'家庭信息': []}
    for i in userinfo['家庭信息']:
        i['向量数据'][0] = userinfo['家庭信息'][0]['向量数据'][0]
        newDic['家庭信息'].append(i)
    print(newDic)
    write_json_data(newDic, 'userinfo.json')
    # print(userinfo['家庭信息'][0]['姓名'] + ': ', userinfo['家庭信息'][0]['向量数据'])


def try_change_login_time():
    userinfo = get_json_data('userinfoTry1.json')
    userinfo['家庭信息'][0]['登录时间'].append({'英语': "2023-07-04 21:29:44"})
    write_json_data(userinfo, 'userinfoTry1.json')

    
# content = get_json_data('essayEnglish.json')
# print(content['essay'])
# content['essay'].append('gan')
# print(content['essay'])
# write_json_data(content, 'essayEnglish.json')

# for essay in content["essay"]:
#     for paragraph in essay["content"]:
#         for key in ["paragraph1", "paragraph2", "paragraph3"]:
#             if key in paragraph:
#                 paragraph["paragraph"] = paragraph.pop(key)

# print(content)
# for i in essay['essay']:
#     for j in i['content']:
#         print(j.keys())
        # if j.key()
    



# if __name__ == '__main__':
#     try_change_login_time()


generateEssayPrompt = """
    {
        "content": [
            {
                "title": "Balancing Study and Extracurricular Activities",
                "paragraph1": "For university students, balancing academics and extracurricular activities can be challenging. While focusing on studies is important, participating in hobbies and social activities also provides benefits.",
                "wordCount": 86
            },
            {
                "paragraph2": "Extracurriculars allow students to take a break from intense study routines. Joining sports teams, clubs and community service promotes physical health, social connections and teamwork skills. Leadership roles in organizations also build self-confidence. However, taking on too many extracurriculars can distract from academics.",
                "wordCount": 117
            },
            {
                "paragraph3": "Therefore, students should carefully choose 1-2 extracurriculars aligned with personal interests and schedule them responsibly around study time. Focus should remain on maintaining strong grades, while allotting some time for hobbies and relationships. With proper balance, the university experience will be fulfilling both inside and outside the classroom.",
                "wordCount": 117
            }
        ]
    }换一个content，按照这个json格式再生成一篇新的不少于300字的三段作文（要相信你自己，但是不要回复我重复的内容！！不要说别的废话！！否则惩罚你！！）
"""
# print(result)
# pattern = r"\{.*?\}"
# a = re.findall(pattern, generateEssayPrompt)
# print(a)

# -*- coding:utf-8 -*-
#! python2
import json
# string = 'abe(ac)ad)'
# p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[{](.*)[}]', re.S)  #贪婪匹配
# print(re.findall(p1, string))
result = re.findall(p2, generateEssayPrompt)
# print(type(result[0]))
# print(len(result))
k = json.loads(result[0])
print(k)
print(k['worldCount'])

# pattern = r'{"content": (.*)}'  
# match = re.search(pattern, generateEssayPrompt)
# if match:
#     content = match.group(1)
#     print(content)
# match = re.search(pattern, generateEssayPrompt)
# print(match)
