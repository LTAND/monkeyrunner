# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

if not device:
    print('device is not connected')
else:
    print('start')
    comand="com.hy.robot.camera/com.hy.robot.camera.view.activity.SplashActivity"
    device.startActivity(component=comand)

    for i in range(1,31):
        MonkeyRunner.sleep(3)
        device.touch(1178,367,'DOWN_AND_UP') # 拍照按钮
        print('camera',i)
        device.reboot()
        MonkeyRunner.sleep(8)

        
    
