from django.db import models
from rbac.models import AbstractUserInfo


class UserProfile(models.Model):
    """
    用户信息：
        关系：
            和AdminInfo一对一的关系
            和UserGroup表多对多的关系
        说明：
            记录所有用户信息，包括运维人员，业务线负责人
            包括：可以登录CMDB用户和不能登录的用户
    """
    name = models.CharField(verbose_name='姓名', max_length=32)
    email = models.EmailField(verbose_name='邮箱地址')
    mobile = models.CharField(verbose_name='手机号', max_length=11)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name


class AdminInfo(AbstractUserInfo):
    """
    用户登录表:
        关系：
            和UserProfile一对一的关系
        说明：
            只包含可以登录CMDB平台的用户
    """
    user = models.OneToOneField(verbose_name="关联用户", to="UserProfile")


class UserGroup(models.Model):
    """
    用户组表：
        关系:
            和UserProfile表多对多的关系
        说明：
            把用户进行分组，一个用户可以有多个组，一个组可以有多个用户
    """
    name = models.CharField(verbose_name="用户组名称", max_length=32, unique=True)
    users = models.ManyToManyField(verbose_name="关联用户", to='UserProfile')

    class Meta:
        verbose_name_plural = "用户组表"

    def __str__(self):
        return self.name


class BusinessUnit(models.Model):
    """
    业务线表：
        关系：
            业务线表和UserGroup是一对多的关系
        说明：
            一个业务线只能属于多个业务线组
            一个业务线只能属于多个管理员组
    """
    name = models.CharField(verbose_name='业务线名称', max_length=64, unique=True)  # 销售，1,2
    contact = models.ForeignKey(verbose_name="所属业务线组", to="UserGroup", related_name='c')  # 业务线联系人：1
    manager = models.ForeignKey(verbose_name="所属运维管理", to="UserGroup", related_name='m')  # 运维管理人员：2

    class Meta:
        verbose_name_plural = "业务线表"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    资产标签表：
        关系：
            和Server表多对多的关系
        说明：
            每个服务器都可以有标签，可以根据标签来查找服务器，参考博客系统的根据标签查博客
    """
    name = models.CharField('标签', max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "标签表"

    def __str__(self):
        return self.name


class IDC(models.Model):
    """
    机房信息表：
        关系：
            和Server是一对多的关系
        说明：
            记录服务器的机房信息
    """
    name = models.CharField('机房', max_length=32)
    floor = models.IntegerField('楼层', default=1)

    class Meta:
        verbose_name_plural = "机房表"

    def __str__(self):
        return self.name


# class Asset(models.Model):
#     """
#     在需要交换机的时候可以增加资产表，目前不需要
#     资产信息表，所有资产公共信息（交换机，服务器，防火墙等）
#     """
#     device_type_choices = (
#         (1, '服务器'),
#         (2, '交换机'),
#         (3, '防火墙'),
#     )
#     device_status_choices = (
#         (1, '上架'),
#         (2, '在线'),
#         (3, '离线'),
#         (4, '下架'),
#     )
#
#     device_type_id = models.IntegerField(choices=device_type_choices, default=1)
#     device_status_id = models.IntegerField(choices=device_status_choices, default=1)
#
#     cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
#     cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)
#
#     # idc = models.ForeignKey('IDC', verbose_name='IDC机房', null=True, blank=True)
#     # business_unit = models.ForeignKey('BusinessUnit', verbose_name='属于的业务线', null=True, blank=True)
#
#     # tag = models.ManyToManyField('Tag')
#
#     latest_date = models.DateField(null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = "资产表"
#
#     def __str__(self):
#         return "%s-%s-%s" % (self.idc.name, self.cabinet_num, self.cabinet_order)
#
#
# class NetworkDevice(models.Model):
#     asset = models.OneToOneField('Asset')
#     management_ip = models.CharField('管理IP', max_length=64, blank=True, null=True)
#     vlan_ip = models.CharField('VlanIP', max_length=64, blank=True, null=True)
#     intranet_ip = models.CharField('内网IP', max_length=128, blank=True, null=True)
#     sn = models.CharField('SN号', max_length=64, unique=True)
#     manufacture = models.CharField(verbose_name=u'制造商', max_length=128, null=True, blank=True)
#     model = models.CharField('型号', max_length=128, null=True, blank=True)
#     port_num = models.SmallIntegerField('端口个数', null=True, blank=True)
#     device_detail = models.CharField('设置详细配置', max_length=255, null=True, blank=True)
#
#     class Meta:
#         verbose_name_plural = "网络设备"


class Server(models.Model):
    """
    服务器信息表：
        关系：
            和IDC机房表 一对多的关系
            和业务线表 一对多的关系
            和标签表 多对多的关系
            和硬盘，内存，网卡都是一对多的关系
        说明：
            记录服务器的基本信息
    """
    # asset = models.OneToOneField('Asset')
    idc = models.ForeignKey(IDC, null=True, blank=True)
    cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
    cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)
    business_unit = models.ForeignKey(BusinessUnit, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    server_status_choices = (
        (1, '上架'),
        (2, '在线'),
        (3, '离线'),
        (4, '下架'),
    )

    server_status_id = models.IntegerField(choices=server_status_choices, default=1)

    hostname = models.CharField(max_length=128, unique=True)
    sn = models.CharField('SN号', max_length=64, db_index=True)
    manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
    model = models.CharField('型号', max_length=64, null=True, blank=True)

    manage_ip = models.GenericIPAddressField('管理IP', null=True, blank=True)

    os_platform = models.CharField('系统', max_length=16, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=128, null=True, blank=True)

    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    latest_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="上次采集时间")

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
    server_obj = models.ForeignKey('Server', related_name='disk')

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
    server_obj = models.ForeignKey('Server', related_name='nic')

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

    server_obj = models.ForeignKey('Server', related_name='memory')

    class Meta:
        verbose_name_plural = "内存表"

    def __str__(self):
        return self.slot


class ServerRecord(models.Model):
    """
    服务器变更记录,creator为空时，表示是资产汇报的数据。
    """
    server_obj = models.ForeignKey('Server', related_name='ar')
    content = models.TextField(null=True)
    creator = models.ForeignKey('UserProfile', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "资产记录表"

    def __str__(self):
        return self.server_obj.hostname
    


