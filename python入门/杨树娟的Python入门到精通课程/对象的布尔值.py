# Python中的对象都会内置一个bool类型的值 使用bool进行获取
# 只要是空、0、False这些对象里的布尔值都为False
print(bool(0))  # 数字0对象里的bool是False
print(bool(None))  # None对象里的bool是False
print(bool([]))  # 空数组对象里的bool是False
print(bool({}))  # 空字典对象里的bool是False
print(bool(''))  # 空字符串里bool是False
print(bool(False))  # False对象里的bool是False
print(bool(1))
print(bool('hello world'))
print(bool([0, 1, 2]))
print(bool({"name": "hello world"}))
print(bool(True))
