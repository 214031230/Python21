
内容概要：
	1. 采集资产的补充
	
	2. API【资产入库】
	
内容详细：
	1. 采集资产的补充
		1. 采集插件补充
			- 新增CPU、basic、main_board
			- 采集插件异常处理+错误堆栈信息
	
		2. 日志
			- logging + 单例模式
			
		3. 插件补充
			- 基本信息
			- 主板信息
			
			修改资产信息格式 = 
								{
									'disk': {
										'status': True,
										'error': None,
										'data': {
											'0': {
												'slot': '0',
												'pd_type': 'SAS',
												'capacity': '279.396',
												'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'
											},
											'1': {
												'slot': '1',
												'pd_type': 'SAS',
												'capacity': '279.396',
												'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'
											},
											'2': {
												'slot': '2',
												'pd_type': 'SATA',
												'capacity': '476.939',
												'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'
											},
											'3': {
												'slot': '3',
												'pd_type': 'SATA',
												'capacity': '476.939',
												'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'
											},
											'4': {
												'slot': '4',
												'pd_type': 'SATA',
												'capacity': '476.939',
												'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'
											},
											'5': {
												'slot': '5',
												'pd_type': 'SATA',
												'capacity': '476.939',
												'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'
											}
										}
									},
									'memory': {
										'status': True,
										'error': None,
										'data': {
											'DIMM #0': {
												'capacity': 1024,
												'slot': 'DIMM #0',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #1': {
												'capacity': 0,
												'slot': 'DIMM #1',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #2': {
												'capacity': 0,
												'slot': 'DIMM #2',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #3': {
												'capacity': 0,
												'slot': 'DIMM #3',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #4': {
												'capacity': 0,
												'slot': 'DIMM #4',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #5': {
												'capacity': 0,
												'slot': 'DIMM #5',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #6': {
												'capacity': 0,
												'slot': 'DIMM #6',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											},
											'DIMM #7': {
												'capacity': 0,
												'slot': 'DIMM #7',
												'model': 'DRAM',
												'speed': '667 MHz',
												'manufacturer': 'Not Specified',
												'sn': 'Not Specified'
											}
										}
									},
									'network': {
										'status': True,
										'error': None,
										'data': {
											'eth0': {
												'up': True,
												'hwaddr': '00:1c:42:a5:57:7a',
												'ipaddrs': '10.211.55.4',
												'netmask': '255.255.255.0'
											}
										}
									},
									'basic': {
										'status': True,
										'error': None,
										'data': {
											'os_platform': 'linux',
											'os_version': '6.5',
											'hostname': 'c1.com'
										}
									},
									'cpu': {
										'status': True,
										'error': None,
										'data': {
											'cpu_count': 24,
											'cpu_physical_count': 2,
											'cpu_model': ' Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz'
										}
									},
									'main_board': {
										'status': True,
										'error': None,
										'data': {
											'manufacturer': 'Parallels Software International Inc.',
											'model': 'Parallels Virtual Platform',
											'sn': 'Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30'
										}
									},
									'type': 'update'
								}
		
		3.1 Agent引擎唯一标识问题处理
			- 只有在agent模式中会遇到唯一标识问题
	
	2. API【资产入库】
		1. 数据库设计 
			from django.db import models


			class BusinessUnit(models.Model):
				"""
				业务线
				"""
				name = models.CharField('业务线', max_length=64, unique=True)

				class Meta:
					verbose_name_plural = "业务线表"

				def __str__(self):
					return self.name


			class IDC(models.Model):
				"""
				机房信息
				"""
				name = models.CharField('机房', max_length=32)
				floor = models.IntegerField('楼层', default=1)

				class Meta:
					verbose_name_plural = "机房表"

				def __str__(self):
					return self.name


			class Server(models.Model):
				"""
				服务器信息
				"""

				device_status_choices = (
					(1, '上架'),
					(2, '在线'),
					(3, '离线'),
					(4, '下架'),
				)
				device_status_id = models.IntegerField(choices=device_status_choices, default=1)

				idc = models.ForeignKey('IDC', verbose_name='IDC机房', null=True, blank=True)
				cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
				cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)

				business_unit = models.ForeignKey('BusinessUnit', verbose_name='属于的业务线', null=True, blank=True)

				# 基本信息 + 主板信息 + CPU信息
				hostname = models.CharField(max_length=128, unique=True)
				os_platform = models.CharField('系统', max_length=16, null=True, blank=True)
				os_version = models.CharField('系统版本', max_length=16, null=True, blank=True)

				sn = models.CharField('SN号', max_length=64, db_index=True)
				manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
				model = models.CharField('型号', max_length=64, null=True, blank=True)

				cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
				cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
				cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)

				latest_date = models.DateField(null=True)
				create_at = models.DateTimeField(auto_now_add=True, blank=True)

				class Meta:
					verbose_name_plural = "服务器表"

				def __str__(self):
					return self.hostname


			class Disk(models.Model):
				"""
				硬盘信息
				"""
				slot = models.CharField('插槽位', max_length=8)
				model = models.CharField('磁盘型号', max_length=32)
				capacity = models.FloatField('磁盘容量GB')
				pd_type = models.CharField('磁盘类型', max_length=32)

				server = models.ForeignKey(verbose_name='服务器', to='Server', related_name='disk_list')

				class Meta:
					verbose_name_plural = "硬盘表"

				def __str__(self):
					return self.slot


			class NIC(models.Model):
				"""
				网卡信息
				"""
				name = models.CharField('网卡名称', max_length=128)
				hwaddr = models.CharField('网卡mac地址', max_length=64)
				netmask = models.CharField(max_length=64)
				ipaddrs = models.CharField('ip地址', max_length=256)
				up = models.BooleanField(default=False)
				server = models.ForeignKey('Server', related_name='nic_list')

				class Meta:
					verbose_name_plural = "网卡表"

				def __str__(self):
					return self.name


			class Memory(models.Model):
				"""
				内存信息
				"""
				slot = models.CharField('插槽位', max_length=32)
				manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)
				model = models.CharField('型号', max_length=64)
				capacity = models.FloatField('容量', null=True, blank=True)
				sn = models.CharField('内存SN号', max_length=64, null=True, blank=True)
				speed = models.CharField('速度', max_length=16, null=True, blank=True)

				server = models.ForeignKey('Server', related_name='memory_list')

				class Meta:
					verbose_name_plural = "内存表"

				def __str__(self):
					return self.slot


			class AssetRecord(models.Model):
				"""
				资产变更记录,creator为空时，表示是资产汇报的数据。
				"""
				server = models.ForeignKey('Server', related_name='servers')
				content = models.TextField(null=True)
				# creator = models.ForeignKey('UserProfile', null=True, blank=True)
				create_at = models.DateTimeField(auto_now_add=True)

				class Meta:
					verbose_name_plural = "资产记录表"


			class ErrorLog(models.Model):
				"""
				错误日志,如：agent采集数据错误 或 运行错误
				"""
				server = models.ForeignKey('Server', null=True, blank=True)
				title = models.CharField(max_length=16)
				content = models.TextField()
				create_at = models.DateTimeField(auto_now_add=True)

				class Meta:
					verbose_name_plural = "错误日志表"

				def __str__(self):
					return self.title

		2. 录入资产数据（采集器汇报的信息字段和数据库对应，方便创建。使用**字典即可创建）
			- create 找到disk_info有，disk_queryset 无
			- update 找到disk_queryset有，disk_info无
			- update-hostname 找到disk_info有，disk_queryset 有
			 	
		3. API验证 
			1. 使用密钥+时间生成动态密钥认证
				三步判断方法：
					- 判断key的时间是否超时
					- 判断key是否存在
					- 判断key是否正确
			2. 简版写法
				server:
					from rest_framework.views import Response
					from django.http import JsonResponse
					from api import models
					from api.lib import service
					from django.views import View
					from django.utils.decorators import method_decorator
					from django.views.decorators.csrf import csrf_exempt

					auth_key = "32425sdf23423tsdf324"
					key_dict = {}


					def get_key(ctime):
						key = "%s|%s" % (auth_key, ctime)
						md5 = hashlib.md5()
						md5.update(key.encode("utf-8"))
						return md5.hexdigest()


					@method_decorator(csrf_exempt, name="dispatch")
					class TestApi(View):
						def get(self, request):
							pass

						def post(self, request):
							info = {
								"status": True,
								"msg": None
							}
							# api认证开始
							server_ctime = time.time()
							client_ctime = request.GET.get("ctime")
							client_key = request.GET.get("key")
							# 1. 判断key的时间是否超时
							if int(server_ctime) - int(float(client_ctime)) > 5:
								info["status"] = False
								info["msg"] = "key已经超时"
								return JsonResponse(info, json_dumps_params={'ensure_ascii': False})

							# 2. 判断key存不存在
							if client_key in key_dict:
								info["status"] = False
								info["msg"] = "key已经被使用"
								return JsonResponse(info, json_dumps_params={'ensure_ascii': False})

							# 3. 判断key是否正确
							server_key = get_key(client_ctime)
							if client_key != server_key:
								info["status"] = False
								info["msg"] = "key错误"
								return JsonResponse(info, json_dumps_params={'ensure_ascii': False})
							# 保存使用过的key
							key_dict[client_key] = client_ctime
							print(request.POST.get("data"))
							return JsonResponse(info)
				client:
					#!/usr/bin/env python3
					import requests
					import time
					import hashlib

					key = "32425sdf23423tsdf324"
					ctime = time.time()

					key = "%s|%s" % (key, ctime)
					md5 = hashlib.md5()
					md5.update(key.encode("utf-8"))
					key = md5.hexdigest()

					response = requests.post(
						url="http://127.0.0.1:8000/api/test/",
						params={"key": key, "ctime": ctime},
						data={"data": "aaaa"}
					)
					print(response.text)
			3. 使用RestAPI
				server:
					import time
					import hashlib
					from rest_framework.views import APIView
					from rest_framework.views import Response
					from django.http import JsonResponse
					from api import models
					from api.lib import service
					from django.views import View
					from django.utils.decorators import method_decorator
					from django.views.decorators.csrf import csrf_exempt
					class TestApi(APIView):
					def dispatch(self, request, *args, **kwargs):
						info = {
							"status": True,
							"msg": None
						}
						# api认证开始
						server_ctime = time.time()
						client_ctime = request.GET.get("ctime")
						client_key = request.GET.get("key")
						# 1. 判断key的时间是否超时
						if int(server_ctime) - int(float(client_ctime)) > 5:
							info["status"] = False
							info["msg"] = "key已经超时"
							return Response(info)

						# 2. 判断key存不存在
						if client_key in key_dict:
							info["status"] = False
							info["msg"] = "key已经被使用"
							return Response(info)

						# 3. 判断key是否正确
						server_key = get_key(client_ctime)
						if client_key != server_key:
							info["status"] = False
							info["msg"] = "key错误"
							return Response(info)
						# 保存使用过的key
						key_dict[client_key] = client_ctime
						return super().dispatch(request, *args, **kwargs)

					def get(self, request):
						host_list = ["c1.com", "c2.com"]
						return Response(host_list)

					def post(self, request):
						print(request.POST.get("data"))
						return Response("POST访问成功")		
				client:
					#!/usr/bin/env python3
					import requests
					import time
					import hashlib

					key = "32425sdf23423tsdf324"
					ctime = time.time()

					key = "%s|%s" % (key, ctime)
					md5 = hashlib.md5()
					md5.update(key.encode("utf-8"))
					key = md5.hexdigest()

					response = requests.post(
						url="http://127.0.0.1:8000/api/test/",
						params={"key": key, "ctime": ctime},
						data={"data": "aaaa"}
					)
					print(response.text)
		
		4. rsa加密 
		
		5. 资产变更记录
			1. 问 
				- 给你一个数据库类，请帮我找到他的所有字段；
					
					示例：
						class OrmView(APIView):
							def get(self,request):
								for filed in models.Disk._meta.fields:
									print(filed.name,filed.verbose_name)
								return Response('...')
				
				- 给你一个类和一个名称，找到他的verbose_name
					cls = models.Disk
					name = 'slot'
					
					obj = cls._meta.get_field(name)
					print(obj.verbose_name)
					
				- 给你一个字典
				
					cls = models.Disk
				
					info = {
						'slot': '0',
						'pd_type': 'SAS',
						'capacity': '279.396',
						'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'
					}
					
					得到一个字符串："插槽位：0；磁盘类型：SAS；型号：SEAGATE ST300MM0006     LS08S0K2B5NV；磁盘容量GB：279.396"
					
				
				- 以上知识点+反射实现：资产变更记录。
				
				注意：硬盘
			2. 记录硬盘更新记录代码示例：
				def disk(request, server):
					"""
					 数据库录入硬盘信息
					:param request:
					:param server:
					:return:
					"""
					# 2.1 取到数据库中的硬盘信息
					disk_queryset = models.Disk.objects.filter(server=server)

					# 2.2 取到采集传递过来的硬盘信息
					disk_info = request.data["disk"]["data"]

					# 2.3 根据槽位转成集合，判断哪些槽位进行了更新，删除，增加
					disk_queryset_set = {i.slot for i in disk_queryset}
					disk_info_set = set(disk_info)

					# 2.3.1 需要增加的
					add_slot_list = disk_info_set - disk_queryset_set
					# 2.3.2 需要删除的
					del_slot_list = disk_queryset_set - disk_info_set
					# 2.3.3 需要更新的
					update_slot_list = disk_queryset_set & disk_info_set

					# 2.4 增加硬盘
					for slot in add_slot_list:
						row_dict = disk_info[slot]
						record_list = []
						for name, new_value in row_dict.items():
							verbose_name = models.Disk._meta.get_field(name)
							tpl = "%s: %s" % (verbose_name, new_value)
							record_list.append(tpl)
						if record_list:
							msg = "【新增硬盘】 槽位%s新增硬盘，硬盘信息：%s" % (slot, ";".join(record_list))
							models.AssetRecord.objects.create(server=server, content=msg)
						row_dict["server"] = server
						# models.Disk.objects.create(**row_dict)
					# 2.5 删除硬盘
					models.Disk.objects.filter(server=server, slot__in=del_slot_list).delete()
					if del_slot_list:
						msg = "【硬盘删除】 移除槽位%s的硬盘" % (";".join(del_slot_list),)
						models.AssetRecord.objects.create(server=server, content=msg)
					# 2.6 更新硬盘
					for slot in update_slot_list:
						# models.Disk.objects.filter(server=server, slot=slot).update(**disk_info[slot])
						# 取到硬盘对象
						obj = models.Disk.objects.filter(server=server, slot=slot).first()
						# 取到采集传递过来的硬盘槽位信息
						row_dict = disk_info[slot]
						record_list = []
						for name, new_value in row_dict.items():
							old_value = str(getattr(obj, name))
							if old_value != new_value:
								setattr(obj, name, new_value)
								verbose_name = models.Disk._meta.get_field(name).verbose_name
								msg = "【硬盘变更】槽位%s: %s由%s更新为%s" % (slot, verbose_name, old_value, new_value)
								record_list.append(msg)
						obj.save()
						if record_list:
							models.AssetRecord.objects.create(server=server, content=";".join(record_list))

		
		
作业：资产变更记录
	- 基本信息 
	- 网卡
	- 内存

	
	 