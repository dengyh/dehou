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
from backend.models import nav,news,comments,job

#导入form表单
from backend.form import UEditorForm,loginForm,adminForm,edit_user_Form

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password

#导入分页
from django.core.paginator import Paginator,InvalidPage,EmptyPage

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
	premissions = public_premissions(request)    #权限认证
	return render(request,template_name,{
			'navlist':navlist,
			'premissions':premissions
			}
		)

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
		premissions = public_premissions(request)   #权限认证
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
		p = nav.objects.filter(pid=navId)
		if p:
			for lists in p:
				delNav = nav.objects.get(id=lists.id)
				delNav.delete()
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
		second_nav_list = nav.objects.filter(pid=nav_id)  #获取 当前二级 子导航
		data = []
		if second_nav_list:
			for menu in second_nav_list:
				temp = {}
				temp['id'] = menu.id
				temp['name'] = menu.name
				data.append(temp)
			third_nav_list = nav.objects.filter(pid=second_nav_list[0])  #获取当前三级 子导航
			data2 = []
			if third_nav_list:
				for menu in third_nav_list:
					temp2 = {}
					temp2['id'] = menu.id
					temp2['name'] = menu.name
					data2.append(temp2)
			return HttpResponse(json.dumps({
				'data' : data,
				'data2' : data2,
				}),content_type='application/json')
		else:  #没有二级导航的情况
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
	premissions = public_premissions(request)   #权限认证
	#实例化分页器
	paginator = Paginator(lists,8)
	#中文页码列表初始化
	page_list = range(0,paginator.num_pages)
	#获取中文页码列表	  
	for x in range(0,paginator.num_pages):
		page_list[x] = x+1

	#确保传进来的中文page参数为整数，如果不是，则设置为1
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
		currentpage = 1

	#确保传进来的当前page为整数，如果不是，则设置为1
	try:
		currentpage = int(request.GET.get('currentpage','1'))
	except ValueError:
		currentpage = 1

	#确保页面没有超出范围，否则输出最后一页的值
	try:
		info_list = paginator.page(page)
		currentpage = page
		# return HttpResponse(currentpage)
	except ValueError (EmptyPage, InvalidPage):
		info_list = paginator.page(paginator.num_pages)
		currentpage =paginator.num_pages
	# return HttpResponse(page)

	
	#获取上一页和下一页的值
	prevpage = currentpage - 1
	nextpage = currentpage + 1
	
	
	#确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
	if(prevpage < 1):
		prevpage = 1
	if(nextpage > paginator.num_pages):
		nextpage = paginator.num_pages
	return render(request,template_name,{
		'info_list':info_list,
		'page_list':page_list,
		'currentpage':currentpage,
		'prevpage':prevpage,
		'nextpage':nextpage,
		'premissions':premissions
		}
		)


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
	premissions = public_premissions(request)    #权限认证
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
	premissions = public_premissions(request)    #权限认证
		#实例化分页器
	paginator = Paginator(lists,8)
	#中文页码列表初始化
	page_list = range(0,paginator.num_pages)
	#获取中文页码列表	  
	for x in range(0,paginator.num_pages):
		page_list[x] = x+1

	#确保传进来的中文page参数为整数，如果不是，则设置为1
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
		currentpage = 1

	#确保传进来的当前page为整数，如果不是，则设置为1
	try:
		currentpage = int(request.GET.get('currentpage','1'))
	except ValueError:
		currentpage = 1

	#确保页面没有超出范围，否则输出最后一页的值
	try:
		info_list = paginator.page(page)
		currentpage = page
		# return HttpResponse(currentpage)
	except ValueError (EmptyPage, InvalidPage):
		info_list = paginator.page(paginator.num_pages)
		currentpage =paginator.num_pages
	# return HttpResponse(page)

	
	#获取上一页和下一页的值
	prevpage = currentpage - 1
	nextpage = currentpage + 1
	
	
	#确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
	if(prevpage < 1):
		prevpage = 1
	if(nextpage > paginator.num_pages):
		nextpage = paginator.num_pages
	return render(request,template_name,{
		'info_list':info_list,
		'page_list':page_list,
		'currentpage':currentpage,
		'prevpage':prevpage,
		'nextpage':nextpage,
		'premissions':premissions
		}
		)

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
	premissions = public_premissions(request)    #权限认证
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
	premissions = public_premissions(request)  #权限认证  
		#实例化分页器
	paginator = Paginator(lists,8)
	#中文页码列表初始化
	page_list = range(0,paginator.num_pages)
	#获取中文页码列表	  
	for x in range(0,paginator.num_pages):
		page_list[x] = x+1

	#确保传进来的中文page参数为整数，如果不是，则设置为1
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
		currentpage = 1

	#确保传进来的当前page为整数，如果不是，则设置为1
	try:
		currentpage = int(request.GET.get('currentpage','1'))
	except ValueError:
		currentpage = 1

	#确保页面没有超出范围，否则输出最后一页的值
	try:
		info_list = paginator.page(page)
		currentpage = page
		# return HttpResponse(currentpage)
	except ValueError (EmptyPage, InvalidPage):
		info_list = paginator.page(paginator.num_pages)
		currentpage =paginator.num_pages
	# return HttpResponse(page)

	
	#获取上一页和下一页的值
	prevpage = currentpage - 1
	nextpage = currentpage + 1
	
	
	#确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
	if(prevpage < 1):
		prevpage = 1
	if(nextpage > paginator.num_pages):
		nextpage = paginator.num_pages
	return render(request,template_name,{
		'info_list':info_list,
		'page_list':page_list,
		'currentpage':currentpage,
		'prevpage':prevpage,
		'nextpage':nextpage,
		'premissions':premissions
		}
		)

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
def job_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	lists = job.objects.all()
	premissions = public_premissions(request)   #权限认证
		#实例化分页器
	paginator = Paginator(lists,8)
	#中文页码列表初始化
	page_list = range(0,paginator.num_pages)
	#获取中文页码列表	  
	for x in range(0,paginator.num_pages):
		page_list[x] = x+1

	#确保传进来的中文page参数为整数，如果不是，则设置为1
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
		currentpage = 1

	#确保传进来的当前page为整数，如果不是，则设置为1
	try:
		currentpage = int(request.GET.get('currentpage','1'))
	except ValueError:
		currentpage = 1

	#确保页面没有超出范围，否则输出最后一页的值
	try:
		info_list = paginator.page(page)
		currentpage = page
		# return HttpResponse(currentpage)
	except ValueError (EmptyPage, InvalidPage):
		info_list = paginator.page(paginator.num_pages)
		currentpage =paginator.num_pages
	# return HttpResponse(page)

	
	#获取上一页和下一页的值
	prevpage = currentpage - 1
	nextpage = currentpage + 1
	
	
	#确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
	if(prevpage < 1):
		prevpage = 1
	if(nextpage > paginator.num_pages):
		nextpage = paginator.num_pages
	return render(request,template_name,{
		'info_list':info_list,
		'page_list':page_list,
		'currentpage':currentpage,
		'prevpage':prevpage,
		'nextpage':nextpage,
		'premissions':premissions
		}
		)

