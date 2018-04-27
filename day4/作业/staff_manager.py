#!/usr/bin/env python3
from tabulate import tabulate
import os
import time

user_status = {"user": None, "status": False}

FILE_PATH = "./file/"

TABLE_PATH = "./table/"

TABLE = "%suser_info" % TABLE_PATH

user_file = "%suser_list" % FILE_PATH

readme = "%shelp_file" % FILE_PATH


def table_list(path):
    """
    获取所有的表
    :param path:
    :return:
    """
    for root, dirs, files in os.walk(path):
        return files


t_list = table_list(TABLE_PATH)


def run_log(func, user):
    """记录用户调用函数日志"""
    with open("./file/fun_run_log", mode="a", encoding="utf-8") as f1:
        timer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f1.write("时间：%s 用户：%s 运行函数：%s\n" % (timer, user, func))


def op_wrapper(func):
    """
    装饰比较函数，用于异常捕捉
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            print_log("语法错误：输入的字段不存在")
    return inner


def wrapper_outer(run_log_func):
    def wrapper(main_func):
        def inner(*args, **kwargs):
            if user_status["user"] and user_status["status"]:
                result = main_func(*args, **kwargs)
                if result != None:
                    return result
            else:
                str_func = "%s " % (main_func,)
                if "blog_exit" in str_func:
                    print_log("Bye Bye!!!".center(40, "-"), "error")
                    exit()
                if "log_out" in str_func:
                    print_log("用户未登录!!!", "error")
                    exit()
                print(">>>欢迎登录MySQL:")
                count = 0
                while count < 3:
                    username = input("请输入用户名：").strip()
                    password = input("请输入密码：").strip()
                    if not username or not password:
                        print_log("用户名或密码不能为空", "error")
                    with open(user_file) as f1:
                        for i in f1:
                            user, passwd = i.split()
                            if username == user and password == passwd:
                                print_log("登录成功！欢迎:<%s>" % (username,))
                                user_status["user"] = username
                                user_status["status"] = True
                                main_func()
                        else:
                            print_log("用户名或者密码错误，请重试！")
                    count += 1
                else:
                    exit()
            res_run_log = run_log_func(main_func, user_status["user"])
            if res_run_log != None:
                return run_log_func
        return inner
    return wrapper


def local_table(t_file):
    """
    把文件转换成字典类型  {'id': ['1', '2', '3'],
                        'name': ['Alex', 'Egon', 'nezha'],
                        'age': ['22', '23', '25'],
                        'phone': ['13651054608', '13304320533', '1333235322'],
                        'job': ['IT', 'Tearcher', 'IT']}
    :param t_file:
    :return:
    """
    n = 1
    table_dic = {}
    line_info_tmp = []
    with open(t_file) as f1:
        for line in f1:
            line = line.strip()
            global line_title
            if n == 1:
                global line_title  # 生命一个全局变量
                line_title = line.split(",")
            else:
                global line_info
                line_info = line.split(",")
                line_info_tmp.append(line_info)
            n += 1
    count = 0
    for i_title in line_title:
        table_dic[i_title] = []
        for i_info in line_info_tmp:
            table_dic[i_title].append(i_info[count])
        count += 1
    # print(table_dic)
    return table_dic


Table_DATA = local_table(TABLE)


def print_log(meg, type_info="error"):
    """
    修改输出颜色
    :param meg:
    :param type_info:
    :return:
    """
    if type_info == "info":
        print(meg)
    elif type_info == "error":
        print("\033[31;0m%s\033[0m" % meg)


# @op_wrapper
def op_gt(argv_fields, argv_value):
    """
    大于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []  # 空列表接受所有匹配到的参数
    for index, value in enumerate(Table_DATA[argv_fields]):  # 循环列表进行匹配，index记录匹配元素的索引
        if float(value) > float(argv_value):  # 匹配参数
            l1 = []  # 空列表接受匹配到的单行
            for key in Table_DATA.keys():  # 循环用户表获取匹配到的完整行
                l1.append(Table_DATA[key][index])  # 根据索引匹配 并把匹配到的行添加到小列表中
            data_res.append(l1)  # 匹配到的行将以列表数据类型的存在data_res中
    return data_res


# @op_wrapper
def op_lt(argv_fields, argv_value):
    """
    小于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if float(value) < float(argv_value):
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


# @op_wrapper
def op_eq(argv_fields, argv_value):
    """
    等于判断：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if value == argv_value:
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


