import json


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

    
k = {'poli': ['a', 'b'], 'ai': ['a', ''], 'eng': []}
k['poli']



# if __name__ == '__main__':
#     try_change_login_time()
