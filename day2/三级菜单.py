data = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'Google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {}
            },
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '上海': {},
    '湖北': {},
    '广东': {}
}

flag = True
while flag:
    for k in data:
        print(k)
    choice = input(">:").strip()
    if not choice:continue
    if choice in data:
        while flag:
            for i in data[choice]:
                print(i)
            choice2 = input(">>").strip()
            if choice2 == "b":
                break
            if choice2 == "q":
                flag = False
                break
            if not choice2:continue
            if choice2 in data[choice]:
                while flag:
                    for i in data[choice][choice2]:
                        print(i)
                    choice3 = input(">>>:").strip()
                    if choice3 == "b":
                        break
                    if choice3 == "q":
                        flag = False
                        break
                    if not choice3:continue
                    if choice3 in data[choice][choice2]:
                        while flag:
                            for i in data[choice][choice2][choice3]:
                                print(i)
                            choice4 = input(">>>:")
                            if not choice4:continue
                            if choice4 == "b":
                                break
                            if choice4 == "q":
                                flag = False
                                break
                            if choice4 in data[choice][choice2][choice3]:
                                while flag:
                                    for i in data[choice][choice2][choice3][choice4]:
                                        print(i)
                            else:
                                "节点不存在！"
                    else:
                        print("节点不存在！")
            else:
                print("节点不存在！")
    else:
        print("节点不存在！")

