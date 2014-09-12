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
#   name : 中文导航
#name_en : 英文导航
#   pid  : 存放子导航
#  level : 导航级数
#  	 title : 页面标题
#  	 title_en : 英文页面标题
#	keywords:页面关键字
#	keywords_en:英文页面关键字
#  	 description: 页面描述
#  	 description_en: 英文页面描述
# ---------------------------
class nav(models.Model):
	name = models.CharField(max_length=20)
	name_en = models.CharField(max_length=20)
	pid  = models.ForeignKey('self',blank=True,null=True,related_name='child_nav')
	level = models.IntegerField(max_length=2,blank=True,null=True)
	title = models.CharField(max_length=128,blank=True,null=True)
	title_en = models.CharField(max_length=128,blank=True,null=True)
	keywords = models.CharField(max_length=128,blank=True,null=True)
	keywords_en = models.CharField(max_length=128,blank=True,null=True)
	description = models.CharField(max_length=256,blank=True,null=True)
	description_en = models.CharField(max_length=256,blank=True,null=True)
	def __unicode__(self):
		return self.name

# ---------------------------
# 信息表 :  news
#   p_id : 一级导航id
#   s_id : 二级导航id
#   t_id : 三级导航id
#       page_title : 页面标题
#     page_title_en: 英文页面标题
#     page_keywords: 页面关键字
#  page_keywords_en: 英文页面关键字
#  page_description: 页面描述
#page_description_en: 英文页面描述
#  title : 中文信息标题
#title_en: 英文信息标题
# remark : 中文信息简要说明
#remark_en:英文信息简要说明
# url : 信息跳转页面
#url_en: 英文信息跳转页面
#   img  : 信息封面图片(固定大小)
#content : 中文信息内容
#content_en: 英文信息内容
#datetime: 信息发布时间
# ---------------------------
class news(models.Model):
	p_id = models.IntegerField(max_length=11)
	s_id = models.IntegerField(max_length=11,blank=True,null=True)
	t_id = models.IntegerField(max_length=11,blank=True,null=True)
	page_title = models.CharField(max_length=128,blank=True,null=True)
	page_title_en = models.CharField(max_length=128,blank=True,null=True)
	page_keywords = models.CharField(max_length=256)
	page_keywords_en = models.CharField(max_length=256,blank=True,null=True)
	page_description = models.CharField(max_length=256)
	page_description_en = models.CharField(max_length=256,blank=True,null=True)
	title = models.CharField(max_length=150,blank=True,null=True)
	title_en = models.CharField(max_length=150,blank=True,null=True)
	remark = models.CharField(max_length=150,blank=True,null=True)
	remark_en = models.CharField(max_length=150,blank=True,null=True)
	url = models.CharField(max_length=150,blank=True,null=True)
	url_en = models.CharField(max_length=150,blank=True,null=True)
	img  = models.ImageField(upload_to='news',blank=True,null=True)
	content = models.TextField()
	content_en = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.p_id)

	class Meta:
		ordering = ['-datetime']

# ---------------------------
# 招聘表 : resume
#   position : 中文招聘职位名称
#position_en : 英文招聘职位名称
#     content: 中文职位介绍
#  content_en: 英文职位介绍
#    datetime: 发布职位时间
# ---------------------------
class job(models.Model):
	position = models.CharField(max_length=20)
	position_en = models.CharField(max_length=20)
	content = models.TextField()
	content_en = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)

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

# ---------------------------
# advantanges: 产品优势表
#  	 problem : 产品问题
#  	big_title : 大标题
#  	big_title_en : 英文大标题
#  	 title1 : 标题1
#  	 title1_en : 标题1
#  	 title2 : 标题2
#  	 title2_en : 标题1
#	solution1: 解决方法1
#   solution2: 解决方法2
#   solution3: 解决方法3
#   solution4: 解决方法4
#  	 problem_en : 英文产品问题
#	solution1_en: 解决方法1
#   solution2_en: 解决方法2
#   solution3_en: 解决方法3
#   solution4_en: 解决方法4
# ---------------------------
class advantages(models.Model):
	problem = models.CharField(max_length=120,blank=True,null=True)
	big_title = models.CharField(max_length=120,blank=True,null=True)
	big_title_en = models.CharField(max_length=120,blank=True,null=True)
	title1 = models.CharField(max_length=120,blank=True,null=True)
	title1_en = models.CharField(max_length=120,blank=True,null=True)
	title2 = models.CharField(max_length=120,blank=True,null=True)
	title2_en = models.CharField(max_length=120,blank=True,null=True)
	solution1 = models.CharField(max_length=120,blank=True,null=True)
	solution2 = models.CharField(max_length=120,blank=True,null=True)
	solution3 = models.CharField(max_length=120,blank=True,null=True)
	solution4 = models.CharField(max_length=120,blank=True,null=True)
	problem_en = models.CharField(max_length=120,blank=True,null=True)
	solution1_en = models.CharField(max_length=120,blank=True,null=True)
	solution2_en = models.CharField(max_length=120,blank=True,null=True)
	solution3_en = models.CharField(max_length=120,blank=True,null=True)
	solution4_en = models.CharField(max_length=120,blank=True,null=True)
	def __unicode__(self):
		return self.problem

# ---------------------------
# page_keywords: 页面关键字表
#  	 nav_id: 导航类型
#  	 title : 页面标题
#  	 title_en : 英文页面标题
#	keywords:页面关键字
#	keywords_en:英文页面关键字
#  	 description: 页面描述
#  	 description_en: 英文页面描述
# ---------------------------
# class page_keywords(models.Model):
# 	nav_id = models.IntegerField(max_length=11)
# 	title = models.CharField(max_length=128,blank=True,null=True)
# 	title_en = models.CharField(max_length=128,blank=True,null=True)
# 	keywords = models.CharField(max_length=128,blank=True,null=True)
# 	keywords_en = models.CharField(max_length=128,blank=True,null=True)
# 	description = models.CharField(max_length=256,blank=True,null=True)
# 	description_en = models.CharField(max_length=256,blank=True,null=True)
# 	datetime = models.DateTimeField(auto_now_add=True)
