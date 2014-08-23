#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
	url(r'^navigation_list', 'navigation_list',{'template_name':'navigation_list.html'}),    # 导航列表
	url(r'^product_list'   , 'product_list'),       # 产品列表
	url(r'^product_add'    , 'product_add'),        # 添加产品
	url(r'^project_list'   , 'project_list'),       # 工程列表
	url(r'^project_add'    , 'project_add'),        # 添加工程
	url(r'^info_list'      , 'info_list'),          # 资讯列表
	url(r'^info_add'       , 'info_add'),		    # 添加资讯
	url(r'^job_list'       , 'job_list'),           # 招聘列表
	url(r'^job_publish'    , 'job_publish'),        # 发布招聘
	url(r'^message_list'   , 'message_list'),       # 留言列表
	url(r'^admin_add'      , 'admin_add'),          # 添加管理员

	# 添加管理员表单处理 避免 admin_add_handle
	url(r'^user_add_handle','user_add_handle',{'template_name' : "admin_add.html"}),
	url(r'^admin_list/$','admin_list',{'template_name' : "admin_list.html"}), # 管理员列表 
)