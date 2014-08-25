#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
	 #导航列表
	url(r'^navigation_list/$', 'navigation_list',{'template_name':'navigation_list.html'}),   
	# 导航添加
	url(r'^navigation_add/$', 'navigation_add',{'template_name':'navigation_add.html'}),

	# 导航添加表单处理
	url(r'^navigation_add_handle/$','navigation_add_handle'),

	# 导航删除处理
	url(r'^del_navigation/$','del_navigation'),

	# 二级、三级导航联动
	url(r'^Twolink/$','Twolink'),

	# 产品列表
	url(r'^product_list/$','product_list',{'template_name':'product_list.html'}),

	# 添加产品
	url(r'^product_add/$','product_add',{'template_name':'product_add.html'}),

	# 添加产品表单处理
	url(r'^product_add_handle/$','product_add_handle'),

	# 工程列表
	url(r'^project_list/$','project_list',{'template_name':'project_list.html'}),   

	# 添加工程
	url(r'^project_add/$','project_add',{'template_name':'project_add.html'}),

	# 添加项目表单处理
	url(r'^pro_add_handle/$','pro_add_handle'),

	# 资讯列表
	url(r'^info_list/$'      , 'info_list',{'template_name':'info_list.html'}),  

	# 添加资讯    
	url(r'^info_add/$'       , 'info_add',{'template_name':'info_add.html'}),

	# 添加资讯表单处理     
	url(r'^info_add_handle/$','info_add_handle'),

	# 删除资讯信息       
	url(r'^del_info/$','del_info'),
	    
	url(r'^job_list'       , 'job_list'),           # 招聘列表
	url(r'^job_publish'    , 'job_publish'),        # 发布招聘
	url(r'^message_list'   , 'message_list'),       # 留言列表
	url(r'^admin_add'      , 'admin_add'),          # 添加管理员

	# 添加管理员表单处理 避免 admin_add_handle
	url(r'^user_add_handle','user_add_handle',{'template_name' : "admin_add.html"}),
	url(r'^admin_list/$','admin_list',{'template_name' : "admin_list.html"}), # 管理员列表 

	url(r'admin_delete', 'admin_delete'),			# 删除管理员
	url(r'admin_edit_url'  ,  'admin_edit_url', {'template_name' : "admin_edit.html"}),	
)