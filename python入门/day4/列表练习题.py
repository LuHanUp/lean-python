# 去除列表中重复的元素
li = [5, 4, 1, 5, 45, 23, 4, 68, 4, 6, 4, 6, 2, 1, 3, 1, 5, 58, 1, 2, 15, 124, 62, 51, 1, 5, 45, 5, 4, 54, 1, 5, 1]
duplicate_nums = []
for i in li:
    i_show_count = li.count(i)
    if i_show_count > 1:
        if [i, i_show_count] not in duplicate_nums:
            duplicate_nums.append([i, i_show_count])
        for j in range(i_show_count - 1):
            li.remove(i)
li.sort()
print("存储重复的列表:", duplicate_nums)
print(li)

# 找到列表中第二大的值 不能使用sort
li = [5, 4, 1, 5, 45, 23, 4, 68, 4, 6, 4, 6, 2, 1, 3, 1, 5, 58, 1, 2, 15, 124, 62, 51, 1, 5, 45, 5, 4, 54, 1, 5, 1]
for n in range(2):
    for index in range(len(li) - 1):
        i = li[index]  # 拿到当前索引对应的值 5
        if i > li[index + 1]:  # 表示5>4 要进行交换
            li[index] = li[index + 1]  # 将4换到5的位置上
            li[index + 1] = i  # 把临时存的5放到4的位置上
print(li)
print("第二大的值为:", li[len(li) - 2])

# 判断一个列表是否是另一个列表的子列表
li = [5, 4, 1, 5, 45, 23, 4, 68, 4, 6, 4, 6, 2, 1, 3, 1, 5, 58, 1, 2, 15, 124, 62, 51, 1, 5, 45, 5, 4, 54, 1, 5, 1]
l2 = [4, 68, 4]
