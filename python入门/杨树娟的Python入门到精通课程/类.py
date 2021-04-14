# 定义一个Class
class Student:
    native_place = "湖北"

    def __init__(self, name, age):  # 这是初始化方法,相当于Java中的构造方法
        self.name = name
        # self.age = age
        self.__age = age  # 如果不希望age属性被外界访问,可以在属性前面添加两个_ ps:其实在类的外部也是可以访问的,使用_类名__属性名 就可以访问

    # 定义类实例方法
    def instance_method(self):  # self就相当于Java中的this
        print("调用了Student类的实例方法instance_method", self.name)

    @staticmethod
    def static_method():
        print("调用了Student类的静态方法static_method")

    @classmethod
    def class_method(cls):
        print("调用了Student类的类方法class_method")

    def __str__(self) -> str:
        return super().__str__()


# 创建类的实例对象,在创建的对象中有一个'类指针'指向了对象对对应的Class
stu = Student("张三", 20)

# 调用类的实例方法
stu.instance_method()

# 调用类方法
Student.class_method()

# 调用静态方法
Student.static_method()

# 在类的外部访问私有属性
# print(stu._Student__age)  # 在类的外部使用 _类名__属性名 访问私有属性,但是不建议私有属性使用这样的方式进行访问

'''
类的继承: 
1. 如果一个类没有继承任何类,则默认继承object
2. Python支持多继承,使用(父类1,父类2...)表示继承
    class Person:
        pass
    class Student(Person): # 表示Student继承了Person类
        pass
3. 子类重写父类方法后可以通过super().xxx()调用父类的方法
4. 获取类的父类类型:
    类名.__bases__ # 返回的是父类类型的元组
    类名.__base__ # 返回的是离的最近的父类
5. 获取类的结构:
    类名.__mro__
6. 获取类的子类:
    类名.__subclasses__() # 返回的所有的子类的列表
7. 类的特殊方法:
    __add__:可以使得两个对象可以进行加法运算,两个int对象的相加的原理就是这个
    __len__:可以返回这个对象的长度
    __new__:用于创建对象,在__init__方法前面执行
    __init__:用于初始化对象,其中self参数就是__new__创建出来的对象
8. 类的特殊属性:__dict__ # 返回这个实例对象所绑定的所有属性和方法的字典
'''
