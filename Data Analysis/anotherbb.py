# import os

# macFilePath = '/Users/mrok/Documents/coder/funtext/Python/Data Analysis/brian_e19_cn/'

# allTXTFiles = [file for carOrRack in os.listdir(macFilePath)
#                if os.path.isdir(os.path.join(macFilePath, carOrRack))
#                for series in os.listdir(os.path.join(macFilePath, carOrRack))
#                if os.path.isdir(os.path.join(macFilePath, carOrRack, series))
#                for vin in os.listdir(os.path.join(macFilePath, carOrRack, series))
#                if os.path.isdir(os.path.join(macFilePath, carOrRack, series, vin))
#                for timestamp in os.listdir(os.path.join(macFilePath, carOrRack, series, vin))
#                if os.path.isdir(os.path.join(macFilePath, carOrRack, series, vin, timestamp))
#                for file in os.listdir(os.path.join(macFilePath, carOrRack, series, vin, timestamp))
#                if os.path.splitext(file)[1] == '.txt']

# print(allTXTFiles)


# import os

# def get_all_txt_files(directory):
#     all_txt_files = []
#     for entry in os.scandir(directory):
#         if entry.is_dir():
#             all_txt_files.extend(get_all_txt_files(entry.path))
#         elif entry.is_file() and entry.name.endswith('.txt'):
#             all_txt_files.append(entry.path)
#     return all_txt_files

# macFilePath = '/Users/mrok/Documents/coder/funtext/Python/Data Analysis/brian_e19_cn/'
# allTXTFiles = get_all_txt_files(macFilePath)
# print(allTXTFiles)


# import json
# import os
# # def system_link(link):
# #     if link.count('/') > 1 and (platform.system() == 'Linux' or 'Darwin'):
# #         return link
# #     elif link.count('/') > 1 and platform.system() == 'Windows':
# #         return link.replace('/', '\\')
# #     elif link.count('\\') > 1 and (platform.system() == 'Linux' or 'Darwin'):
# #         return link.replace('\\', '/')
# #     elif link.count('\\') > 1 and platform.system() == 'Windows':
# #         return link

# # \\n1920301a016.bmwgroup.net\brian_e19_cn\DTSV_China_C\G048\9D27145\20230816_1445

# def write_json_data(params, jsonFileName=''):
#     # 使用写模式，名称定义为r
#     # 其中路径如果和读json方法中的名称不一致，会重新创建一个名称为该方法中写的文件名
#     with open(jsonFileName, 'w', encoding='utf-8') as f:
#         # 将dict写入名称为r的文件中
#         json.dump(params, f, ensure_ascii=False)


# def directory_to_dict(directory):
#     result = {}
#     for entry in os.scandir(directory):
#         if entry.is_dir():
#             result[entry.name] = directory_to_dict(entry.path)
#         else:
#             result[entry.name] = entry.path
#     return result


# macFilePath = '/Users/mrok/Documents/coder/funtext/Python/Data Analysis/brian_e19_cn/'
# directory_dict = directory_to_dict(macFilePath)
# print(directory_dict)
# write_json_data(directory_dict, 'bb.json')




# import itertools
# import os
# from pprint import pprint


# def get_all_txt_files(directory):
#     all_txt_files = []
#     for entry in os.scandir(directory):
#         if entry.is_dir():
#             all_txt_files.extend(get_all_txt_files(entry.path))
#         elif entry.is_file() and entry.name.endswith('.txt'):
#             all_txt_files.append(entry.path)
#     return all_txt_files

# filePath = 'F:\\'
# allTXTFiles = get_all_txt_files(filePath)



# allTXTFiles = sorted(allTXTFiles, key=lambda x: (x.split('_')[-3], x.split('_')[-2]), reverse=True)

# pprint(allTXTFiles)
# print('asdfgh'[:-1])

# 按照 x.split('_')[-4] 分组
# allTXTFiles = sorted(allTXTFiles, key=lambda x: x.split('_')[-4])

# 对每个组内的文件按照 x.split('_')[-3] 和 x.split('_')[-2] 的倒序排序
# result = []
# for _, group in itertools.groupby(allTXTFiles, key=lambda x: x.split('_')[-4]):
#     sorted_group = sorted(group, key=lambda x: (x.split('_')[-3], x.split('_')[-2]), reverse=True)
#     result.extend(sorted_group)

# li = ['/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G048/9D27145/20230818_0915/9D27145_20230818_0915_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_R/G048/HY20900/20230818_1301/HY20900_20230818_1301_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_R/G048/HY20900/20230818_1313/HY20900_20230818_1313_CheckOut.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G068/S603606/20230818_1412/S603606_20230818_1412_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_R/G048/HY20900/20230814_1414/HY20900_20230814_1414_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G068/S603606/20230818_1426/S603606_20230818_1426_CheckOut.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G048/9D27145/20230816_1445/9D27145_20230816_1445_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_R/G068/HY07492/20230818_1513/HY07492_20230818_1513_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_R/G068/HY07492/20230818_1523/HY07492_20230818_1523_CheckOut.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G048/9D27145/20230816_1606/9D27145_20230816_1606_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G068/LH81514/20230817_1636/LH81514_20230817_1636_CheckOut.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G048/9D27145/20230814_1655/9D27145_20230814_1655_CheckIn.txt',
#  '/Users/mrok/Documents/coder/funtext/Python/Data '
#  'Analysis/brian_e19_cn/DTSV_China_C/G068/LH81514/20230817_1731/LH81514_20230817_1731_CheckIn.txt']
# pprint(result)

# sorted_li = sorted(allTXTFiles, key=lambda x: (x.split('\\')[-1].split('_')[-4], x.split('_')[-3], x.split('_')[-2]), reverse=True)
# pprint(sorted_li)
# pprint(allTXTFiles)



# import os
# import timeit

# # li = []
# def print_txt_files(directory=r'C:\\'):
#     for subdir, dirs, files in os.walk(directory):
#         for filename in files:
#             if filename.endswith('.txt'):
#                 print(os.path.join(subdir, filename))
#                 # li.append(os.path.join(subdir, filename))
# print(timeit.timeit(print_txt_files, number=1))
                

# # 打印C盘下的所有txt文件名
# print_txt_files('C:\\')
# print(li)


# import timeit
# from pathlib import Path
# def k():
#     for path in Path(r'C:\\').rglob('*.txt'):
#         print(path.as_posix())

# print(timeit.timeit(k, number=1))



import timeit
import os
def bb():
    os.system('dir /s /b C:\\*.txt > C:\\all_txt.txt')

print(timeit.timeit(bb, number=1))
