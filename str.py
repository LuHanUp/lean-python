# 字符串 在Python中只要是加了引号(无论是'' or "" or """""" or '''''')的都被认为是字符串

# 字符串特性：不可修改、有索引，可切片

# 定义一个字符串:变量名 = 字符串值
name = "BlackGirl"

# 字符串不可修改演示
# name = "aaaa"
# id(name)  #
# name = "bbbb"
# id(name)
# 两次id显示的内存地址是不一致的
# name[2] = '2'  # 'str' object does not support item assignment  不可以对str中的指定索引进行修改

# 字符串切片
print(name[2])
print(name[2:4])  # 取值范围是[2,4)

# 字符串拼接
appendName = "这是一个字符串" + "这是另一个字符串"
print(appendName)

# 多行字符串
msg = '''
hello 
my name is Alex,this big king.
good ad python.and making money
adn cheaseing.....girl
'''
print(msg)

# 字符串内引用外部变量
name = "Alex"
age = 30
hobbie = 'girl'

desc = '''
----------%s info----------------
name: %s
age: %d
hobbie: %s
----------end--------------------
''' % (name, name, age, hobbie)  # 这是早期python2.x的用法
print(desc)

# %s 表示引入字符串类型的变量
# %d 表示引入整型类型的变量
# %f 表示引入float类型的变量

name = "Alex"
age = 30
hobbie = 'girl'

desc = f'''
----------{name} info----------------
name: {name}
age: {age}
hobbie: {hobbie}
----------end--------------------
'''  # 这是python3.x的用法，在字符串的开头加一个f标识
print(desc)
