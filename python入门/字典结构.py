# 字典数据结构对应的就是Java中的Map
dist_obj = {"key": "value"}
print(dist_obj)

# 字典的创建方式

'''使用{}进行创建'''
sources = {"name": "张三", "age": 28}
print(sources)

'''使用dist()创建'''
sources = dict(name='张三', age=28)
print(sources)

print("获取字典中的元素".center(60, "-"))

'''方式一：使用[]进行获取，[]内填写key'''
print(sources['age'])
# print(sources['address']) # 如果使用不存在的key 那么就会抛出异常 KeyError: 'address'

'''方式二：使用get方法进行获取'''
print(sources.get("name"))
print(sources.get("address"))  # 使用get方法不会抛出异常 但是会返回一个None
print(sources.get("address", "这是key不存在时返回的默认值"))

print("删除字典中的元素".center(50, "-"))

'''删除指定的key-value键值对'''
del sources["name"]
print(sources)
# sources.clear()  # 清空字典，删除字典内的所有元素

print("修改字典内的数据".center(50, "-"))

'''使用update()进行修改'''
sources.update(name="修改后的张三")
print(sources)

'''使用[]进行修改'''
sources["age"] = 30  # 将age由原来的28修改为30
print(sources)

print("字段的获取相关操作".center(50, "-"))

print(sources.items())  # 返回字典内的所有元素以'元组'的方式进行返回
print(sources.values())  # 返回字典内所有的value
print(sources.keys())  # 返回字典内的所有的key
