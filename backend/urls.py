#coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
	url(r'^news_list'      , 'news_list'),          # 新闻列表
	url(r'^news_add'       , 'news_add'),		    # 添加新闻
	url(r'^news_trash'     , 'news_trash'),         # 回收站
	url(r'^navigation_list', 'navigation_list'),    # 导航列表
	url(r'^message_list'   , 'message_list'),       # 留言列表
	url(r'^admin_add'      , 'admin_add'),          # 添加管理员
	url(r'^admin_list'     , 'admin_list'),         # 管理员列表
	url(r'^job_list'       , 'job_list'),           # 招聘列表
	url(r'^job_publish'    , 'job_publish'),        # 发布招聘
)