# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
device = MonkeyRunner.waitForConnection()

if not device:
  print('devices is not connected')
else:
  comand = 'com.iflytts.texttospeech/.ui.main.HomeActivity'
  device.startActivity(component=comand)
  MonkeyRunner.sleep(4)
  device.touch(339, 1214, 'DOWN_AND_UP')
  def do_play():
    device.touch(359, 1214, 'DOWN_AND_UP')
    MonkeyRunner.sleep(10)
    return
  do_play()