# @op_wrapper
def op_like(argv_fields, argv_value):
    """
    模糊匹配：
        根据判断返回数据，以列表的方式
    :param argv_fields: 字段：age
    :param argv_value:  判断的值：22
    :return:
    """
    data_res = []
    for index, value in enumerate(Table_DATA[argv_fields]):
        if argv_value in value:
            l1 = []
            for key in Table_DATA.keys():
                l1.append(Table_DATA[key][index])
            data_res.append(l1)
    return data_res


def where_parser(section):
    """
    where条件解析
    :param section: 条件: age > 22
    :return:
    """
    choice = {
        ">": op_gt,
        "<": op_lt,
        "=": op_eq,
        "like": op_like
    }
    for choice_key, func in choice.items():
        if choice_key in section:
            fields, value = section.split(choice_key)
            if fields.strip() in line_title:
                where_data = func(fields.strip(), value.strip())  # 执行where判断，返回判断结果
                return where_data   # 返回给语法解析器
            else:
                print_log("语法错误：%s字段不存在" % fields)
                return None
    else:
        print_log("语法错误：缺少条件%s" % choice.keys(), "error")
        return None


def syntax_select(where_data, query_section):
    """
    把where返回的结果根据字段打印出来
    :param where_data:  [['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param query_section: # select name,age from user_info  select * from user_info
    :return:
    """
    fields_tmp = query_section.split("from")[0].split("select")[1].split(",")  # 切割 query_section 成列表["age","name"]
    fields = [i.strip() for i in fields_tmp]  # 去掉关键字的空格
    for t_name in t_list:
        if t_name in query_section:
            if "*" in fields:
                fields = line_title
            res_li = []  # 用于存储匹配到的字段内容 每条记录以列表方式存储  res_li = [[23 ,Egon] ,[34,alex]]
            try:
                for i in where_data:   # 循环 where查的数据  ['2', 'Egon', '23', '13304320533', 'Tearcher']   ['3', 'nezha', '25', '1333235322', 'IT']]
                    li = []  # 存储字段对应的单条数据   li = [23,] --> li = [23 ,Egon]  age：li = [alex,22]  name = [Egon,34]
                    for k in fields:  # k = "age" k = "name"  fields = [age,name]
                        try:                                                                 # i = ['2', 'Egon', '23', '13304320533', 'Tearcher']
                            index = line_title.index(k)  # 返回字段对应的索引  #  line_title = [id ,name, age ,phone,job]  # age = 2  # name = 1
                            li.append(i[index])  # 添加字段对应的数据到列表 i = ['2', 'Egon', '23', '13304320533', 'Tearcher']
                        except ValueError:
                            print_log("语法错误：%s列不存在！" % k)
                            return None
                    res_li.append(li)
                print(tabulate(res_li, headers=fields, tablefmt="grid"))
                return None
            except TypeError:
                print_log("语法错误：where没有跟条件", where_data)
                return None
    else:
        print_log("语法错误：表不存在")
        return None


def syntax_insert(where_data, query_section):
    """
    :param where_data:
    :param query_section: insert into user_info values(3,nezha,25,1333235322,IT);
    :return:
    """
    if "values" in query_section:
        res_tmp = query_section.split("values")[1].split(",")
        res = [i.strip("()").strip() for i in res_tmp]
        res_w = ",".join(res)
        if len(res) != len(line_title):
            print_log("语法错误：需要%s个参数，你给了%s个" % (len(line_title), len(res)), "error")
            return None
        else:
            if res[0] in Table_DATA["id"]:
                print_log("ID重复", "error")
            else:
                with open(TABLE, mode="a") as f1:
                    f1.write(res_w + "\n")
    else:
        print_log("语法错误：缺少values")
        return None


def syntax_update(where_data, query_section):
    """

    :param where_data: = [['2', 'Egon', '23', '13304320533', 'Tearcher']]
    :param query_section:  = update user_info set age = 25
    :return:
    """
    #  根据 where_data 的id获取Table_DATA["id"]的索引，在根据索引去Table_DATA[字段]修改值
    if "set" in query_section and "=" in query_section:  # 判断语法是否有set
        res_tmp = query_section.split("set")[1].split("=")  # 取出需要修改的字段和值
        res = [i.strip() for i in res_tmp]  # 去掉空格 ["age", "25"]
        for line in where_data:
            line_id = line[0]  # 获取匹配到内容的ID
            index = Table_DATA["id"].index(line_id)  # index = id  在 Table_DATA表id列的索引
            Table_DATA[res[0]][index] = res[1]  #
        # print_log(Table_DATA)
        return Table_DATA
    else:
        print_log("语法错误：缺少set或者 = ", "error")
        return None
    # print(where_data)


