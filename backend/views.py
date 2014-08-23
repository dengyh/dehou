#coding: utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import Context,Template,RequestContext
from django.shortcuts import render_to_response, RequestContext

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#导入数据model
from django.contrib.auth.models import User  #用户表
from backend.models import userInfo  #继承User表
from backend.models import nav

#导入form表单
from backend.form import UEditorForm,adminForm

# ======================================
# 	名字：导航列表
#   功能：罗列导航信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def navigation_list(request,template_name):
	navlist = nav.objects.filter(level=1)
	return render(request,template_name,{'navlist':navlist})

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
def admin_list(request,template_name):
	adminlist = User.objects.all()
	return render(request,template_name,{'adminlist':adminlist})

# ======================================
# 	名字：添加管理员以及权限表单处理
#   功能：超级管理员添加普通管理员以及添加权限
#   人员：杨凯
#   日期：2014.08.22
# --------------------------------------
@csrf_exempt
def user_add_handle(request,template_name):
	if request.method == "POST":
		premissions = request.POST.getlist('premissions','')
		is_premissions = ''
		#是否有权限  有
		# stt = s.split(',')
		# print stt[3]
		if premissions:
			for i in premissions:
				is_premissions += i + ','    #以 ',' 分割,组合成字符串

		form = adminForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			first_name = form.cleaned_data['first_name']			
			# list1 = premissions[0]
			# print premissions
			checkUser = User.objects.filter(username=username)
			pwdMatch = password == password2
			if checkUser:
				form.errors['username'] = u'管理员已存在'
				return render(request,template_name,{'form':form})
			if not pwdMatch:
				form.errors['password'] = u'两次密码输入不一致'
				return render(request,template_name,{'form':form})
			new_user = User.objects.create_user(
						username = username,
						password = password,
						first_name = first_name,
					)
			UInfo = userInfo.objects.create(
						user = new_user,
						premissions = is_premissions,
				)
			template_name = 'admin_list.html'
			return render(request,template_name)
		else:
			return render(request,template_name,{'form':form})
	else:
		form = adminForm()
		return render(request,template_name,{'form': form})