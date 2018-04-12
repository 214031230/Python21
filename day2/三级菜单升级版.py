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

next_level = data
current_layer = []
while True:
    for k in next_level:
        print(k)
    choice = input(">:").strip()
    if not choice:continue
    if choice in next_level:
        current_layer.append(next_level)
        next_level = next_level[choice]
    elif choice == "b":
        next_level = current_layer.pop()
    else:
        print("节点不存在！")




