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
