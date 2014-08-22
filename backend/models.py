#coding: utf-8
from django.db import models

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
#   img  : 图片上传路径
#content : 信息内容
# is_del : 是否删除 0表示否,1表示是,则进入回收站
#datetime: 信息发布时间
# ---------------------------
class news(models.Model):
	p_id = models.IntegerField(max_length=11)
	s_id = models.IntegerField(max_length=11)
	t_id = models.IntergerField(max_length=11,blank=True,null=True)
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
class job(models.Model):
	name = models.CharField(max_length=10)
	position = models.CharField(max_length=20)
	degree = models.CharField(max_length=20)
	files = models.FieldField(upload_to='resume',blank=True,null=True)
	datetime = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name

