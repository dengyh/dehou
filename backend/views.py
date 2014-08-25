#coding: utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import Context,Template,RequestContext
from django.shortcuts import render_to_response, RequestContext

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import settings
import json
#导入数据model
from django.contrib.auth.models import User  #用户表
from backend.models import userInfo  #继承User表
from backend.models import nav,news

#导入form表单
from backend.form import UEditorForm,loginForm,adminForm,edit_user_Form

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password	


# ======================================
# 	名字：判断权限公共函数
#   功能：根据权限显示左侧栏目
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
def public_premissions(request):
	username = request.user                       # 获取 当前 登陆的 管理员名称
	user = User.objects.get(username=username)    # User表中找到 当前管理员
	Info = userInfo.objects.get(user=user)        # 查询userInfo
	premissions = Info.premissions
	if premissions:
		list_premissions = premissions.split(',')
		length = len(list_premissions)    
		del(list_premissions[length-1])           #移除最后一个 ',' 元素
	return list_premissions

# ======================================
# 	名字：后台首页
#   功能：显示后台首页
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
def home(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	username = request.user                       # 获取 当前 登陆的 管理员名称
	user = User.objects.get(username=username)    # User表中找到 当前管理员
	Info = userInfo.objects.get(user=user)         # 查询userInfo
	premissions = Info.premissions
	if premissions:
		list_premissions = premissions.split(',')
		length = len(list_premissions)    
		del(list_premissions[length-1])               #移除最后一个 ',' 元素
		# print list_premissions
		# data = []
		# for lists in list_premissions:
		# 	print '*'*20
		# 	print lists
		# # print '*'*20
		# # print list_premissions[0]
	return render(request,template_name,{'premissions':list_premissions})

# ======================================
# 	名字：登陆界面
#   功能：管理员登陆
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
def login_in(request,template_name):
	return render(request,template_name)

# ======================================
# 	名字：登出
#   功能：管理员登出
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
@csrf_exempt
def login_out(request):
	logout(request)
	return HttpResponseRedirect('/backend/login/')

# ======================================
# 	名字：登陆界面
#   功能：管理员登陆
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
@csrf_exempt
def check_login(request,template_name):
	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return HttpResponseRedirect('/backend/home/')
			else:
				form.errors['username'] = u'用户名或密码错误'
				return render(request,template_name,{'form':form})
		else:
			return render(request,template_name,{'form':form})			
	else:
		form = loginForm()
		return render(request,template_name,{'form': form})

# ======================================
# 	名字：导航列表
#   功能：罗列导航信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def navigation_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	navlist = nav.objects.filter(level=1)
	premissions = public_premissions(request)
	return render(request,template_name,{'navlist':navlist,'premissions':premissions})

# ======================================
# 	名字：导航添加
#   功能：添加子导航(二级、三级导航)
#   人员：杨凯
#   日期：2014.08.23
# --------------------------------------
def navigation_add(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		navId = request.GET.get('id','')
		premissions = public_premissions(request)
		return render(request,template_name,{'id':navId,'premissions':premissions})
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：导航添加表单处理
#   功能：添加子导航(二级、三级导航)
#   人员：杨凯
#   日期：2014.08.23
# --------------------------------------
@csrf_exempt
def navigation_add_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method =="POST":
		navId = request.POST.get('id','')
		# print '*'*40
		# print navId
		nav_name = request.POST.get('name','')
		p_nav = nav.objects.get(id=navId)   #找到父ID
		p = nav(
              name = nav_name,
              pid  = p_nav,
			)
		p.save()
		return HttpResponseRedirect('/backend/navigation_list/')
	return httpResponse('请求方法错误...')

# ======================================
# 	名字：导航删除
#   功能：从数据库中将导航删除
#   人员：杨凯
#   日期：2014.08.24
# --------------------------------------
def del_navigation(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		navId = request.GET.get('id','')
		delNav = nav.objects.get(id=navId)
		delNav.delete()
		return HttpResponseRedirect('/backend/navigation_list/')
	return httpResponse('请求方法错误...')

# ======================================
# 	名字：导航联动
#   功能：根据父导航实现 实现二级、三级导航的 联动效果
#   人员：杨凯
#   日期：2014.08.24
# --------------------------------------
def Twolink(request):
	if request.is_ajax():
		nav_id = request.POST.get('id','')
		nav_list = nav.objects.filter(pid=nav_id)  #获取 子导航
		data = []
		if nav_list:
			for menu in nav_list:
				temp = {}
				temp['id'] = menu.id
				temp['name'] = menu.name
				data.append(temp)
			return HttpResponse(json.dumps(data),content_type='application/json')
		else:  #没有子导航的情况
			return HttpResponse(json.dumps('error'),content_type='application/json')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：产品列表
#   功能：分页罗列产品
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def product_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	lists = news.objects.filter(p_id=1)
	premissions = public_premissions(request)
	return render(request,template_name,{'lists':lists,'premissions':premissions})


# ======================================
# 	名字：添加产品
#   功能：显示添加产品表单
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def product_add(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	# ueditor编辑器初始化
	form = UEditorForm()
	product_nav = nav.objects.filter(id=1)  #获取 佳易得产品 一级导航
	#获取 所有二级导航
	product_second_nav = nav.objects.filter(pid = product_nav[0]) 
	#获取属于当前二级导航的 三级导航
	product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	premissions = public_premissions(request)
	return render(request,template_name,{"form": form,"product_nav":product_nav,"product_second_nav":product_second_nav,"product_third_nav":product_third_nav,'premissions':premissions})

# ======================================
# 	名字：添加产品表单处理  同时 适用于  添加工程表单处理
#   功能：添加产品进数据库
#   人员：杨凯
#   日期：2014.08.23
# --------------------------------------
@csrf_exempt
def product_add_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		p_id  = request.POST.get('p_id','')
		s_id  = request.POST.get('s_id','')
		t_id  = request.POST.get('t_id','0')
		title = request.POST.get('title','')
		remark = request.POST.get('remark','')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			remark = remark,
			img = img,
			content = content,
			)
		p.save()
		return HttpResponseRedirect('/backend/product_list/')
	return HttpResponse('请求方法错误...')


# ======================================
# 	名字：工程列表
#   功能：分页罗列工程
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def project_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	lists = news.objects.filter(p_id=2)
	premissions = public_premissions(request)
	return render(request,template_name,{'lists':lists,'premissions':premissions})

# ======================================
# 	名字：添加工程
#   功能：添加工程进数据库
#   人员：黄晓佳
#   日期：2014.08.22
# --------------------------------------
def project_add(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	# ueditor编辑器初始化
	form = UEditorForm()
	product_nav = nav.objects.filter(id=2)  #获取 工程应用 一级导航
	#获取 所有二级导航
	# if len(product_nav) > 0:
	product_second_nav = nav.objects.filter(pid = product_nav[0]) 
	#获取属于当前二级导航的 三级导航
	product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	premissions = public_premissions(request)
	return render(request,template_name,{"form": form,"product_nav":product_nav,"product_second_nav":product_second_nav,"product_third_nav":product_third_nav,'premissions':premissions})


# ======================================
# 	名字：添加工程表单处理
#   功能：添加产品进数据库
#   人员：杨凯
#   日期：2014.08.23
# --------------------------------------
@csrf_exempt
def pro_add_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		p_id  = request.POST.get('p_id','')
		s_id  = request.POST.get('s_id','')
		t_id  = request.POST.get('t_id','0')
		title = request.POST.get('title','')
		remark = request.POST.get('remark','')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			remark = remark,
			img = img,
			content = content,
			)
		p.save()
		return HttpResponseRedirect('/backend/project_list/')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：资讯列表
#   功能：分页罗列资讯
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def info_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	lists = news.objects.filter(p_id__gt=2)
	premissions = public_premissions(request)
	return render(request,template_name,{'lists':lists,'premissions':premissions})

# ======================================
# 	名字：添加资讯
#   功能：添加资讯进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def info_add(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	# ueditor编辑器初始化
	form = UEditorForm()
	product_nav = nav.objects.filter(id__gt=2,level=1)   #获取  一级导航
	#获取 所有二级导航
	# if len(product_nav) > 0:
	product_second_nav = nav.objects.filter(pid = product_nav[0]) 
	#获取属于当前二级导航的 三级导航
	product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	premissions = public_premissions(request)
	return render(request,template_name,{"form": form,"product_nav":product_nav,"product_second_nav":product_second_nav,"product_third_nav":product_third_nav,'premissions':premissions})

# ======================================
# 	名字：添加资讯表单处理
#   功能：添加资讯进数据库
#   人员：杨凯
#   日期：2014.08.24
# --------------------------------------
@csrf_exempt
def info_add_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		p_id  = request.POST.get('p_id','')
		s_id  = request.POST.get('s_id','')
		t_id  = request.POST.get('t_id','0')
		title = request.POST.get('title','')
		remark = request.POST.get('remark','')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			remark = remark,
			img = img,
			content = content,
			)
		p.save()
		return HttpResponseRedirect('/backend/info_list/')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：删除资讯信息
#   功能：从数据库中将信息(包括图片处理)删除,
#   人员：杨凯
#   日期：2014.08.24
# --------------------------------------
def del_info(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		newsId = request.GET.get('id','')
		types = request.GET.get('type','')
		#print types
		delNews = news.objects.get(id=newsId)
		if delNews.img:       # 信息 中有 图片
			file_directory = settings.PROJECT_PATH + delNews.path;
			if os.path.exists(file_directory):
				os.remove(file_directory)
				delNews.delete()
				return HttpResponseRedirect('/backend/'+types+'_list/')
		else:
			delNews.delete()
			return HttpResponseRedirect('/backend/'+types+'_list/')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：招聘列表
#   功能：罗列招聘信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def job_list(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	return render_to_response("job_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：发布招聘
#   功能：添加招聘信息进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def job_publish(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
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
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	return render_to_response("message_list.html", context_instance=RequestContext(request))

# ======================================
# 	名字：添加管理员
#   功能：超级管理员添加普通管理员
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def admin_add(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	return render_to_response("admin_add.html", context_instance=RequestContext(request))

# ======================================
# 	名字：管理员列表
#   功能：超级管理员查看操作普通管理员
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def admin_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	adminlist = User.objects.all()
	premissions = public_premissions(request)
	return render(request,template_name,{'adminlist':adminlist,'premissions':premissions})

# ======================================
# 	名字：添加管理员以及权限表单处理
#   功能：超级管理员添加普通管理员以及添加权限
#   人员：杨凯
#   日期：2014.08.22
# --------------------------------------
@csrf_exempt
def user_add_handle(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		premissions = request.POST.getlist('premissions','')
		is_premissions = ''
		#是否有权限  有		
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

			return HttpResponseRedirect('/backend/admin_list/')
		else:
			return render(request,template_name,{'form':form})
	else:
		form = adminForm()
		return render(request,template_name,{'form': form})

# ======================================
# 	名字：管理员删除用户
#   功能：删除普通管理员
#   人员：黄晓佳
#   日期：2014.08.23
# --------------------------------------
@csrf_exempt
def admin_delete(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":					       		# 确保表单提交是post
		id = request.POST.get('id_attr', '')			   		# 要删除的管理员id
		password = request.POST.get('delete_attr', '')	   		# 确认密码

	userInfo = User.objects.get(id=1)				       		# 获取超级管理员
	userPassword = userInfo.password                       		# 获取超级管理员密码

	if check_password(password, userPassword):             		# 如果密码一致
		deleteUser = User.objects.get(id = id)             		# 获取要删除的用户
		deleteUser.delete()                                		# 删除用户
		deletePremissions = userInfo.objects.get(user=deleteUser)# 删除Info表中的权限	
		deletePremissions.delete()		                                       
		return HttpResponseRedirect('/backend/admin_list/')		   		# 删除成功跳转
	else:												   		# 如果密码不一致
		return HttpResponse(u'删除失败,请检查...')     		# 删除不成功跳转

# ======================================
# 	名字：管理员修改跳转
#   功能：修改跳转页面
#   人员：黄晓佳
#   日期：2014.08.23
# --------------------------------------
@csrf_exempt
def admin_edit(request, template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":							   		# 确保是get提交
		id = request.GET.get('id','')	                   		# 要修改的管理员id
	info = User.objects.get(id=id)					   		# 获取管理员信息
	premissions = public_premissions(request)
	return render(request, template_name, {'info' : info,'premissions':premissions}) # 跳转到修改页面

# ======================================
# 	名字：管理员修改
#   功能：管理员修改权限
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
@csrf_exempt
def user_edit_handle(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		admin_id = request.POST.get('id','')    # 获取管理员的id
		premissions = request.POST.getlist('premissions','') #获取管理员权限
		is_premissions = ''
		# stt = s.split(',')
		# print stt[3]
		if premissions:
			for i in premissions:
				is_premissions += i + ','    #以 ',' 分割,组合成字符串

		form = edit_user_Form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']			
			# list1 = premissions[0]
			# print premissions
			checkUser = User.objects.filter(username=username)
			# if checkUser:
			# 	form.errors['username'] = u'管理员已存在'
			# 	return render(request,template_name,{'form':form})
			  # update User表	
			edit_user = User.objects.get(id=admin_id)
			edit_user.username = username
			edit_user.first_name = first_name
			edit_user.save()
			  # update userInfo表
			UInfo = userInfo.objects.get(user=edit_user)
			UInfo.premissions = is_premissions
			UInfo.save()
			return HttpResponseRedirect('/backend/admin_list/')
		else:
			return render(request,template_name,{'form':form})
	else:
		form = adminForm()
		return render(request,template_name,{'form': form})

# ======================================
# 	名字：管理员修改响应
#   功能：修改数据库数据
#   人员：黄晓佳
#   日期：2014.08.23
# --------------------------------------
# @csrf_exempt
# def admin_edit(request, template_name):
# 	if request.method == "POST":                                # 确保表单提交是post
