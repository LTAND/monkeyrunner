# -*- coding: UTF-8 -*-
# 测试app的无限次划线操作
import random
import os
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

comand = 'com.android.functiontest/.ui.TPActivity'
device.startActivity(component=comand)

# adb 获取屏幕分辨率
# adb shell wm size
# out = os.popen('adb shell wm size').read()
# print(out)
toltalX = 1280
toltalY = 720

def getPotX():
  return random.randint(0,toltalX)
def getPotY():
  return random.randint(0,toltalY)

def doPlay():
  # print(getPotX(),getPotY())
  # print(getPotX(),getPotY())
  device.drag((getPotX(),getPotY()),(getPotX(),getPotY()),0.1,10)
  MonkeyRunner.sleep(1)
  return
    
def doMorePlay(len):
  for i in range(1,len+1):
    print("doPlay"+i)
    doPlay()
  return

# 只要在这方法添加参数 -- 滑动次数5
doMorePlay(5)
