# 作业1：猜年龄游戏某些程序实现以下结果
## 程序启动后让用户猜年龄
criticalValue = 25  # 预设定的正确的年龄

while True:
    age = int(input(">>:"))
    if age < criticalValue:
        print("猜的太小了，往大里试试...")
    elif age > criticalValue:
        print("猜的太大了，往小里试试...")
    else:
        print("恭喜你，猜对了")
        break
print("程序结束....")

# 作业2：写一段程序，读取用户输入的工资，根据工资多少打印下面相应的文字
wage = int(input("请输入你的工资："))
if wage <= 1000:
    print("月薪", wage, "：老板，我是你爹")
elif wage <= 2000:
    print("月薪", wage, "：老板，wqnmlgebxxxxx")
elif wage <= 5000:
    print("月薪", wage, "：老板脑子有坑，背后说坏话")
elif wage <= 10000:
    print("月薪", (wage / 10000), "万", "：老板说的有点问题，但是我不说话")
elif wage <= 20000:
    print("月薪", (wage / 10000), "万", "：老板说啥就是啥，给钱就行")
elif wage <= 30000:
    print("月薪", (wage / 10000), "万", "：老板说什么都是对的，如果有人错了，那一定是我")
elif wage <= 50000:
    print("月薪", (wage / 10000), "万", "：996就像呼吸一样自然")
elif wage >= 100000:
    print("月薪", (wage / 10000), "万", "：公司就是我家")
print("程序结束....")
