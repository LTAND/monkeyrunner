# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
devices = MonkeyRunner.waitForConnection()

if not devices:
    print('devices is not connected')
else:
    print('start')
    comand="com.hy.HoneyMarket/com.hy.HoneyMarket.processView.view.activity.RecyclerViewPagerActivity"
    devices.startActivity(component=comand)
    MonkeyRunner.sleep(4)
    
    # 点击 故事机下载
    devices.touch(520,250,'DOWN_AND_UP')
    print('1.download')
    # 点击 爱奇艺巴布下载
    devices.touch(1127,250,'DOWN_AND_UP')
    print('2.download')
    # 点击 蛋生园下载
    devices.touch(520,480,'DOWN_AND_UP')
    print('3.download')
    # 点击 学画画下载
    devices.touch(1127,480,'DOWN_AND_UP')
    print('4.download')
    
    # 点击下载任务列表按钮
    MonkeyRunner.sleep(2)
    devices.touch(1183,660,'DOWN_AND_UP')
    # devices.takeSnapshot().writeToFile('D://1.png','png')

    # 删除下载任务
    MonkeyRunner.sleep(4)
    for i in range(1,5):
        devices.touch(1127,278,'DOWN_AND_UP')
        MonkeyRunner.sleep(2)
    # devices.takeSnapshot().writeToFile('D://2.png','png')

    # 退出 应用市场
    MonkeyRunner.sleep(5)
    (devices.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP))*2