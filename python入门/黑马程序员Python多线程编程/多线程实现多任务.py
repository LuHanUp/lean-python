'''
1. 先导入线程模块
2. 使用线程类创建线程对象
3. 使用线程对象启动线程执行指定任务
'''

import threading  # 1.导入线程模块
import time
import os


def sing(num):
    for i in range(num):
        print("唱歌...")
        time.sleep(0.6)


def dance(num):
    for i in range(num):
        print("跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.使用线程类创建线程对象
    # 2.1 args:使用元组的方式给任务传递参数.ps:元组的方式中,参数的位置要和任务的参数位置要一样
    # 2.2 kwargs:使用字典的方式给任务传递参数
    # 2.3 daemon:设置是否守护主线程
    # sing_thread = threading.Thread(target=sing, args=(6,), daemon=True)
    sing_thread = threading.Thread(target=sing, args=(6,))
    dance_thread = threading.Thread(target=dance, kwargs={"num": 9})

    # 设置跳舞子线程为守护主线程,那么会在主线程结束的时候销毁跳舞子线程
    # dance_thread.setDaemon(True)

    # 3.使用线程对象启动任务
    sing_thread.start()
    dance_thread.start()

'''
线程的注意事项:
1. 默认情况下主线程会等待所有子线程执行结束再结束
    如果需要主线程结束所有子线程也结束:将子线程设置成守护主线程
        dance_thread.setDaemon(True)
'''
