'''
1. 先导入进程包
2. 使用进程类创建进程对象
3. 使用进程对象启动进程执行指定任务
'''

import multiprocessing  # 1.导入进程包
import time


def sing(num):
    for i in range(num):
        print("唱歌...")
        time.sleep(0.6)


def dance(num):
    for i in range(num):
        print("跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.使用进程类创建进程对象
    # 2.1 args:使用元组的方式给任务传递参数.ps:元组的方式中,参数的位置要和任务的参数位置要一样
    # 2.2 kwargs:使用字典的方式给任务传递参数
    sing_process = multiprocessing.Process(target=sing, args=(6,))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 9})

    # 3.使用进程对象启动任务
    sing_process.start()
    dance_process.start()
