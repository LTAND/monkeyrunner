# -*- coding: UTF-8 -*-
import random
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection()

def play_video():
  # 需要停留某个故事里的页面，执行这个方法
  MonkeyRunner.sleep(2)
  device.touch(253, 386, "DOWN_AND_UP") # 点击故事
  MonkeyRunner.sleep(2)
  device.touch(1167, 645, "DOWN_AND_UP") # 点击全屏 
  MonkeyRunner.sleep(20)                 # 播放时长
  device.touch(50, 52, "DOWN_AND_UP") # 打开菜单 
  device.touch(50, 52, "DOWN_AND_UP") # 退出视频 
  return True

if device:
  print("start")

  for i in range(1,101):
    print("play_video %d" % i)
    play_video()
