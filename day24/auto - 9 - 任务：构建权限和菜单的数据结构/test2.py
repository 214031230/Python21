#!/usr/bin/env python3
permission_list = [
    {
        'permissions__title': '用户列表',
        'permissions__url': '/app01/user/',
        'permissions__name': 'user_list',
        'permissions__menu_id': 1,
        'permissions__menu__title': '用户管理',
        'permissions__menu__icon': 'fa-clipboard',
        'permissions__parent_id': None,
        'permissions__parent__name': None
    },
    {
        'permissions__title': '订单列表',
        'permissions__url': '/app01/order/',
        'permissions__name': 'order',
        'permissions__menu_id': 2,
        'permissions__menu__title': '商品管理',
        'permissions__menu__icon': 'fa-clipboard',
        'permissions__parent_id': None,
        'permissions__parent__name': None
    }
]

menu_info = {}
for row in permission_list:
    menu_info[row["permissions__menu_id"]] = {"title": row["permissions__menu__title"],
                                              "icon": row["permissions__menu__icon"],
                                              "children": [{"title": row["permissions__title"],
                                                            "url": row["permissions__url"]}]}
print(menu_info)
