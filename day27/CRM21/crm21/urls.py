"""s21crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from crm.views import account
from crm.views import depart
from crm.views import user
from crm.views import course
from crm.views import school
from crm.views import classes
from crm.views import public
from crm.views import private
from crm.views import record
from rbac.views import menus
from rbac.views import roles
from rbac.views import permission

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录页面
    url(r'^login/', account.login, name='login'),    
    # 注销页面
    url(r'^logout/', account.logout, name='logout'),
    # 欢迎页面
    url(r'^index/', account.index, name='index'),
    # 验证码
    url(r'^v_code/', account.v_code, name='v_code'),

    # 部门管理
    url(r'^depart/list/', depart.depart_list, name='depart_list'),
    url(r'^depart/add/', depart.depart_add, name='depart_add'),
    url(r'^depart/edit/(\d+)/', depart.depart_edit, name='depart_edit'),
    url(r'^depart/del/(\d+)/', depart.depart_del, name='depart_del'),
    
    # 用户管理
    url(r'^user/list/', user.user_list, name='user_list'),
    url(r'^user/add/', user.user_add, name='user_add'),
    url(r'^user/edit/(\d+)/', user.user_edit, name='user_edit'),
    url(r'^user/del/(\d+)/', user.user_del, name='user_del'),
    
    # 课程管理
    url(r'^course/list/', course.course_list, name='course_list'),
    url(r'^course/add/', course.course_add, name='course_add'),
    url(r'^course/edit/(\d+)/', course.course_edit, name='course_edit'),
    url(r'^course/del/(\d+)/', course.course_del, name='course_del'),
    
    # 校区管理
    url(r'^school/list/', school.school_list, name='school_list'),
    url(r'^school/add/', school.school_add, name='school_add'),
    url(r'^school/edit/(\d+)/', school.school_edit, name='school_edit'),
    url(r'^school/del/(\d+)/', school.school_del, name='school_del'),
    
    # 班级管理
    url(r'^classes/list/', classes.classes_list, name='classes_list'),
    url(r'^classes/add/', classes.classes_add, name='classes_add'),
    url(r'^classes/edit/(\d+)/', classes.classes_edit, name='classes_edit'),
    url(r'^classes/del/(\d+)/', classes.classes_del, name='classes_del'),
    
    # 公共客户管理
    url(r'^public/customer/list/', public.public_customer_list, name='public_customer_list'),
    url(r'^public/customer/add/', public.public_customer_add, name='public_customer_add'),
    url(r'^public/customer/edit/(\d+)/', public.public_customer_edit, name='public_customer_edit'),
    url(r'^public/customer/del/(\d+)/', public.public_customer_del, name='public_customer_del'),
    
    # 私有客户管理
    url(r'^private/customer/list/', private.private_customer_list, name='private_customer_list'),
    url(r'^private/customer/add/', private.private_customer_add, name='private_customer_add'),
    url(r'^private/customer/edit/(\d+)/', private.private_customer_edit, name='private_customer_edit'),
    
    # 客户跟进记录管理
    url(r'^record/list/(\d+)/', record.record_list, name='record_list'),
    url(r'^record/add/(\d+)/', record.record_add, name='record_add'),

    # 权限管理（代替Django Admin中的表操作）
    # 菜单管理
    url(r'^rbac/menus/list/', menus.menus_list, name='menus_list'),
    url(r'^rbac/menus/add/', menus.menus_add, name='menus_add'),
    url(r'^rbac/menus/edit/(\d+)/', menus.menus_edit, name='menus_edit'),
    url(r'^rbac/menus/del/(\d+)/', menus.menus_del, name='menus_del'),
    
    # 角色管理
    url(r'^rbac/roles/list/', roles.roles_list, name='roles_list'),
    url(r'^rbac/roles/add/', roles.roles_add, name='roles_add'),
    url(r'^rbac/roles/edit/(\d+)/', roles.roles_edit, name='roles_edit'),
    url(r'^rbac/roles/del/(\d+)/', roles.roles_del, name='roles_del'),
    
    # 权限管理
    url(r'^rbac/permission/list/', permission.permission_list, name='permission_list'),
    url(r'^rbac/permission/add/', permission.permission_add, name='permission_add'),
    url(r'^rbac/permission/edit/(\d+)/', permission.permission_edit, name='permission_edit'),
    url(r'^rbac/permission/del/(\d+)/', permission.permission_del, name='permission_del'),
]
