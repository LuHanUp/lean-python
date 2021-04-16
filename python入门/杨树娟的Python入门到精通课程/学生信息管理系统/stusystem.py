import os

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

# 保存学生信息的文件名称
file_name = "students.txt"


# 新增学生信息
def save(lst):
    with open(file_name, "a", encoding="utf-8") as file:
        for stu_info in lst:
            file.write(str(stu_info) + '\n')


# 添加学生信息的操作
def insert():
    student_list = []
    while True:
        stu_id = input("请输入学生编号:")

        id_exists = False

        # 判断学生编号有没有重复
        if os.path.exists(file_name):  # 当文件存在时,再去校验
            with open(file_name, mode="r", encoding="utf-8") as file:
                stu_old_list = file.readlines()
                for stu_old_info in stu_old_list:
                    stu_old_info = dict(eval(str(stu_old_info)))
                    if stu_old_info["id"] == stu_id:
                        id_exists = True
                        break
        if id_exists:
            print(f"学生编号{stu_id}已经存在了,请重新输入学生编号")
            continue

        stu_name = input("请输入学生姓名:")
        english_grade = python_grade = java_grade = 0

        # 处理英语成绩
        while True:
            try:
                english_grade = int(input("请输入英语成绩:"))
                break
            except:
                print("成绩输入错误,请重新输入...ps:请输入数字")
                continue
        # 处理python成绩
        while True:
            try:
                python_grade = int(input("请输入Python成绩:"))
                break
            except:
                print("成绩输入错误,请重新输入...ps:请输入数字")
                continue
        # 处理Java成绩
        while True:
            try:
                java_grade = int(input("请输入Java成绩:"))
                break
            except:
                print("成绩输入错误,请重新输入...ps:请输入数字")
                continue

        # 信息都输入完毕后,将信息保存到字典中,然后将字典保存进列表中,带添加完毕后将列表写到文件中
        stu_info = {"id": stu_id, "stu_name": stu_name, "english_grade": english_grade, "python_grade": python_grade,
                    "java_grade": java_grade}
        student_list.append(stu_info)
        answer = input("是否继续输入学生信息?y/n:")
        if answer == 'n':
            break
    # 输入完毕后将学生信息进保存到文件中
    save(student_list)
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
                answer = input("您确定要退出吗?y/n:")
                if answer == 'y':
                    print("感谢您使用学生信息管理系统!!!")
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