# ======================================
# 	名字：发布招聘
#   功能：添加招聘信息进数据库
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def job_publish(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	# ueditor编辑器初始化
	form = UEditorForm()
	premissions = public_premissions(request)   #权限认证
	return render(request,template_name,{"form": form,'premissions':premissions})

# ======================================
# 	名字：发布招聘信息处理
#   功能：添加招聘信息进数据库
#   人员：杨凯
#   日期：2014.08.26
# --------------------------------------
def job_publish_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		position = request.POST.get('position','')
		content = request.POST.get('content','')
		jobs = job.objects.create(
			position = position,
			content = content,
			)
		return HttpResponseRedirect('/backend/job_list/')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：删除招聘信息
#   功能：删除招聘信息相对应的数据
#   人员：杨凯
#   日期：2014.08.26
# --------------------------------------
def del_job(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		job_id = request.GET.get('id','')
		delJob = job.objects.get(id=job_id)
		delJob.delete()
		premissions = public_premissions(request)   #权限认证
		return render(request, "backend_href.html", {'title':"删除成功", 'href':"message",'premissions':premissions})
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：留言列表
#   功能：罗列留言信息
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def message_list(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	lists = comments.objects.all()
	premissions = public_premissions(request)   #权限认证
		#实例化分页器
	paginator = Paginator(lists,8)
	#中文页码列表初始化
	page_list = range(0,paginator.num_pages)
	#获取中文页码列表	  
	for x in range(0,paginator.num_pages):
		page_list[x] = x+1

	#确保传进来的中文page参数为整数，如果不是，则设置为1
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
		currentpage = 1

	#确保传进来的当前page为整数，如果不是，则设置为1
	try:
		currentpage = int(request.GET.get('currentpage','1'))
	except ValueError:
		currentpage = 1

	#确保页面没有超出范围，否则输出最后一页的值
	try:
		info_list = paginator.page(page)
		currentpage = page
		# return HttpResponse(currentpage)
	except ValueError (EmptyPage, InvalidPage):
		info_list = paginator.page(paginator.num_pages)
		currentpage =paginator.num_pages
	# return HttpResponse(page)

	
	#获取上一页和下一页的值
	prevpage = currentpage - 1
	nextpage = currentpage + 1
	
	
	#确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
	if(prevpage < 1):
		prevpage = 1
	if(nextpage > paginator.num_pages):
		nextpage = paginator.num_pages
	return render(request,template_name,{
		'info_list':info_list,
		'page_list':page_list,
		'currentpage':currentpage,
		'prevpage':prevpage,
		'nextpage':nextpage,
		'premissions':premissions
		}
		)

# ======================================
# 	名字：留言删除
#   功能：删除留言信息
#   人员：杨凯
#   日期：2014.08.25
# --------------------------------------
def del_message(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		message_id = request.GET.get('id','')
		delMsg = comments.objects.get(id=message_id)
		delMsg.delete()
		premissions = public_premissions(request)   #权限认证
		return render(request, "backend_href.html", {'title':"删除成功", 'href':"message",'premissions':premissions})
	return HttpResponse('请求方法错误...')


# ======================================
# 	名字：添加管理员
#   功能：超级管理员添加普通管理员
#   人员：黄晓佳
#   日期：2014.08.21
# --------------------------------------
def admin_add(request,template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	premissions = public_premissions(request)   #权限认证
	return render(request,template_name,{'premissions':premissions})

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

	if request.method == "POST":                                        # 确保表单提交是post
		ids = request.POST.get('id_attr', '')                           # 要删除的管理员id
		password = request.POST.get('delete_attr', '')                  # 确认密码

	userInfos = User.objects.get(id=1)                                  # 获取超级管理员
	userPassword = userInfos.password                                   # 获取超级管理员密码

	if check_password(password, userPassword):                        
		deleteUser = User.objects.get(id = ids)            		        # 获取要删除的用户
		deletePremissions = userInfo.objects.get(user=deleteUser)       # 删除Info表中的权限	
		deletePremissions.delete()                                      # 删除权限
		deleteUser.delete()                                		        # 删除用户

		return render(request, "backend_href.html", {'title':"用户删除成功 :)", 'href':"admin"})  # 删除成功跳转
	else:                                                             
		return render(request, "backend_href.html", {'title':"密码错误，删除失败 :(", 'href':"admin"})  # 删除失败跳转

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
		ids = request.GET.get('id','')	                   		# 要修改的管理员id

	info = User.objects.get(id=ids)					   		    # 获取管理员信息
	premissions = public_premissions(request)
	return render(request, template_name, {'info' : info,'premissions':premissions}) # 跳转到修改页面

# ======================================
# 	名字：管理员修改表单处理
#   功能：修改管理员
#   人员：黄晓佳
#   日期：2014.08.25
# --------------------------------------
@csrf_exempt
def admin_edit_handle(request):
	if request.method == "POST":
		# 获取表单
		ids = request.POST.get('id', '')
		username = request.POST['username']
		first_name = request.POST['first_name']
		premissions = request.POST.getlist('premissions','')
		is_premissions = ''
		# 以 ',' 分割,组合成字符串
		if premissions:
			for i in premissions:
				is_premissions += i + ','   	

		# 修改基本资料
		user1 = User.objects.get(id = ids)
		user1.username = username
		user1.first_name = first_name
		user1.save()

		# 修改权限
		usrInfo1 = userInfo.objects.get(user = user1)
		usrInfo1.premissions = is_premissions
		usrInfo1.save()

		return render(request, "backend_href.html", {'title':"修改成功 :)", 'href':"admin"})
	else:
		return render(request, "backend_href.html", {'title':"修改失败，请重试 :(", 'href':"admin"})

# ======================================
# 	名字：资讯修改页面
#   功能：修改页面显示资讯
#   人员：黄晓佳
#   日期：2014.08.25
# --------------------------------------
def edit_info(request, template_name):
	if request.method == "GET":
		ids = request.GET.get('id','')
		types = request.GET.get('type','')

	new = news.objects.get(id = ids)
	p_id = new.p_id
	s_id = new.s_id
	t_id = new.t_id

	p_id_name = nav.objects.get(id = p_id).name
	s_id_name = nav.objects.get(id = s_id).name
	
	premissions = public_premissions(request)

	# ueditor编辑器初始化
	form = UEditorForm()

	param = {
		'new':new, 
		'type':types, 
		'form':form,
		'p_id_name':p_id_name,
		's_id_name':s_id_name,
		'premissions':premissions,
	}

	if t_id != 0:
		t_id_name = nav.objects.get(id = t_id).name
		param['t_id_name'] = t_id_name

	return render(request, template_name, param)

# ======================================
# 	名字：资讯修改表单处理
#   功能：修改表单
#   人员：黄晓佳
#   日期：2014.08.25
# --------------------------------------
def edit_info_handle(request):
	if request.method == "POST":
		ids = request.POST['id']
		types = request.POST['type']
		title = request.POST['title']
		remark = request.POST['remark']
		hiddenImg = request.POST['hiddenImg']
		img = request.FILES.get('img', None)
		content = request.POST['content']

		# 如果没有上传图片
		if not img:
			img = hiddenImg

		# 保存修改
		new = news.objects.get(id = ids)
		new.title = title
		new.remark = remark
		new.img = img
		new.content = content
		new.save()

		return render(request, "backend_href.html", {'title':"修改成功 :)", 'href':types})
	else:
		return render(request, "backend_href.html", {'title':"修改失败，请重试 :(", 'href':types})

# ======================================
# 	名字：导航修改页面
#   功能：导航显示
#   人员：黄晓佳
#   日期：2014.08.25
# --------------------------------------
def navigation_edit(request, template_name):
	if request.method == "GET":
		ids = request.GET['id']

		navs = nav.objects.get(id = ids)
		premissions = public_premissions(request)
		return render(request, template_name, {'nav': navs,'premissions':premissions})

# ======================================
# 	名字：导航修改表单处理
#   功能：导航修改
#   人员：黄晓佳
#   日期：2014.08.25
# --------------------------------------
def navigation_edit_handle(request):
	if request.method == "POST":
		ids = request.POST['id']
		name = request.POST['name']

		navs = nav.objects.get(id = ids)
		navs.name = name
		navs.save()

		return render(request, "backend_href.html", {'title':'修改成功 :)', 'href':'navigation'})
	else:
		return render(request, "backend_href.html", {'title':'修改失败，请重试 :(', 'href':'navigation'})