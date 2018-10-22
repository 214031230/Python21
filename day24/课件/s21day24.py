s21day24 

内容回顾：
	1.使用别人源码，启动：解释器+工作目录
	
	2. django请求生命周期
	
	3. 配置文件
		- key必须大写
		- 导入配置
			from django.conf import settings
	
	3. 在模板中定义函数
		- sample_tag
		- inclusion_tag
	
	4. 寻找模板的顺序（静态文件）
		- 最外层templates目录 （static）
		- 去注册的app下的templates目录中找（按照app注册顺序）（static）
		
	5. auto示例：所有用户登录后看到的菜单都一样。


今日内容：
	1. 菜单+权限信息=> 数据库
	
	2. 权限组件的应用（含菜单）
	
	3. crm业务
	
内容详细：
	1. 菜单+权限信息=> 数据库
		a. 数据库设计
			from django.db import models

			class Menu(models.Model):
				"""
				菜单表
				"""
				title = models.CharField(verbose_name='标题',max_length=32)
				icon = models.CharField(verbose_name='图标',max_length=32)


			class Permission(models.Model):
				"""
				权限表
				"""
				url = models.CharField(verbose_name='URL(含正则)', max_length=128)
				title = models.CharField(verbose_name='名称',max_length=32)
				name = models.CharField(verbose_name='别名',max_length=32,unique=True)

				menu = models.ForeignKey(verbose_name='管理菜单',to='Menu',to_field='id',null=True,blank=True)
				parent = models.ForeignKey(verbose_name='父菜单',to='Permission',null=True,blank=True)
				
				
			class Role(models.Model):
				"""
				角色表
				"""
				title = models.CharField(verbose_name='名称', max_length=32)
				permissions = models.ManyToManyField(verbose_name='关联权限',to='Permission')
				
				
			class UserInfo(models.Model):
				"""
				用户表
				"""
				username = models.CharField(verbose_name='用户名',max_length=32)
				password = models.CharField(verbose_name='密码',max_length=64)
				roles = models.ManyToManyField(verbose_name='关联角色',to='Role')
	
		b. 数据填充
			
		
		c. 上一节功能去掉
			- 去掉web app
			- url.py
				urlpatterns = [
					url(r'^admin/', admin.site.urls),
					# url(r'^web/', include('web.urls')),
				]
			- settings.py 
				去掉 MENU_LIST
				去掉注册的app：    'web.apps.WebConfig',
	
		
		d. 获取权限和菜单信息
			用户登录：马帅，UserInfo表中做查询，登录成功后获取两部分数据：
			权限 = {
				"user": {"url":'/app01/user/'},
				"user_add": {"url":'/app01/user/add/'},
				"user_edit": {"url":'/app01/user/edit/(\d+)'},
				"order": {"url":'/app01/order/'},
			}
			
			菜单信息 = {
				1:{
					'title':'用户管理',
					'icon':'fa-clipboard',
					'children':[
						{'title':'用户列表','url':'/app01/user/'},
					]
				},
				2:{
					'title':'商品管理',
					'icon':'fa-clipboard',
					'children':[
						{'title':'订单列表','url':'/app01/order/'},
					]
				}
			
			}
			
		
		e. 权限控制 
		
		
		f. 动态生成二级菜单
		
		
		
		g. 粒度控制到按钮级别
			- 权限别名 
			- filter 
		
		
	2. 使用权限系统
		1. 拷贝rbac应用
		
		2. 删除rbac/migrations目录中除 __init__.py 以外的所有文件
		
		3. 配置文件中注册 rbac的app
			INSTALLED_APPS = [
				...
				'rbac.apps.RbacConfig',
			]
		
		4. 数据库迁移 
			python manage.py makemigrations
			python manage.py migrate
			
		
		5. 编写测试系统的业务逻辑
			如果使用rbac中的模板的话，需要先删除layout.html中的：
				 <!-- 导入xxxxxxx模块 -->
				{% load rbac %}
				<!-- 执行get_menu函数并传递了一个参数 -->
				{% get_menu request %}
		
			业务逻辑开发完毕....
	
		6. 设置权限相关的配置文件
			# ############################ 权限+菜单相关配置 #############################
			RBAC_PERMISSION_SESSION_KEY = "ijksdufwesdfs"
			RBAC_MENU_SESSION_KEY = "rtwsdfgwerffsd"

			VALID_LIST = [
				'/api/login/',
				'/admin/.*'
			]
			
		7. 基于django admin 录入权限数据
			- 菜单 
			- 权限 
			- 权限角色关系表
			- 角色 
			- 用户角色关系表
			- 用户 
			
		8. 权限和菜单信息的应用
			- 用户登录：初始化权限和菜单信息
				def login(request):
					"""
					用户登录
					:param request:
					:return:
					"""
					if request.method == "GET":
						return render(request, 'api/login.html')
					
					user = request.POST.get('user')
					pwd = request.POST.get('pwd')
					
					user = rbac_model.UserInfo.objects.filter(username=user, password=pwd).first()
					if not user:
						return render(request, 'api/login.html', {'msg': '用户名或密码错误'})
					# ############ 看这里 ############
					init_permission(user, request)
					
					return redirect('/api/app/list/')
			- 中间件：权限判断
				settings.py 
					MIDDLEWARE = [
						...
						'rbac.middlewares.rbac.RBACMiddleware',
					]
			- inclusion_tag:动态生成菜单 
				layout.html 
					<div class="menu-body">
						{% load rbac %}

						{% get_menu request %}
					</div>
						
			
		9. 控制页面按钮
			
			{% extends 'layout.html' %}
			
			{% load rbac %} 

			{% block content %}
				<h1>应用列表</h1>
				
				{% if 'app_add'|permission:request %}
					<a class="btn btn-primary" href="{% url 'app_add' %}">添加</a>
				{% endif %}
				
				<table class="table table-bordered">
					<thead>
						<tr>
							<th>ID</th>
							<th>姓名</th>
							 {% if "app_edit"|permission:request or "app_del"|permission:request %}
							<th>操作</th>
							{% endif %}
						</tr>
					</thead>
					<tbody>
						{% for row in app_queryset %}
							<tr>
								<td>{{ row.id }}</td>
								<td>{{ row.title }}</td>
								{% if "app_edit"|permission:request or "app_del"|permission:request %}
								<td>
									{% if "app_edit"|permission:request %}
										<a href="{% url 'app_edit' row.id %}">编辑</a>
									{% endif %}
									{% if "app_del"|permission:request %}
										<a href="{% url 'app_del' row.id %}/">删除</a>
									{% endif %}
								</td>
								{% endif %}
							</tr>
						{% endfor %}
					</tbody>
				</table>


			{% endblock %}
			
			
			
			
			
