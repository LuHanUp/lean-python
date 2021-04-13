# 列表生成式：格式为：[列表元素表达式 for 元素变量 in 可迭代对象]

# 列表是可变的，可重复，有序的序列

li = [i for i in range(10)]
print(li)
li = [i * i for i in range(10)]  # 其中i*i就是元素表达式 就是将每个i都翻一倍
print(li)