def syntax_delete(where_data, query_section):
    """
    根据where条件删除匹配行
    :param where_data:  = [['1', 'Alex', '22', '13651054608', 'IT'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param query_section: delete from user_info
    :return:
    """
    if "from" in query_section:  # 判断语法是否有from
        for line in where_data:
            line_id = line[0]  # 获取匹配到内容的ID
            index = Table_DATA["id"].index(line_id)  # index = id  在 Table_DATA表id列的索引
            for dic_line in Table_DATA:  # 删除获取到的索引对应多有值
                Table_DATA[dic_line].pop(index)
        return Table_DATA
    else:
        print_log("语法错误：from", "error")
        return None


def local_file(argv):
    """
    把修改后的字典写入到文件中
    :param arv: = 修改后的Table_DATA {'id': ['1', '2', '3'],
                        'name': ['Alex', 'Egon', 'nezha'],
                        'age': ['22', '23', '25'],
                        'phone': ['13651054608', '13304320533', '1333235322'],
                        'job': ['IT', 'Tearcher', 'IT']}
    :return:
    """
    #  把字典转换成列表，在转成字符串写入到新的表文件，删除旧表文件，重命名新文件为旧文件
    with open("user_info.bak", mode="a", encoding="utf-8") as f1:
        title = ",".join(line_title)   # 获取title转换成字符串写入文件
        f1.write(title + "\n")
        li = []  #  [['1', 'Alex', '22', '13651054608', 'linux'], ['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'nezha', '25', '1333235322', 'linux']]
        for i in range(len(argv["id"])):
            li_tmp = []  # li1 = ['1', 'Alex', '22', '13651054608', 'IT']
            for f in line_title:
                li_tmp.append(argv[f][i])
            li.append(li_tmp)
        for i in li:
            info = ",".join(i)
            f1.write(info + "\n")
    os.remove(TABLE)
    os.rename("user_info.bak", TABLE)


def syntax_parser(cmd):
    """
    语法分析器
    :param cmd:  语法：select name,age from user_info where age > 22
    :return:
    """
    choice_action = {
        "select": syntax_select,
        "insert": syntax_insert,
        "update": syntax_update,
        "delete": syntax_delete
    }
    cmd = cmd.strip()
    actions = ["select", "insert", "update", "delete"]
    if cmd.split()[0] in actions:  # 判断用户输入的语法是否正确（增删改查）
        if "where" in cmd:
            query_section, where_section = cmd.split("where")  # 根据where关键件把用户输入的命令切割成两部分，前半部分是增删改查方法，后半部分是where条件
            where_data = where_parser(where_section)  # 把where条件交给where函数进行分配判断
            action = query_section.split()[0]  # action = select ...
            if action in choice_action:
                func_res = choice_action[action](where_data, query_section)  # 执行增删改成函数
                if func_res != None:
                    local_file(func_res)   # func_res 等于修改后的TABLE_DATA
        else:
            query_section = cmd  # query_section 默认值等于cmd
            where_section = "id > 0"  # 条件默认为id > 0
            where_data = where_parser(where_section)  # 把where条件交给where函数进行分配判断
            action = query_section.split()[0]  # action = select ...
            if action == "update" or action == "delete":
                print_log("语法错误：修改或删除缺少where条件")
                return None
            if action in choice_action:
                choice_action[action](where_data, query_section)  # 执行增删改成函数
    else:
        print_log("语法错误: %s" % actions, "error")
        return None


def mysql_help():
    """
    :return:
    """
    with open(readme, mode="r", encoding="utf-8") as f1:
        print("*" * 100)
        for i in f1:
            print(i, end="")
        print("\n" + "*" * 100)


@wrapper_outer(run_log)
def main():
    """
    主运行程序
    :return:
    """
    mysql_help()
    while True:
        cmd = input("[user_info]>")
        if not cmd:continue
        syntax_parser(cmd)


if __name__ == "__main__":
    main()

