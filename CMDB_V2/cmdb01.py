CMDB项目概述

	自动化平台相关：CMDB资产管理
		1. 堡垒机
		2. 代码发布
		3. 配管系统、装机 
		4. 私有云/公有云 
		5. 故障自愈、预测 
		
	目标：CMDB
		1. Excel做资产管理
		2. 监控系统的联动
		3. 装机系统需求联动

		总结：cmdb资产管理开发。
		
	实现思路：
		1. agent模式
		2. ssh模式
		3. salt模式
		
		兼容以上三种模式的设计且可扩展。
		
	基本架构
		- 资产采集
		- api 
		- 管理平台

	今日内容：
		- 资产采集
		
	
内容详细：
	1. 创建项目
		- 创建：auto_client
		
			- 编写资产采集脚本(使用sup)
			
			- agent模块(auto_client运行在每台需要采集的服务器上面)
				1. 获取本机资产信息
				2. 使用requests将资产信息汇报到api，入库持久化
			- ssh/salt模块(auto_client运行在中控机上或者saltstack管理机上)
				1. 获取未采集的资产列表
				2. 循环列表，为每个服务器资产创建一个线程去采集（线程池）
				3. 使用requests将资产信息分别汇报到api，入库持久化
			
			- 相关知识点：
				1. 错误堆栈信息
					异常处理记录日志(使用e无法记录代码的行数和详细信息)
					- 使用traceback模块（也可以获取子线程的异常信息）
						- 示例：
								import traceback
								try:
									pass
								except Exception as e:
									msg = traceback.format_exc()
						print(msg)
						
				2. 唯一标识问题（自动发现会遇到的问题）
					- 如果只是物理机的话，使用sn号就可以解决
					- 如果是物理机+虚拟机：
						- 使用sn结合openstack的API来记录
						- 主机名作为唯一标识：；
							- 问题：怎么保证主机名唯一性，两台机器主机名一致怎么处理？
							- 解决方法：在client下生产一个文件(hostname)记录主机名
								- 如果是新增机器：
									则hostname为空，运行client以后保存主机名到hostname汇报到api。
									如果主机名已经存在：
										则不写入到数据库中，并记录错误日志
									如果不存在：
										则正常汇报
								- 如果是已存在机器：
									则hostname中保存有当前主机名
									如果主机名发生修改：
										则携带旧的主机名和新的主机名进行汇报：
										如果新的主机名已经存在：
											则使用旧的主机名进行汇报，并记录错误信息
										如果新的主机名不存在：
									则替换旧的主机名为新的主机名，并返回成功信息给客户端，客户端修改hostname为新的主机名
									
				3. POST方式提交数据，django的request.POST可能没有值，去request.body
					- request.body 和 request.POST区别：
					- POST: 获取请求体中的所有数据
					- body: 获取请求体中的原生数据
					如果http发送的请求体格式是：
							"hostname=123&cpu=xxxx"
					则request.POST才能进行解析
					一般情况如果在POST中获取不到值，则在body中获取值。
					
				4. 开放封闭原则：
					- 开放：对配置文件开放
					- 封闭：对源码封闭
					
				5. 线程池
				
				6. csrf token，取消个别函数的csrf token验证，使用特殊装饰器：
					如：
						@csrf_exempt #  告诉django该函数不用走csrf验证
						def asset(request):
							pass
								
				7. 在python中实现抽象类和抽象方法
					# 定义抽象类和抽象方法如果在派生类中没有实现handler方法，在调用handler就会抛出异常 raise NotImplementedError
					class Base:
						def handler(self):
							raise NotImplementedError("handler must be implemented")

					# 继承抽象类
					class Foo:
						def handler(self):
							pass	
		
		- 创建：api，基于django实现。
			- auto_server
	
	2. 项目结构设计
		- auto_client:
			a. 项目基础架构：开放封闭+工厂模式
			
			b. 约束：面向对象约束(用抽象方法实现接口类)
																		
			c. 插件的可扩展性
				
				
						
			客户端遗留的问题：
				- 错误信息 
				- 日志 
				- 插件：信息 （内存、网卡、硬盘）
			
		
		- API
			1. 写接口的三种方式：
				- FBV
					import json
					from django.shortcuts import render, HttpResponse
					from django.views.decorators.csrf import csrf_exempt
					from django.http import JsonResponse

					@csrf_exempt
					def asset(request):
						if request.method == "GET":
							return JsonResponse(['c1.com', 'c2.com', 'c3.com'], safe=False)
						info = json.loads(request.body)
						print(info)
						return HttpResponse('收到了')
						
				- CBV
					import json
					from django.shortcuts import render,HttpResponse
					from django.views.decorators.csrf import csrf_exempt
					from django.utils.decorators import method_decorator
					from django.views import View
					
					@method_decorator(csrf_exempt,name='dispatch')
					class AssetView(View):
						def get(self,requset,*args,**kwargs):
							host_list = ['c1.com', 'c2.com', 'c3.com']
							return HttpResponse(json.dumps(host_list))


						def post(self,request,*args,**kwargs):
							info = json.loads(request.body.decode('utf-8'))
							print(info)
							return HttpResponse('收到了')
							
				- restful api(推荐)
					- django rest framework
						优点：
							- 自动加 csrf_exempt
							- 页面变好看
							- 自动反序列化
						- 示例：
							from rest_framework.views import APIView
							from rest_framework.response import Response

							class AssetView(APIView):
								def get(self, requset, *args, **kwargs):
									host_list = ['c1.com', 'c2.com', 'c3.com']
									return Response(host_list)

								def post(self, request, *args, **kwargs):
									print(request.data) # json格式
									return HttpResponse('收到了')
														
							注意：注册app 
			
			2. cbv中添加装饰器
				import json
				from django.shortcuts import render,HttpResponse
				from django.views.decorators.csrf import csrf_exempt
				from django.utils.decorators import method_decorator
				from django.views import View

				class AssetView(View):
					"""
					资产相关接口
					"""
					@method_decorator(装饰器1)
					def get(self,requset,*args,**kwargs):
						host_list = ['c1.com', 'c2.com', 'c3.com']
						return HttpResponse(json.dumps(host_list))

					@method_decorator(装饰器1)
					def post(self,request,*args,**kwargs):
						info = json.loads(request.body.decode('utf-8'))
						print(info)
						return HttpResponse('收到了')
			
			3. cbv中添加装饰器csrf_exempt
					import json
					from django.shortcuts import render,HttpResponse
					from django.views.decorators.csrf import csrf_exempt
					from django.utils.decorators import method_decorator
					from django.views import View
					
					# 方式一
					@method_decorator(csrf_exempt,name='dispatch')
					class AssetView(View):
						"""
						资产相关接口
						"""
						# 方式二
						# @method_decorator(csrf_exempt)
						# def dispatch(self, request, *args, **kwargs):
						#     return super().dispatch(request, *args, **kwargs)

					
						def get(self,requset,*args,**kwargs):
							host_list = ['c1.com', 'c2.com', 'c3.com']
							return HttpResponse(json.dumps(host_list))


						def post(self,request,*args,**kwargs):
							info = json.loads(request.body.decode('utf-8'))
							print(info)
							return HttpResponse('收到了')
			
											
重点：
	1. 写代码的思路（*****）
		- 开发封闭原则
		- 设计模式：工厂模式
		
	2. 客户端开发（****）
		
		
	3. restful api (*****)
	
	
作业：
	在正式环境中定义命令并进行解析