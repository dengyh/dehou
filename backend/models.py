#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
# ---------------------------
# 新增用户表字段 : userInfo  扩展User表字段
#           user : 存放User表字段
#   premissions  : 存放管理员权限
# ---------------------------
class userInfo(models.Model):
	user = models.OneToOneField(User,related_name='Info')
	premissions = models.CharField(max_length=30,blank=True,null=True)
	def __unicode__(self):
		return self.user.username

# ---------------------------
# 导航表 : nav
#   name : 导航名称
#   pid  : 存放子导航
#  level : 导航级数
# ---------------------------
class nav(models.Model):
	name = models.CharField(max_length=20)
	pid  = models.ForeignKey('self',blank=True,null=True,related_name='child_nav')
	level = models.IntegerField(max_length=2)
	def __unicode__(self):
		return self.name

# ---------------------------
# 信息表 :  news
#   p_id : 一级导航id
#   s_id : 二级导航id
#   t_id : 三级导航id
#  title : 信息标题
# remark : 信息简要说明
#   img  : 信息封面图片(固定大小)
#content : 信息内容
# is_del : 是否删除 0表示否,1表示是,则进入回收站
#datetime: 信息发布时间
# ---------------------------
class news(models.Model):
	p_id = models.IntegerField(max_length=11)
	s_id = models.IntegerField(max_length=11)
	t_id = models.IntegerField(max_length=11,blank=True,null=True)
	title = models.CharField(max_length=150,blank=True,null=True)
	remark = models.CharField(max_length=150,blank=True,null=True)
	img  = models.ImageField(upload_to='news',blank=True,null=True)
	content = models.TextField()
	is_del = models.BooleanField()
	datetime = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.p_id

	class Meta:
		ordering = ['-datetime']

# ---------------------------
# 简历表 : resume
#   name : 姓名
#position: 选择职位
#  degree: 学历
#  files : 简历
#datetime: 投递简历时间
# ---------------------------
class resume(models.Model):
	name = models.CharField(max_length=10)
	position = models.CharField(max_length=20)
	degree = models.CharField(max_length=20)
	files = models.FileField(upload_to='resume',blank=True,null=True)
	datetime = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['datetime']

# ---------------------------
# 留言回复表 : comments
#   	name : 用户名
#	    title: 留言标题
#     content: 留言内容 
#   send_time: 留言时间
#       admin: 管理员名字
# replay_content : 回复内容
# replay_time: 回复时间
# ---------------------------
class comments(models.Model):
	name  = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	content = models.TextField()
	send_time = models.DateTimeField(auto_now_add=True)
	admin = models.CharField(max_length=20)
	replay_content = models.TextField()
	replay_time = models.DateTimeField(blank=True,null=True)
	def __unicode__(self):
		return self.name
