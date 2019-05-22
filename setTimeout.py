# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()
if(device):
  print("device start")
  for i in range(1,21):
    print(i)
    device.reboot()
    MonkeyRunner.sleep(80)
else:
  print("device fail")