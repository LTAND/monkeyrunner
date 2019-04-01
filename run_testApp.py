# -*- coding: UTF-8 -*-
# 进入testapp
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
device = MonkeyRunner.waitForConnection()

# device.startActivity(component='com.android.functiontest/.ui.MainActivity')
# 在wifi页面触发特殊按钮
for i in range(0,10):
  device.touch(116, 315, 'DOWN_AND_UP')