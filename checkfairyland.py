# ！/usr/bin/python
# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice  
device=MonkeyRunner.waitForConnection()
if not device:
	print('Please connect a device to start!')
else:
	print("Start")
	for i in range(1,50):
		comand="com.tencent.qqlivekid/.activity.WelcomeActivity"
		device.startActivity(component=comand)
		MonkeyRunner.sleep(15)
		print('touch video')
		device.touch(517,618,'DOWN_AND_UP')
		device.touch(517,618,'DOWN_AND_UP')
		print('video checked')
		MonkeyRunner.sleep(10)
		print('reboot')
		print(i)
		MonkeyRunner.sleep(2)
		device.reboot()
		MonkeyRunner.sleep(50)

