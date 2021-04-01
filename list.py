# 列表的操作

# 声明一个列表变量
names = ["Monkey", "BlackGirl", "XiaoBin"]

# 往列表中添加一个元素
names.append("this is append element")
names.insert(2, "this is insert element")

print(names)

# 修改列表中某个位置的元素
names[3] = '哈哈哈哈'

# 获取指定元素在列表中的位置
print("哈哈哈哈在names中的索引为:", names.index("哈哈哈哈"))

# 删除列表中的元素
del names[3]
names.remove("this is insert element")

print(names)

# 切片和str的切片类似
print(names[-2])

print(names[0:2:1])  # 最后一个1表示为跳过的步长

# 嵌套
names.append(["XiaoMing", "XiaoLan"])
print(names[3])
print(names[3][0])
