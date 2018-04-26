#!/usr/bin/env python3

TABLE = "./my_db/user_info"


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


def print_log(meg, type_info="info"):
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
            where_data = func(fields.strip(), value.strip())  # 执行where判断，返回判断结果
            return where_data   # 返回给语法解析器
    else:
        print_log("语法错误：%s" % choice.keys(), "error")


def syntax_select(where_data, query_section):
    """
    把where返回的结果根据字段打印出来
    :param where_data:  [['2', 'Egon', '23', '13304320533', 'Tearcher'], ['3', 'nezha', '25', '1333235322', 'IT']]
    :param query_section: # select name,age from user_info
    :return:
    """
    fields_tmp = query_section.split("from")[0].split("select")[1].split(",")
    fields = [i.strip() for i in fields_tmp]
    res_li = []
    lens = len(fields)
    res_li.append(fields)
    for i in where_data:
        li = []
        for k in fields:
            index = line_title.index(k)
            li.append(i[index])
        res_li.append(li)
    for i in res_li:
        print(("{:<8}" * lens).format(*i))


def syntax_insert(where_data, query_section):
    pass


def syntax_update(where_data, query_section):
    pass


def syntax_delete(where_data, query_section):
    pass


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
    action = ["select", "insert", "update", "delete"]
    if cmd.split()[0] in action:  # 判断用户输入的语法是否正确（增删改查）
        query_section, where_section = cmd.split("where")  # 根据where关键件把用户输入的命令切割成两部分，前半部分是增删改查方法，后半部分是where条件
        where_data = where_parser(where_section)  # 把where条件交给where函数进行分配判断
        action = query_section.split()[0]
        for action in choice_action:
            choice_action[action](where_data, query_section)

    else:
        print_log("语法错误: %s" % action, "error")


def main():
    """
    主运行程序
    :return:
    """
    while True:
        cmd = input("[user_info]>")
        syntax_parser(cmd)


main()