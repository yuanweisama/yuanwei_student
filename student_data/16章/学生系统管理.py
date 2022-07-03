import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择功能'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('宁确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计
            elif choice == 7:
                show()  # 显示所有信息


def menu():
    print('===========================学生信息管理系统===========================')
    print('------------------------------功能菜单------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')


def insert():
    student = []  # 创建一个空列表
    while True:
        numb = input('请输入学号')
        if not numb:
            break

        name = input('请输入名字')
        if not name:
            break

        try:
            english = int(input('请输入english成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入Java成绩'))
        except ValueError:
            print('输入无效，不是整数类型，请重新输入')
            continue

            # 将输入的学生保存到字典
        new_student = {'numb': numb, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生的信息保存到列表
        student.append(new_student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break
    # 调用save()函数
    save(student)
    print('学生信息录入完毕')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except NameError:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        numb = ' '
        name = ' '
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2.')
            if mode == '1':
                numb = input('输入学生学号')
            elif mode == '2':
                name = input('输入学生姓名')
            else:
                print('您输入有误，请重新输入')
                search()
                with open(filename, 'r', encoding='utf-8') as file:  # 只读文件
                    student_new = file.readlines()
                for item in student_new:
                    d = dict(eval(item))
                    if numb != '':
                        if d['numb'] == numb:
                            student_query.append(d)
                    elif name != '':
                        if name != '':
                            if d[name] == name:
                                student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            student_query.clear()
            answer = input()
            if answer == 'y':
                continue
            else:
                break
        else:
            print('查无此人')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示')
        return
        # 定义标题显示格式
    format_tile = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_tile.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('numb'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java')),
                                 ))


def delete():
    while True:
        student_id = input('请输入要删除的学生的id：')
        if student_id != '':  # 如果输入值不等于空
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:  # 只读文件
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_id:
                with open(filename, 'w', encoding='utf-8') as w_file:
                    for item in student_old:
                        d_file = dict(eval(item))  # 将字符串转成字典
                        if d_file['numb'] != student_id:
                            w_file.write(str(d_file) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生已经删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后重新显示所有学生
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as refile:
            student_old = refile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生的id：')
    with open(filename, 'w', encoding='utf-8') as w_file:
        for item in student_old:
            d = dict(eval(item))
            if d['numb'] == student_id:
                print('找到学生，可以修改相关信息')
                while True:

                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except ValueError:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                w_file.write(str(d) + '\n')
                print('修改成功')
            else:
                w_file.write(str(d) + '\n')
        answer = input('是否要修改其他学生的信息？y/n\n')
        if answer == 'y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        student_new = []
        with open(filename, 'r', encoding='utf-8') as refile:
            student_list = refile.readlines()
            for item in student_list:
                d = dict(eval(item))
                student_new.append(d)

    else:
        return
    mode = input('请选择（0升序，1降序）')
    if mode == '0':
        mode_bool = False
    elif mode == '1':
        mode_bool = True
    else:
        print('输入有误请重试')
        sort()
    mode_sort = input('请选择排序方式：（1.按英语成绩，2.按python成绩，3.按java成绩，4.按总成绩）')
    if mode_sort == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=mode_bool)
    elif mode_sort == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=mode_bool)
    elif mode_sort == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=mode_bool)
    elif mode_sort == '4':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=mode_bool)
    else:
        print('输入有误请重试')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as refile:
            students = refile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存学生信息')


def show():
    students = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as refile:
            for item in refile:
                students.append(dict(eval(item)))
                if students:
                    show_student(students)
                    students.clear()
    else:
        print('暂未保存数据文件')


if __name__ == '__main__':
    main()
