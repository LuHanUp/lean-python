def fun():
    return [1, 2, 3], [4, 4, 5, 6]


print(fun())

'''
函数的定义：
语法结构：def 函数名称(形式参数...):
            代码块
            [return]
            
函数的形式参数：
1. 如果需要定义默认值,直接使用=赋值即可:def fun(a,b=10)
2. 如果不确定参数的个数使用*定义:def fun(*args)
    这个不确定个数的参数类型为元组
3. 参数不确定的关键字参数使用**定义:def fun(**args)
    这个关键字参数的类型为字典
4. 如果需要可变参数的只能有1个,那么在函数体中用pass来定义:
def fun(*a,*b):  # 这里会报错，因为可变的位置参数只能有1个
    pass
5. 在一个函数的定义过程中，可变的关键词形参需要放在位置参数的后面
def fun(**args,*args2): # 会报错,因为关键字参数需要放在位置参数后面
6. 如果参数放在了*之后,在调用函数时，只能采用关键字参数传递
def fun(a,b,*,c,d):
fun(10,20,30,40) # 会报错，因为30，40是位置参数，而不是关键字参数，因为函数定义时c,d这两个参数只能使用关键词参数传递
fun(10,20,c=30,d=40) # c,d作为关键字参数传递是正确的

函数变量的作用域：
1. 定义在函数参数的变量作用域为函数内部，相当于局部变量
2. 在函数体中定义的变量就是局部变量，只能在函数体中使用
3. 如果局部变量被global修饰了，那么这个变量就变成了全局变量

函数的返回值
1. 如果函数没有返回值 return可以省略不写
2. 函数的返回值，如果是1个，直接返回类型
3. 函数的返回值，如果是多个，返回的类型是元组

'''


def fun(a, b, c):
    print(f"a={a},b={b},c={c}")


fun(**{"a": 100, "b": 200, "c": 300})  # 将字典作为关键字参数传入函数中,使用**
