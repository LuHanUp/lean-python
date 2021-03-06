# 字符串的驻留机制：仅保留一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，Python的驻留机制对相同的字符串只保留一份拷贝
# 后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
s1 = 'Python'
s2 = "Python"
s3 = """Python"""
print(s1 is s2, id(s1), id(s2))
print(s2 is s3, id(s2), id(s3))
# 实际上s1和s2和s3指向同一份内存地址，这个内存地址保存的就是Python这个字符串，这就是字符串的驻留机制
# 驻留机制的几种情况(交互模式)
'''
1. 字符串的长度为0或者1
2. 符合标识符的字符串
    标识符：字母/数字/_ 组合的字符串即为标识符字符串
3. 字符串在编译时进行驻留，而非运行时：
    s1 = 'abc',s2 = 'ab' + 'c',s3 = "".join(['ab','c'])
    其中s1 is s2 返回True，而s1 is s3 返回False  因为join方法会在运行时重新创建一个对象
    说明：这代码在PyCharm中都是返回True的，因为PyCharm会对字符串进行优化
4. [-5,256]之间的整数数字
'''
# sys中的intern方法会强制2个字符串指向同一个内存地址
'''
import sys
s1 = 'abc%'
s2 = 'abc%'
s1 is s2 False
s1 = sys.intern(s2)
s1 is s2 True
'''

'''字符串判断方法
1. isidentifier()：指定的字符串是否是合法的标识符
2. isspace()：指定的字符串四否全部由空白字符组成
    空白字符：回车、换行、水平制表符、空格
3. isalpha()：判断指定字符串是否全由字母组成
4. isdecimal()：指定字符串是否全由十进制的数字组成
5. isnumeric()：指定的字符串是否全由数字组成
6. isalnum()：指定字符串是否全由字母+数字组成
'''

'''格式化字符串
格式化字符串有两种方式：
1. %做占位符
    %s:表示字符串占位
    %d：表示整数占位
        %10d:其中的10表示的是字符的宽度
    %f：表示浮点占位
        %.3f:.3表示保留小数点后3位
    示例：'我的名字叫做%s，今年%d岁了，很高兴遇到你们' % ('张三',21)
2. {}做占位符,{}里也可以使用宽度({0:10d})和精度({0:0.3f})
    示例：'我的名字叫做{0},今年{1}岁了，我的真的叫{0}'.format(name,age) # 其中的0 1表示占位的索引
'''
