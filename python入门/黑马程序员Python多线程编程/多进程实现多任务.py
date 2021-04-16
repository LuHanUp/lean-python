'''
1. 先导入进程包
2. 使用进程类创建进程对象
3. 使用进程对象启动进程执行指定任务
'''

import multiprocessing  # 1.导入进程包
import time
import os


def sing(num):
    print("唱歌进程的pid:{0}".format(os.getpid()))
    for i in range(num):
        print("唱歌...")
        time.sleep(0.6)


def dance(num):
    print("跳舞的进程pid:{0}".format(os.getpid()))
    for i in range(num):
        print("跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':
    print("主进程pid:{0}".format(os.getpid()))
    # 2.使用进程类创建进程对象
    # 2.1 args:使用元组的方式给任务传递参数.ps:元组的方式中,参数的位置要和任务的参数位置要一样
    # 2.2 kwargs:使用字典的方式给任务传递参数
    sing_process = multiprocessing.Process(target=sing, args=(6,))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 9})

    # 设置跳舞子进程为守护主进程,那么会在主进程结束的时候销毁跳舞子进程
    # dance_process.daemon = True

    # 3.使用进程对象启动任务
    sing_process.start()
    dance_process.start()

'''
进程的注意事项:
1. 默认情况下主进程会等待所有子进程执行结束再结束
    如果需要主进程结束所有子进程也结束:将子进程设置成守护主进程
        dance_process.daemon = True
'''
