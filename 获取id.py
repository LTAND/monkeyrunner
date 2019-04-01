# -*- coding: UTF-8 -*-

# 打开C:\Users\win 10\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat
# 或有设置环境变量的代开cmd,输入uiautomatorviewer

# 获取当前屏幕控件id,再运行脚本
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice,By
device = MonkeyRunner.waitForConnection()

if not device:
    print('devices is not connected')
else:
    print('start')
    comand="com.hy.storyMachine/.view.activity.HomeActivity"
    device.startActivity(component=comand)
    easy_device = EasyMonkeyDevice(device)  
    MonkeyRunner.sleep(10)
    easy_device.touch(By.id('id/img_pause_play'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)
    easy_device.touch(By.id('id/img_last'), MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)
    easy_device.touch(By.id('id/img_next'), MonkeyDevice.DOWN_AND_UP)
    # 点击左下角的按钮
    MonkeyRunner.sleep(5)
    easy_device.touch(By.id('id/img_album'), MonkeyDevice.DOWN_AND_UP)
    