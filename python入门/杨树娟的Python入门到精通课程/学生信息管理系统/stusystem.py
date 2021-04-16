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


# 读取学生信息到list中
def read_stu_list(file_patch=file_name):
    stu_list_result = []
    if os.path.exists(file_patch):
        with open(file_patch, 'r', encoding="utf-8") as file:
            stu_list = file.readlines()
            for item in stu_list:
                stu_list_result.append(dict(eval(item)))
    return stu_list_result


# 显示学生信息
def show_stu_list(stu_old_list):
    format_title = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    print(format_title.format("编号", "姓名", "英语成绩", "Python成绩", "Java成绩", "总成绩"))
    format_content = "{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^12}\t{:^10}"
    for item in stu_old_list:
        print(format_content.format(item.get("id"),
                                    item.get("stu_name"),
                                    item.get("english_grade"),
                                    item.get("python_grade"),
                                    item.get("java_grade"),
                                    int(item.get("english_grade")) + int(item.get("python_grade")) + int(
                                        item.get("java_grade"))))
    if len(stu_old_list) <= 0:
        print("暂无学生信息".center(60, "-"))


# 删除学生信息
def delete():
    if os.path.exists(file_name):
        stu_old_list = read_stu_list(file_name)  # 从文件中读取学生信息列表
        show_stu_list(stu_old_list)  # 显示学生信息
        is_deleted = False
        delete_stu_id = input("请输入要删除的学生编号:")
        un_delete_list = []
        for stu_info in stu_old_list:
            if stu_info["id"] == delete_stu_id:
                is_deleted = True
            else:
                un_delete_list.append(stu_info)
        with open(file_name, "w", encoding="utf-8") as file:
            for stu_info in un_delete_list:
                file.write(str(stu_info) + "\n")
        if is_deleted:
            print(f"学生编号{delete_stu_id}信息已被删除")
            show()  # 显示学生信息
        else:
            print("没有找到编号{0}的学生".format(delete_stu_id))
        answer = input("是否继续删除?y/n:")
        if answer == "y":
            delete()  # 进行递归删除
    else:
        print("暂无学生信息!!!")


# 查询学生信息
def search():
    stu_list = read_stu_list(file_name)
    if len(stu_list) <= 0:
        print("暂无学生信息,请先进行添加!!!")
        return
    while True:
        is_find = False
        search_stu_id = input("请输入要查找的学生编号:")
        for stu_info in stu_list:
            if stu_info.get("id") == search_stu_id:
                is_find = True
                print("找到了编号{0}的学生".format(search_stu_id))
                show_stu_list([stu_info])
        if not is_find:
            print("没有找到编号{0}的学生".format(search_stu_id))
        answer = input("是否还要继续查找?y/n:")
        if answer == "y":
            continue
        else:
            break


# 修改学生信息
def update():
    stu_list = read_stu_list(file_name)
    show_stu_list(stu_list)
    if len(stu_list) <= 0:
        print("暂无学生信息,无法修改,请先进行添加")
    else:
        if_find = False
        update_stu_id = input("请输入要修改的学生编号:")
        with open(file_name, "w", encoding="utf-8") as file:
            for stu_info in stu_list:
                if stu_info.get("id") == update_stu_id:
                    if_find = True
                    print("找到了编码{0}的学生,请修改其信息".format(update_stu_id))
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
                    stu_info["english_grade"] = english_grade
                    stu_info["python_grade"] = python_grade
                    stu_info["java_grade"] = java_grade
                file.write(str(stu_info) + "\n")
        if not if_find:
            print("没有找到要修改的学生{0}".format(update_stu_id))
        answer = input("是否继续修改?y/n:")
        if answer == "y":
            update()


# 对学生信息进行排序
def sort():
    stu_list = read_stu_list(file_name)
    while True:
        is_desc = input("请选择排序规则:0.升序 1.降序:")
        if is_desc == "0":
            is_desc = False
            break
        elif is_desc == "1":
            is_desc = True
            break
        else:
            print("您输入的不正确,请重新输入")
            continue
    while True:
        sort_field = input("请输入排序方式: 1.按照英语成绩排序 2.按照Python成绩排序 3.按照Java成绩排序 0.按照总成绩排序:")
        if sort_field == "1":
            stu_list.sort(key=lambda item: int(item["english_grade"]), reverse=is_desc)
        elif sort_field == "2":
            stu_list.sort(key=lambda item: int(item["python_grade"]), reverse=is_desc)
        elif sort_field == "3":
            stu_list.sort(key=lambda item: int(item["java_grade"]), reverse=is_desc)
        elif sort_field == "0":
            stu_list.sort(
                key=lambda item: int(item["english_grade"]) + int(item["python_grade"]) + int(item["java_grade"]),
                reverse=is_desc)
        else:
            print("您输入的不合法,请重新输入")
            continue
        show_stu_list(stu_list)
        break
    answer = input("是否继续进行排序?y/n:")
    if answer == "y":
        sort()


# 返回学生个数
def count():
    print("学生总个数:{0}".format(len(read_stu_list(file_name))))


# 显示所有学生信息
def show():
    show_stu_list(read_stu_list(file_name))


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

'''
项目打包成可执行文件
1. 安装第三方模块PyInstaller
    window:pip install PyInstaller
    mac:pip3 install PyInstaller
2. 执行打包操作
    pyinstaller -F py文件路径
'''
