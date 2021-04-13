girl_age = 25
count = 0
while count < 3:
    age = int(input("猜姑娘的年龄>:"))
    if age > girl_age:
        print("猜大了，往小了试试...")
    elif age < girl_age:
        print("猜小了，往大了试试...")
    else:
        print("猜对了....")
        break
    count += 1
    if count == 3:
        cmd = input("你这么笨，是否需要再试一把？(y/n)").strip()
        if cmd in ["Y", "y", "yes"]:
            count = 0
        else:
            print("程序结束")
