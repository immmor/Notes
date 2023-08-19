import os
import platform

# def system_link(link):
#     if link.count('/') > 1 and (platform.system() == 'Linux' or 'Darwin'):
#         return link
#     elif link.count('/') > 1 and platform.system() == 'Windows':
#         return link.replace('/', '\\')
#     elif link.count('\\') > 1 and (platform.system() == 'Linux' or 'Darwin'):
#         return link.replace('\\', '/')
#     elif link.count('\\') > 1 and platform.system() == 'Windows':
#         return link

# \\n1920301a016.bmwgroup.net\brian_e19_cn\DTSV_China_C\G048\9D27145\20230816_1445

winFilePath = r'C:\Users\QXZ3PSW\Desktop\brian_e19_cn\DTSV_China_C\G048\\9D27145\20230818_0915\\9D27145_20230818_0915_CheckIn.txt'
# brian\[car, rack]\PU\长VIN后7位\时间戳\[checkin.txt, checkout.txt]
macFilePath = '/Users/mrok/Documents/coder/funtext/Python/Data Analysis/brian_e19_cn/'
# 打印当前目录所有文件夹的名字
# fileInBrian = os.listdir(macFilePath)
# fileInDRSVCar = os.listdir(macFilePath + fileInBrian[0])
# fileInG068 = fileInDRSVCar[0]
# print(fileInDRSVCar)
CARG0489D27145 = []
allTXTFiles = []
for carOrRack in os.listdir(macFilePath):
    # print(carOrRack)
    if os.path.isdir(macFilePath + carOrRack):
        for series in os.listdir(macFilePath + carOrRack):
            # print(series)
            if os.path.isdir(macFilePath + carOrRack + '/' + series):
                for vin in os.listdir(macFilePath + carOrRack + '/' + series):
                    # print(vin)
                    if os.path.isdir(macFilePath + carOrRack + '/' + series + '/' + vin):
                        for timestamp in os.listdir(macFilePath + carOrRack + '/' + series + '/' + vin):
                            # print(timestamp)
                            if os.path.isdir(macFilePath + carOrRack + '/' + series + '/' + vin + '/' + timestamp):
                                for file in os.listdir(macFilePath + carOrRack + '/' + series + '/' + vin + '/' + timestamp):
                                    # 如果文件以.txt结尾
                                    if file.endswith('.txt'):
                                        # print(file)
                                        allTXTFiles.append(file)

print(allTXTFiles)

