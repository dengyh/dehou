#coding: utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import Context,Template,RequestContext
from django.shortcuts import render_to_response, RequestContext
from backend.form import UEditorForm
from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#导入数据model
from django.contrib.auth.models import User  #用户表

# ======================================
# 	名字：导航列表
#   功能：罗列导航信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def navigation_list(request):
	return render_to_response("navigation_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：产品列表
#   功能：分页罗列产品
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def product_list(request):
	return render_to_response("product_list.html", context_instance=RequestContext(request))


# ======================================
# 	名字：添加产品
#   功能：添加产品进数据库
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def product_add(request):
	# ueditor编辑器初始化
	form = UEditorForm()
	return render_to_response("product_add.html", {"form": form}, context_instance=RequestContext(request))

# ======================================
# 	名字：工程列表
#   功能：分页罗列工程
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def project_list(request):
	return render_to_response("project_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：添加工程
#   功能：添加工程进数据库
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def project_add(request):
	# ueditor编辑器初始化
	form = UEditorForm()
	return render_to_response("project_add.html", {"form": form}, context_instance=RequestContext(request))

# ======================================
# 	名字：资讯列表
#   功能：分页罗列资讯
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def info_list(request):
	return render_to_response("info_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：添加资讯
#   功能：添加资讯进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def info_add(request):
	# ueditor编辑器初始化
	form = UEditorForm()
	return render_to_response("info_add.html", {"form": form}, context_instance=RequestContext(request))

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
# 	名字：添加管理员以及权限表单处理
#   功能：超级管理员添加普通管理员以及添加权限
#   人员：杨凯
#   日期：2014.08.22
# --------------------------------------
@csrf_exempt
def admin_add_handle(request):
	return HttpResponse('请求成功...')
	# if request.method == "POST":
	# 	username = request.POST.get('username','')
	# 	password = request.POST.get('password','')
	# 	first_name = request.POST.get('first_name','')
	# 	premissions = request.POST.getlist('premissions','')
	# 	print username
	# 	user = User(
	# 		username = username,
	# 		password =  user.set_password(password),
	# 		first_name = firsr_name,
	# 		premissions = premissions,
	# 		)
	# 	print '*'*50
	# 	print user.password
	# 	#user.save()
	# 	#return HttpResponseRedirect('/backend/admin_list')
	# 	return HttpResponse('请求成功...')
	# return HttpResponse('请求方式错误...')



