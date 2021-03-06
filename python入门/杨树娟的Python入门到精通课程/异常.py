# 异常/BUG

age = input("请输入你的年龄")
if age >= 18:
    print("你的年龄是:" + age)

'''
1. 语法错误:SyntaxError
    age=input("请输入你的年龄")
    if age >= 18 : # 这里就会抛出异常,因为age是str类型的,需要用int来转换一下
        # do something
2. 索引越界错误:IndexError
    list=[11,22,33,44]
    item=list[4] # 这里就会抛出索引越界异常,因为所以是从0开始的,而这个list只有4个元素,所以最大索引只能是3
3. 异常处理机制:其中BaseException是最大的异常类,相当于Java中的Exception
    语法:
        try:
            代码块
        except 异常类型:
            异常处理代码块
        except 异常类型2:
            异常处理代码块2
    打印异常信息:
        import traceback
        traceback.print_exc() # 打印异常信息
'''
