# ！/usr/bin/python
# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice  
device=MonkeyRunner.waitForConnection()
if not device:
	print('Please connect a device to start!')
else:
	print("Start")
	for i in range(1,50):
		comand="com.hy.HoneyMarket/com.hy.HoneyMarket.processView.view.activity.RecyclerViewPagerActivity"
		device.startActivity(component=comand)
		MonkeyRunner.sleep(6)
		# device.touch(536,256,'DOWN_AND_UP')
		device.touch(1131,278,'DOWN_AND_UP')
		device.touch(530,513,'DOWN_AND_UP')
		device.touch(1124,505,'DOWN_AND_UP')
		MonkeyRunner.sleep(1)

		device.press("KEYCODE_BACK ",'DOWN_AND_UP')
		device.press("KEYCODE_BACK ",'DOWN_AND_UP')

		
		

		MonkeyRunner.sleep(2)
		print('Successful.Please Check')
		print(i)

# device.reboot()