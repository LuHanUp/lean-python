menuStr = '''
========================学生信息管理系统===========================
----------------------------功能菜单-----------------------------
\t\t\t\t\t\t\t\t\t1. 录入学生信息
\t\t\t\t\t\t\t\t\t2. 查找学生信息
\t\t\t\t\t\t\t\t\t3. 删除学生信息
\t\t\t\t\t\t\t\t\t4. 修改学生信息
\t\t\t\t\t\t\t\t\t5. 排序
\t\t\t\t\t\t\t\t\t6. 统计学生总人数
\t\t\t\t\t\t\t\t\t7. 显示所有学生信息
\t\t\t\t\t\t\t\t\t0. 退出系统
'''


# 新增学生信息
def insert():
    pass


# 删除学生信息
def delete():
    pass


# 查询学生信息
def search():
    pass


# 修改学生信息
def update():
    pass


# 对学生信息进行排序
def sort():
    pass


# 返回学生个数
def count():
    pass


# 显示所有学生信息
def show():
    pass


def main():
    while True:
        menu()
        choose = input("请选择:")
        try:
            choose = int(choose)
        except ValueError:
            continue
        if choose in range(8):
            if choose == 0:
                answer = input("您确定要退出吗?y/n")
                if answer == 'y':
                    print("感谢您的使用!!!")
                    break
                else:
                    continue
            elif choose == 1:
                insert()
            elif choose == 2:
                search()
            elif choose == 3:
                delete()
            elif choose == 4:
                update()
            elif choose == 5:
                sort()
            elif choose == 6:
                count()
            elif choose == 7:
                show()


# 显示系统菜单
def menu():
    print(menuStr)


if __name__ == '__main__':
    main()
