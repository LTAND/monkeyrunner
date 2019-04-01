import os

abspath = os.getcwd()  # 获取当前路径
rootpath = os.path.abspath('..')  # 获取上级路径
print(abspath)
print(rootpath)


# 文件夹不存在，则创建文件夹
path = 'D:\\test_image'  
if not os.path.isdir(path):  
    os.makedirs(path)


# adb 获取屏幕分辨率
# adb shell wm size
# out = os.popen('adb shell wm size').read()
# print(out)