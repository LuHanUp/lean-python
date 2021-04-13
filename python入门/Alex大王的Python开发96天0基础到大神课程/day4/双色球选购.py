red_balls = []  # 存储选中的红色球
blue_balls = []  # 存储选中的蓝色球

# 双色球的选购规则 [][0]:表示选购球的个数 [][1]:表示选购球最大的数上限 [][2]:表示当前选购球的颜色 [][3]:表示将当前选购的数添加到一个对应的列表中
rules = [[6, 33, "红球", red_balls],
         [1, 16, "蓝球", blue_balls]]

for item in rules:
    print(f"开始选购{item[2]}".center(50, "-"))
    count = 0
    while count < item[0]:
        choice = input(f"输入第{count + 1}个{item[2]}>:").strip()
        if not choice.isdigit():
            print("不合法，请重新输入")
            continue
        choice = int(choice)
        if 0 < choice <= item[1] and choice not in item[3]:
            item[3].append(choice)
            count += 1
print(red_balls, blue_balls)