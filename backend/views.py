#coding: utf-8
from django.template import Context,Template,RequestContext
from django.shortcuts import render_to_response, RequestContext
from backend.form import UEditorForm

# ======================================
# 	名字：新闻列表
#   功能：分页罗列新闻
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def news_list(request):
	return render_to_response("news_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：添加新闻
#   功能：添加新闻进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def news_add(request):
	# ueditor编辑器初始化
	form = UEditorForm()
	return render_to_response("news_add.html", {"form": form}, context_instance=RequestContext(request))

# ======================================
# 	名字：新闻列表
#   功能：分页罗列新闻
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def news_trash(request):
	return render_to_response("news_trash.html", context_instance=RequestContext(request))

# ======================================
# 	名字：导航列表
#   功能：罗列导航信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def navigation_list(request):
	return render_to_response("navigation_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：留言列表
#   功能：罗列留言信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def message_list(request):
	return render_to_response("message_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：添加管理员
#   功能：超级管理员添加普通管理员
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def admin_add(request):
	return render_to_response("admin_add.html", context_instance=RequestContext(request))

# ======================================
# 	名字：管理员列表
#   功能：超级管理员查看操作普通管理员
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def admin_list(request):
	return render_to_response("admin_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：招聘列表
#   功能：罗列招聘信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def job_list(request):
	return render_to_response("job_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：发布招聘
#   功能：添加招聘信息进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def job_publish(request):
	# ueditor编辑器初始化
	form = UEditorForm()
	return render_to_response("job_publish.html", {"form": form}, context_instance=RequestContext(request))