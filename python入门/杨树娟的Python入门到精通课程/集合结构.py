# 集合的定义使用{}来表示，集合set是没有value的字典结构 集合是可变的，不可重复的，无序的序列

"""集合的创建操作"""
s = {10, 20, 30, 40}
print(s, type(s))

s = set({10, 20, 30, 40, 50, 60})
print(s, type(s))

s = set([10, 20, 30, 40, 50, 60, 70])
print(s, type(s))

s = set((10, 20, 30, 40, 50))
print(s, type(s))

'''集合的添加操作'''
s.add(100)
print(s, type(s))

s.update([200, 30, 50, 600])
print(s, type(s))

s.update((1, 2, 3, 4, 5, 6, 7))
print(s, type(s))

s.update({45, 68, 2164, 876, 15, 64, 1, 31, 6})
print(s, type(s))

'''集合的删除操作'''
# s.remove(1000)  # remove方法，如果要删除的元素不存在，那么就会抛出异常 KeyError: 1000
s.discard(2164)  # discard方法，如果要删除的元素不存在，不会抛出异常
print(s, type(s))

s.pop()  # 移除set的第一个元素，因为set是无序的，所以第一个元素也是不确定的，所以可以说是随机删除一个元素
print(s, type(s))

# s.clear()  # 清空集合

'''集合之间的操作'''
s = {10, 20, 30, 40}
s2 = {10, 20, 30}
s3 = {20, 40, 60}
s4 = {30, 40, 20, 10}
print(f"s:{s}")
print(f"s2:{s2}")
print(f"s3:{s3}")
print(f"s3:{s4}")

print(f"s4和s相等吗:{s4 == s}")

print(f"s2是s的子集吗:{s2.issubset(s)}")
print(f"s3是s的子集吗:{s3.issubset(s)}")

print(f"s是s2的超集吗:{s.issuperset(s2)}")
print(f"s是s3的超集吗:{s.issuperset(s3)}")

print(f"s2和s3之间没有交集吗:{s2.isdisjoint(s3)}")
print(f"s和s2之间没有交集吗:{s.isdisjoint(s2)}")

'''集合之间的数学操作'''
print(f"s和s2之间的交集是:{s.intersection(s2)}")
print(f"s和s2之间的并集是:{s.union(s2)} == {s | s2}")  # 并集操作union 等价于 |
print(f"s和s2之间的差集是:{s.difference(s2)} == {s - s2}")  # 差集操作difference 等价于 -
print(f"s和s3之间的对称差集是:{s.symmetric_difference(s3)} == {s ^ s3}")  # 对称差集操作symmetric_difference 等价于 ^

'''集合生成式
    格式为：{元素表达式 for 元素遍历 in 可迭代对象}
'''
s = {i * i for i in range(10)}
print(s, type(s))
