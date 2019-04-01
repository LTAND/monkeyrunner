# 导入模块
# 获取设备
# 开始截图
# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()
device.takeSnapshot().writeToFile('D://img/0001.png','png')