总结：
	1. 保存的代码：
		- 上一节示例：auto - 7 - 静态的菜单示例（最终版）.zip 
		- 本节示例：nb_test.zip 
		
	2. 权限相关
		
		1. 权限系统是如何实现的？
			基于角色的权限控制（rbac）
			
		2. 权限系统中用了哪些表？表中都有哪些字段？
		
	
		3. 你用中间件实现过什么？为什么使用中间件？
			rbac对权限的控制。
			
		4. 你认为哪里最难搞？
			- 动态二级菜单+默认选中
			- 构建菜单和权限的数据结构时。
			
		5. 其他
			...
			
	
作业：补充 nb_test 应用。
	- 8个api操作（使用ModelForm实现增删改查）
		url(r'^app/list/$', views.app_list,name='app_list'),
		url(r'^app/add/$', views.app_add,name='app_add'),
		url(r'^app/edit/(\d+)/$', views.app_edit,name='app_edit'),
		url(r'^app/del/(\d+)/$', views.app_del,name='app_del'),
		
		url(r'^api/list/$', views.api_list,name='api_list'),
		url(r'^api/add/$', views.api_add,name='api_add'),
		url(r'^api/edit/(\d+)/$', views.api_edit,name='api_edit'),
		url(r'^api/del/(\d+)/$', views.api_del,name='api_del'),
	- 9 + api 
		在api列表中设置一个按钮，点击测试。
		
		
		"""
		pip3 install requests 
		"""
		import requests
		response = requests.get(url='http://www.baidu.com')
		print(response.status_code)
		print(response.text)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
			




























			
			
			
			
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
