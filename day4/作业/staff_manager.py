#!/usr/bin/env python3

TABLE = "./my_db/user_info"


def local_table(t_file):
    """
    把文件转换成字典类型
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
    print(table_dic)
    return table_dic


Table_DATA = local_table(TABLE)


def syntax_parser(cmd):
    """
    语法分析器
    :param cmd:
    :return:
    """

def main():
    """
    主运行程序
    :return:
    """
    while True:
        cmd = input("[user_info]")
        syntax_parser(cmd)