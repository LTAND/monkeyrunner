# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

comand = 'com.android.dialer/.DialtactsActivity'
device.startActivity(component=comand)
device.drag((339,357),(1075,357),0.1,10)

# 向下滑动极限
# for i in range(1,30): 
#     device.drag((180,180),(600,600),0.1,10)
#     MonkeyRunner.sleep(2)
#     print('dragUp:',i)

# 向下滑动极限
# for i in range(1,1001): 
#     device.drag((400,400),(180,180),0.1,10)
#     MonkeyRunner.sleep(1)
#     device.drag((180,180),(600,600),0.1,10)
#     MonkeyRunner.sleep(1)
#     print('drag:',i)    

# 向上滑动极限
# for i in range(1,1001): 
#     device.drag((400,400),(180,180),0.1,10)
#     MonkeyRunner.sleep(1)
#     print('dragUp:',i) 

# for i in range(1,3):
#     MonkeyRunner.sleep(10)
#     device.touch(456,1605,'DOWN_AND_UP')
#     print(i)
#     MonkeyRunner.sleep(5)
#     device.reboot()

# device.touch(100, 400, MonkeyDevice.DOWN) 
# device.touch(339, 1075, MonkeyDevice.MOVE)
# device.touch(88, 656, MonkeyDevice.UP) 
