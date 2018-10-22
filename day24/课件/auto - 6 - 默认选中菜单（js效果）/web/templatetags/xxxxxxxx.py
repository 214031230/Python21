import copy
from django.template import Library
from django.utils.safestring import mark_safe
from django.conf import settings

register = Library()

# 此方法在HTML中可以被调用，调用方式： {% show_menu "aasdfd" %}
@register.simple_tag
def show_menu(a1):
    return mark_safe("<a>菜单</a>")


@register.inclusion_tag('menu.html')
def get_menu(request):
    """
    :param request: 请求相关的所有数据
    :return:
    """
    # request.method
    # request.session
    # request.path_info

    new_menu_list = copy.deepcopy(settings.MENU_LIST)
    flag = False
    for item in new_menu_list:
        for child in item['children']:
            if request.path_info == child['url']:
                child['class'] = 'active'
                item['class'] = ""
                flag = True
                break
        if flag:
            break

    return {'menus':new_menu_list}