cmdb(三)

内容回顾：
	cmdb项目：
		1. cmdb项目架构
			- 资产采集
			- api
			- 管理后台
		2. 资产采集
			- 可插拔式插件
			- 兼容多种模式扩展
			- 线程池
			- 错误堆栈信息
			- requests模块
			- 日志处理
			- 约束，通过抛出异常。
		3. api 
			- FBV和CBV
			- 反射实现资产变更记录
			- 接口加密
				- rsa数据加密（长度限制）
		
	本节相关知识点：
		1. 面向对象继承
			
			
			class Base(object):
				def f1(self):
					print('Base.f1')
					self.f2()
					
				def f2(self):
					print('Base.f2')
					
			class Foo(Base):
					
				def f2(self):
					print('Foo.f2')
			
			
			obj = Foo()
			obj.f1()
			
			"""
			Base.f1 
			Foo.f2
			"""
		
		2. super，是根据对象的类的继承关系（mro），网上找。
		
			class Base(object):
				def f2(self):
					print('Base.f2')
					
			class Foo(Base):
					
				def f2(self):
					super(Foo,self).f2()
					
					print('Foo.f2')
		
		
		
			
			class Base(object):
				def f2(self):
					super(Base,self).f2()
					print('Base.f2')
					
			class Foo(object):
				def f2(self):
					print('Foo.f2')	
					
			class Bar(Base,Foo):
					
				def f2(self):
					super(Bar,self).f2()
					print('Bar.f2')
			
			# Bar, Base ,Foo
			
			obj = Bar()
			obj.f2()
			
			super，是根据对象的类的继承关系（mro），网上找。
			
			
			
			class Base(object):
				def f2(self):
					super(Base,self).f2()
					print('Base.f2')
					
			class Foo(Base):
				def f2(self):
					super(Foo,self).f2()
					print('Foo.f2')	
					
			# Foo Base 
			obj = Foo()
			obj.f2() # 报错 
			
		3. django，ModelForm组件
			- 对用提交的数据进行校验
			- 自动生成表单
			- 快速实现数据的增加
			

今日内容：cmdb的后台管理

	1. 模板
	
	2. 业务管理
	
	3. 资产管理
	
	4. 快速实现CURD组件
	
	
内容详细：
	1. 模板
		- HTML、CSS、JS
		
	2. 业务管理
		- 传统方式：增删改查
		- stark组件：增删改查
			- 拷贝stark app到项目中
			- 配置 
				INSTALLED_APPS = [
					'django.contrib.admin',
					'django.contrib.auth',
					'django.contrib.contenttypes',
					'django.contrib.sessions',
					'django.contrib.messages',
					'django.contrib.staticfiles',
					'rest_framework',
					'stark.apps.StarkConfig',
					'api.apps.ApiConfig',
				]
			- 使用
				- 在指定app中，创建stark.py 
				- 注册想要增删改查的类 stark.py 
					from stark.service.stark import site
					from api import models

					site.register(models.BusinessUnit)
				- 配置路由
					from django.conf.urls import url,include
					from django.contrib import admin
					from stark.service.stark import site
					urlpatterns = [
						...
						url(r'^stark/',site.urls),
					]

		小总结：stark帮助用户快速完成增伤改查
			- 拷贝stark组件到项目中
			- 注册stark app （在自定义app的上方）
			- 
				from stark.service.stark import site,StarkConfig
				from api import models


				class BusinessUnitConfig(StarkConfig):
					list_display = [StarkConfig.display_checkbox,'id','name',]

				site.register(models.BusinessUnit,BusinessUnitConfig)


				class IDCConfig(StarkConfig):
					list_display = [StarkConfig.display_checkbox,'name','floor',]

				site.register(models.IDC,IDCConfig)
				
			- 路由注册 
				from django.conf.urls import url,include
				from django.contrib import admin
				from stark.service.stark import site
				urlpatterns = [
					
					url(r'^stark/',site.urls),
				]
				
				内部会自动创建URL：
					/stark/model所在app名称/model类名小写/list/
					/stark/model所在app名称/model类名小写/add/
					/stark/model所在app名称/model类名小写/2/del/
					/stark/model所在app名称/model类名小写/2/change/
					
				
			- 手动设置菜单
				
		示例：
			业务线，基本增删改查
			IDC，基本增删改查
	
	3. 主机管理
		组件功能：
			- 自动生成4个URL，可以通过extra_url进行定制。
			- 视图函数是在内部StarkConfig中实现
				url(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
				url(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
				url(r'^(?P<pk>\d+)/change/', self.wrapper(self.change_view), name=self.get_change_url_name),
				url(r'^(?P<pk>\d+)/del/', self.wrapper(self.delete_view), name=self.get_del_url_name),
			- 列表 
				- 定制显示列（数据库字段、自定义字段）
				- 删除、修改、更新
				- 模糊匹配
				- 批量操作
				- 组合搜索
				- 分页
				- 跳转是，保留原搜索条件。
			- 编辑页面
				- 时间插件的定制
				
		
	4. stark组件的实现机制
		参考django admin源码。
		
		a. 将类注册到字典中。（列表，注意：django admin是字典，我我们是列表）
			site.register(models.BusinessUnit, BusinessUnitConfig)
			
		b. 自动生成URL 
			from stark.service.stark import site
			urlpatterns = [
				url(r'^stark/',site.urls),
			]
				

			"""
			http://127.0.0.1:8000/stark/api/businessunit/list/          BusinessUnitConfig.changelist_view
			http://127.0.0.1:8000/stark/api/businessunit/add/           BusinessUnitConfig.add_view
			http://127.0.0.1:8000/stark/api/businessunit/2/change/      BusinessUnitConfig.change_view
			http://127.0.0.1:8000/stark/api/businessunit/1/del/         BusinessUnitConfig.delete_view
			"""
						
		
		
			"""
			http://127.0.0.1:8000/stark/api/idc/list/          IDCConfig.changelist_view
			http://127.0.0.1:8000/stark/api/idc/add/           IDCConfig.add_view
			http://127.0.0.1:8000/stark/api/idc/2/change/      IDCConfig.change_view
			http://127.0.0.1:8000/stark/api/idc/1/del/         IDCConfig.delete_view
			"""
						
		
			"""
			http://127.0.0.1:8000/stark/server/idc/list/          StarkConfig.changelist_view
			http://127.0.0.1:8000/stark/server/idc/add/           StarkConfig.add_view
			http://127.0.0.1:8000/stark/server/idc/2/change/      StarkConfig.change_view
			http://127.0.0.1:8000/stark/server/idc/1/del/         StarkConfig.delete_view
			"""
						
		
	5. 使用文档（在stark app中）
			
		
总结：
	模板 
	stark组件   *****
	cmdb的后台管理  
	
			

	
	
	
	
	
	
	
	
