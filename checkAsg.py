# ！/usr/bin/python
# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice  
device=MonkeyRunner.waitForConnection()
if not device:
	print('Please connect a device to start!')
else:
	print("Start")
	for i in range(1,50):
		comand="com.handict.superapp_business_senior_next/com.handict.superapp_business_senior_next.UnityPlayerActivity"
		device.startActivity(component=comand)
		MonkeyRunner.sleep(10)
		print('touch open video')
		device.touch(642,411,'DOWN_AND_UP')
		device.touch(642,411,'DOWN_AND_UP')
		print('video going')
		MonkeyRunner.sleep(66)
		print('reboot')
		print(i)
		MonkeyRunner.sleep(2)
		device.reboot()
		MonkeyRunner.sleep(50)

