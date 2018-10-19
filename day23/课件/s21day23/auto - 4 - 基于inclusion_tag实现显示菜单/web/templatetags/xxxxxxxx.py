
# 在此处定义函数（特殊要求）
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

    return {'menus':settings.MENU_LIST}