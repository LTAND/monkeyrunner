# -*- coding: UTF-8 -*-
import random
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection()

# 点击
if(device):
  print("start")
  device.touch(113, 409, "DOWN_AND_UP")
  