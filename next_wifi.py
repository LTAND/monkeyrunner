# -*- coding: UTF-8 -*-
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
devices = MonkeyRunner.waitForConnection()
devices.startActivity(component="com.huiyu.honeyrobot.car/.view.activity.OptionsWifiActivity")

def doNext():
  os.popen('adb shell am start com.huiyu.honeyrobot.car/.view.activity.OptionsWifiActivity')
  MonkeyRunner.sleep(3)
  os.popen('adb shell am force-stop com.huiyu.honeyrobot.car')
  MonkeyRunner.sleep(5)
  devices.touch(1160, 70, "DOWN_AND_UP")
  return True

if not devices:
  print('devices is not connected')
else:
  print('start')
  for i in range(1, 6):
    if(doNext() == True):
      print(i, "Finsh")