# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner.recorder import MonkeyRecorder 
device = MonkeyRunner.waitForConnection()  # 连接设备
if device:
  print("device start")
  MonkeyRecorder.start(device)  # 录制开始

