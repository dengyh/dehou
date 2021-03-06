#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
	url(r'^login/$','login_in',{'template_name':'login.html'}),            # 登陆界面
	url(r'^check_login/$','check_login',{'template_name':'login.html'}),   # 登陆检查
	url(r'^login_out/$','login_out'),                                      # 登出
	url(r'^$','home',{'template_name':'home.html'}),                       # 后台首页
	url(r'^home/$','home',{'template_name':'home.html'}),                  # 后台首页

	url(r'^job_list/$'       , 'job_list',{'template_name':'job_list.html'}),                        # 招聘列表
	url(r'^job_publish/$'    , 'job_publish',{'template_name':'job_publish.html'}),                  # 发布招聘
	url(r'^job_publish_handle/$', 'job_publish_handle'),                                             # 发布招聘表单处理
	url(r'^job_edit/$', 'job_edit', {'template_name':'job_edit.html'}),                              # 修改招聘
	url(r'^job_edit_handle/$', 'job_edit_handle'),                                                   # 修改招聘表单处理

	url(r'^del_job/$'   , 'del_job'),                                                                # 招聘信息删除
	url(r'^message_list/$'   , 'message_list',{'template_name':'message_list.html'}),                # 留言列表
	url(r'^message_replay_handle/$'   , 'message_replay_handle'),                                    # 留言回复表单处理
	url(r'^del_message/$'   , 'del_message'),                                                        # 留言删除
 
	url(r'^advantages_list/$', 'advantages_list', {'template_name':'advantages_list.html'}),      # 产品优势列表
	url(r'^advantages_edit/$', 'advantages_edit', {'template_name':'advantages_edit.html'}),      # 产品优势修改
	url(r'^advantages_edit_handle/$', 'advantages_edit_handle'),                                   # 产品优势修改表单处理
)

urlpatterns += patterns('backend.views',
	url(r'^navigation_list/$', 'navigation_list',{'template_name':'navigation_list.html'}),  # 导航列表 
	url(r'^navigation_add/$', 'navigation_add',{'template_name':'navigation_add.html'}),     # 导航添加
	url(r'^navigation_add_handle/$','navigation_add_handle'),                                # 导航添加表单处理
	url(r'^del_navigation/$','del_navigation'),                                              # 导航删除处理
	url(r'^Twolink/$','Twolink',{'template_name':'Twolink.html'}),                           # 二级、三级导航联动
	url(r'^Twolink2/$','Twolink2',{'template_name':'Twolink2.html'}),                           # 二级、三级导航联动
	url(r'^navigation_edit/$', 'navigation_edit', {'template_name':'navigation_edit.html'}), # 导航修改
	url(r'^navigation_edit_handle/$', 'navigation_edit_handle'),                             # 导航修改表单处理
)

urlpatterns += patterns('backend.views',
	url(r'^product_list/$','product_list',{'template_name':'product_list.html'}),   # 产品列表
	url(r'^product_add/$','product_add',{'template_name':'product_add.html'}),      # 添加产品
	url(r'^product_add_handle/$','product_add_handle'),                             # 添加产品表单处理

	url(r'^project_list/$','project_list',{'template_name':'project_list.html'}),   # 工程列表
	url(r'^project_add/$','project_add',{'template_name':'project_add.html'}),      # 添加工程
	url(r'^pro_add_handle/$','pro_add_handle'),                                     # 添加项目表单处理

	url(r'^info_list/$', 'info_list',{'template_name':'info_list.html'}),           # 资讯列表
	url(r'^info_add/$', 'info_add',{'template_name':'info_add.html'}),              # 添加资讯
	url(r'^info_add_handle/$','info_add_handle'),                                   # 添加资讯表单处理

	url(r'^del_info/$','del_info'),                                                 # 删除资讯信息
	url(r'^edit_info/$', 'edit_info', {'template_name':'edit_info.html'}),          # 修改资讯，包括产品，工程，资讯
	url(r'^edit_info_handle/$', 'edit_info_handle'),                                # 修改资讯表单处理
)

urlpatterns += patterns('backend.views',
	url(r'^user_add_handle','user_add_handle',{'template_name' : "admin_add.html"}),          # 添加管理员表单处理 避免 admin_add_handle
	url(r'^admin_list/$','admin_list',{'template_name' : "admin_list.html"}),                 # 管理员列表 
	url(r'^admin_add/$' , 'admin_add',{'template_name':'admin_add.html'}),                    # 添加管理员
	url(r'^admin_delete/$', 'admin_delete'),			                                      # 删除管理员
	url(r'^admin_edit/$', 'admin_edit', {'template_name' : "admin_edit.html"}),	              # 管理员编辑
	url(r'^admin_edit_handle/$', 'admin_edit_handle'),                                        # 修改管理员表单处理
	url(r'^admin_changePwd/$', 'admin_changePwd', {'template_name':"admin_changePwd.html"}),  # 更改密码
	url(r'^admin_changePwd_handle$', 'admin_changePwd_handle'),                               # 更改密码表单处理
)

# urlpatterns += patterns('backend.views',
# 	url(r'^page_keyword_list/','page_keyword_list',{'template_name' : "page_keyword_list"}),          # 关键词列表
# 	url(r'^page_keyword_edit/$','page_keyword_edit',{'template_name' : "page_keyword_edit.html"}),                 # 关键词编辑
# 	url(r'^page_keyword_edit_handle/$' , 'page_keyword_edit_handle'),       #关键词表单处理
# )