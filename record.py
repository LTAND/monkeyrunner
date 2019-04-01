#导入模块 以及给它别名
#连接设备
#录制开始
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner.recorder import MonkeyRecorder 
device = MonkeyRunner.waitForConnection()
MonkeyRecorder.start(device)

