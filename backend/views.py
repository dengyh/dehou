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
from backend.models import nav,news,comments,job,advantages

#导入form表单
from backend.form import UEditorForm,UEditorForm_en,loginForm,adminForm,edit_user_Form

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password

#导入分页
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from datetime import *
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

#---------------------------------------------------
#      名字 ： 分页公共函数
#      功能 :  实现分页
#      人员 ： 杨凯
#      日期 ： 2014.08.27
#  all_list :  传递需要分页的 数据
#       num :  传递每页显示的
#---------------------------------------------------
def public_page(request,all_list,num):
    #确保传进来的page参数为整数，如果不是，则设置为1
    try:
        page = int(request.GET.get('page','1'))
        # page =1
    except ValueError:
        page = 1
        currentpage = 1
    #分页实现
    #实例化中文分页器
    paginator = Paginator(all_list,num)
    
    #中文页码列表初始化
    if(paginator.num_pages>10):
        page_list = range(0,10)
    else:
        page_list = range(0,paginator.num_pages)
    
    #判断最大页数是否超过最大显示页数
    #判断最大显示页数是否超过实际页码范围
    if(paginator.num_pages > 10 and paginator.num_pages -page > 9):
        # page_list[0] = 1
        # page_list[1] = 2
        # page_list[2] = 3
        for x in range(0,3):
            page_list[x] = x + 1
        for x in range(3,8):
            # if(paginator.num_pages - page <= 9 ):
            #     page_list[x] = x + 9
            if page < 3:
                if page == 1:
                    page_list[x] = page + x
                else:
                    page_list[x] = page + x - 1
            else:
                page_list[x] = x + page - 2
        page_list[7] = '...'
        for x in range(8,10):
            page_list[x] = paginator.num_pages - 9 + x
    
    #如果最大页数超过最大显示页数，并且是最后几页，则只显示最后几页
    elif(paginator.num_pages > 10 and paginator.num_pages -page <= 9):
        for x in range(0,10):
            page_list[x] = paginator.num_pages - 9 + x
    
    #如果最大页码数不超过显示页码数，则将全部页数在前台输出
    else:     
        for x in range(0,paginator.num_pages):
            page_list[x] = x+1
  
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
        currentpagepage =paginator.num_pages
    
    #获取上一页和下一页的值
    prevpage = currentpage - 1
    nextpage = currentpage + 1

    #确保上一页没有超出页面范围，否则分别赋值为1和最大页码数
    if(prevpage < 1):
        prevpage = 1
    if(nextpage > paginator.num_pages):
        nextpage = paginator.num_pages
    pages = {}
    pages['info_list'] = info_list
    pages['page']      = page
    pages['currentpage'] = currentpage
    pages['prevpage'] = prevpage
    pages['nextpage'] = nextpage
    pages['page_list'] = page_list
    return pages


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
				return HttpResponseRedirect('/backend/')
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
@csrf_exempt
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
		nav_name_en = request.POST.get('name_en','')
		title = request.POST.get('title','')
		title_en = request.POST.get('title_en','')
		keywords = request.POST.get('keywords','')
		keywords_en = request.POST.get('keywords_en','')
		description = request.POST.get('description','')
		description_en = request.POST.get('description_en','')
		p_nav = nav.objects.get(id=navId)   #找到父ID】
		p = nav(
			name = nav_name,
			name_en = nav_name_en,
			pid  = p_nav,
			title = title,
			title_en = title_en,
			keywords = keywords,
			keywords_en = keywords_en,
			description = description,
			description_en = description_en,
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
@csrf_exempt
def Twolink(request,template_name):
	if request.is_ajax():
		nav_id = int(request.POST.get('id',''))
		product_nav = nav.objects.filter(id__gt=3,level=1)  
		if nav_id <= 9:          #一级导航id <= 9
			p_id = nav_id        #父导航 id
			s_id = ''  		     #二级导航 id
			product_nav1 = nav.objects.filter(id=nav_id)   #获取当前导航  
			try:
				product_second_nav = nav.objects.filter(pid=product_nav1[0])
			except Exception:
				product_second_nav = None
			try:
				product_third_nav = nav.objects.filter(pid=product_second_nav[0])
			except Exception:
				product_third_nav = None
		else:					 #二级导航以上id >9
			pid = int(request.POST.get('pid',''))                   
			#product_nav = nav.objects.filter(id=p_id)
			p_id = pid     #父导航   id
			# print '*'*20
			s_id = nav_id  #二级导航 id
			try:
				product_second_nav = nav.objects.filter(pid=p_id)     #获取所有二级导航
				product_second_nav1 = nav.objects.filter(id=nav_id)   #获取当前导航 
				product_third_nav = nav.objects.filter(pid=nav_id)
			except Exception:
				product_third_nav = None
		# print p_id
		# print s_id
		return render(request,template_name,{
				'product_nav':product_nav,
				'Pid':p_id,
				'Sid':s_id,
				'product_second_nav':product_second_nav,
				'product_third_nav':product_third_nav,
			}
			)
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：导航联动   应用于 佳易德产品 和  工程应用
#   功能：根据父导航实现 实现二级、三级导航的 联动效果
#   人员：杨凯
#   日期：2014.08.24
# --------------------------------------
@csrf_exempt
def Twolink2(request,template_name):
	if request.is_ajax():
		nav_id = int(request.POST.get('id',''))  #二级id
		pid = int(request.POST.get('pid',''))   #  父id
		product_nav = nav.objects.filter(id=pid)  #获取父导航              
		#product_nav = nav.objects.filter(id=p_id)
		p_id = pid     #父导航   id
		# print '*'*20
		s_id = nav_id  #二级导航 id
		try:
			product_second_nav = nav.objects.filter(pid=p_id)     #获取所有二级导航
			product_second_nav1 = nav.objects.filter(id=nav_id)   #获取当前导航 
			product_third_nav = nav.objects.filter(pid=nav_id)
		except Exception:
			product_third_nav = None
	# print p_id
	# print s_id
	return render(request,template_name,{
			'product_nav':product_nav,
			'Pid':p_id,
			'Sid':s_id,
			'product_second_nav':product_second_nav,
			'product_third_nav':product_third_nav,
		}
		)
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
	lists = news.objects.filter(p_id=2)
	premissions = public_premissions(request)    #权限认证
	public_pages = public_page(request,lists,8)  #分页
	public_pages['list_type_name'] = []      #初始化一个 list
	#for 循环用来获取 文章 相对应的 导航名称
	for menu in lists:
		temp = {}
		temp['p_name'] = nav.objects.get(id=menu.p_id).name  #获取父导航名字
		try:
			temp['s_name'] = nav.objects.get(id=menu.s_id).name  #获取二级导航名字
		except Exception:
			temp['s_name'] = None
		try:
			temp['t_name'] = nav.objects.get(id=menu.t_id).name  #获取三级导航名字
		except Exception:
			temp['t_name'] = None	
		public_pages['list_type_name'].append(temp)
	# 用来 将 info_list 和 导航组合在一起，在模板中循环的时候就可以一一对应
	data = []
	for index in range(len(public_pages['info_list'])):
		data.append({
			'news': public_pages['info_list'][index],
			'navs': public_pages['list_type_name'][index]
			})
	# print '*'*20
	# for item in data:
	# 	print item['news']
	#渲染页面
	# return HttpResponse(currentpage_en)
	return render(request,template_name,{'public_pages':public_pages,'data':data,'premissions':premissions})

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
	# ueditor编辑器初始化（英文版）
	form_en = UEditorForm_en()
	#获取 佳易得产品 一级导航
	product_nav = nav.objects.filter(id=2)  
	#获取 所有二级导航
	try:
		product_second_nav = nav.objects.filter(pid = product_nav[0])
	except Exception:
		product_second_nav = None
	#获取属于当前二级导航的 三级导航
	try:
		product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	except Exception:
		product_third_nav = None

	premissions = public_premissions(request)    #权限认证
	return render(request,template_name,{"form": form,
		"form_en": form_en,
		"product_nav":product_nav,
		"product_second_nav":product_second_nav,
		"product_third_nav":product_third_nav,
		'premissions':premissions})

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
		title_en = request.POST.get('title_en', '')
		remark = request.POST.get('remark','')
		remark_en = request.POST.get('remark_en', '')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		content_en = request.POST.get('content_en', '')
		page_title = request.POST.get('page_title','')
		page_title_en = request.POST.get('page_title_en','')
		page_keywords = request.POST.get('page_keywords','')
		page_keywords_en = request.POST.get('page_keywords_en','')
		page_description = request.POST.get('page_description','')
		page_description_en = request.POST.get('page_description_en','')
		url = request.POST.get('url','')
		url_en = request.POST.get('url_en','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			title_en = title_en,
			remark = remark,
			remark_en = remark_en,
			img = img,
			content = content,
			content_en = content_en,
			page_title = page_title,
			page_title_en = page_title_en,
			page_keywords = page_keywords,
			page_keywords_en = page_keywords_en,
			page_description = page_description,
			page_description_en = page_description_en,
			url = url,
			url_en = url_en,
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
	lists = news.objects.filter(p_id=3)
	premissions = public_premissions(request)    #权限认证
	public_pages = public_page(request,lists,8)  #分页
	public_pages['list_type_name'] = []      #初始化一个 list
	#for 循环用来获取 文章 相对应的 导航名称
	for menu in lists:
		temp = {}
		temp['p_name'] = nav.objects.get(id=menu.p_id).name  #获取父导航名字
		try:
			temp['s_name'] = nav.objects.get(id=menu.s_id).name  #获取二级导航名字
		except Exception:
			temp['s_name'] = None
		try:
			temp['t_name'] = nav.objects.get(id=menu.t_id).name  #获取三级导航名字
		except Exception:
			temp['t_name'] = None	
		public_pages['list_type_name'].append(temp)
	# 用来 将 info_list 和 导航组合在一起，在模板中循环的时候就可以一一对应
	data = []
	for index in range(len(public_pages['info_list'])):
		data.append({
			'news': public_pages['info_list'][index],
			'navs': public_pages['list_type_name'][index]
			})
	# print '*'*20
	# for item in data:
	# 	print item['news']
	#渲染页面
	# return HttpResponse(currentpage_en)
	return render(request,template_name,{'public_pages':public_pages,'data':data,'premissions':premissions})

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
	# ueditor编辑器初始化（英文版）
	form_en = UEditorForm_en()
	#获取 工程应用 一级导航
	product_nav = nav.objects.filter(id=3)  
	#获取 所有二级导航
	try:
		product_second_nav = nav.objects.filter(pid = product_nav[0])
	except Exception:
		product_second_nav = None
	#获取属于当前二级导航的 三级导航
	try:
		product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	except Exception:
		product_third_nav = None
	premissions = public_premissions(request)    #权限认证
	return render(request,template_name,{"form": form,
		"form_en": form_en,
		"product_nav":product_nav,
		"product_second_nav":product_second_nav,
		"product_third_nav":product_third_nav,
		'premissions':premissions})

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
		title_en = request.POST.get('title_en','')
		remark = request.POST.get('remark','')
		remark_en = request.POST.get('remark_en','')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		content_en = request.POST.get('content_en','')
		page_title = request.POST.get('page_title','')
		page_title_en = request.POST.get('page_title_en','')
		page_keywords = request.POST.get('page_keywords','')
		page_keywords_en = request.POST.get('page_keywords_en','')
		page_description = request.POST.get('page_description','')
		page_description_en = request.POST.get('page_description_en','')
		url = request.POST.get('url','')
		url_en = request.POST.get('url_en','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			title_en = title_en,
			remark = remark,
			remark_en = remark_en,
			img = img,
			content = content,
			content_en = content_en,
			page_title = page_title,
			page_title_en = page_title_en,
			page_keywords = page_keywords,
			page_keywords_en = page_keywords_en,
			page_description = page_description,
			page_description_en = page_description_en,
			url = url,
			url_en = url_en,
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
	lists = news.objects.filter(p_id__gt=3)
	premissions = public_premissions(request)    #权限认证
	public_pages = public_page(request,lists,8)  #分页
	public_pages['list_type_name'] = []      #初始化一个 list
	#for 循环用来获取 文章 相对应的 导航名称
	for menu in lists:
		temp = {}
		temp['p_name'] = nav.objects.get(id=menu.p_id).name  #获取父导航名字
		try:
			temp['s_name'] = nav.objects.get(id=menu.s_id).name  #获取二级导航名字
		except Exception:
			temp['s_name'] = None
		try:
			temp['t_name'] = nav.objects.get(id=menu.t_id).name  #获取三级导航名字
		except Exception:
			temp['t_name'] = None	
		public_pages['list_type_name'].append(temp)
	# 用来 将 info_list 和 导航组合在一起，在模板中循环的时候就可以一一对应
	data = []
	for index in range(len(public_pages['info_list'])):
		data.append({
			'news': public_pages['info_list'][index],
			'navs': public_pages['list_type_name'][index]
			})
	# print '*'*20
	# for item in data:
	# 	print item['news']
	#渲染页面
	# return HttpResponse(currentpage_en)
	return render(request,template_name,{'public_pages':public_pages,'data':data,'premissions':premissions})

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
	# ueditor编辑器初始化（英文版）
	form_en = UEditorForm_en()
	#获取  一级导航
	product_nav = nav.objects.filter(id__gt=3,level=1)  
	#获取 所有二级导航
	try:
		product_second_nav = nav.objects.filter(pid = product_nav[0])
	except Exception:
		product_second_nav = None
	#获取属于当前二级导航的 三级导航
	try:
		product_third_nav = nav.objects.filter(pid = product_second_nav[0])
	except Exception:
		product_third_nav = None
	premissions = public_premissions(request)
	return render(request,template_name,{"form": form,
		"form_en": form_en,
		"product_nav":product_nav,
		"product_second_nav":product_second_nav,
		"product_third_nav":product_third_nav,
		'premissions':premissions})

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
		title_en = request.POST.get('title_en','')
		remark = request.POST.get('remark','')
		remark_en = request.POST.get('remark_en','')
		img   = request.FILES.get('img',None)
		content = request.POST.get('content','')
		content_en = request.POST.get('content_en','')
		page_title = request.POST.get('page_title','')
		page_title_en = request.POST.get('page_title_en','')
		page_keywords = request.POST.get('page_keywords','')
		page_keywords_en = request.POST.get('page_keywords_en','')
		page_description = request.POST.get('page_description','')
		page_description_en = request.POST.get('page_description_en','')
		url = request.POST.get('url','')
		url_en = request.POST.get('url_en','')
		p = news(
			p_id = p_id,
			s_id = s_id,
			t_id = t_id,
			title = title,
			title_en = title_en,
			remark = remark,
			remark_en = remark_en,
			img = img,
			content = content,
			content_en = content_en,
			page_title = page_title,
			page_title_en = page_title_en,
			page_keywords = page_keywords,
			page_keywords_en = page_keywords_en,
			page_description = page_description,
			page_description_en = page_description_en,
			url = url,
			url_en = url_en,
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
	premissions = public_premissions(request)    #权限认证
	public_pages = public_page(request,lists,8)  #分页
	#渲染页面
	# return HttpResponse(currentpage_en)
	return render(request,template_name,{'public_pages':public_pages,'premissions':premissions})

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
	# ueditor编辑器初始化（英文版）
	form_en = UEditorForm_en()
	premissions = public_premissions(request)   #权限认证
	return render(request,template_name,{"form": form,"form_en": form_en,'premissions':premissions})

# ======================================
# 	名字：发布招聘信息处理
#   功能：添加招聘信息进数据库
#   人员：杨凯
#   日期：2014.08.26
# --------------------------------------
@csrf_exempt
def job_publish_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		position = request.POST.get('position','')
		content = request.POST.get('content','')
		position_en = request.POST.get('position_en','')
		content_en = request.POST.get('content_en','')
		jobs = job.objects.create(
			position = position,
			content = content,
			position_en = position_en,
			content_en = content_en,
			)
		return HttpResponseRedirect('/backend/job_list/')
	return HttpResponse('请求方法错误...')

# ======================================
# 	名字：删除招聘信息
#   功能：删除招聘信息相对应的数据
#   人员：杨凯
#   日期：2014.08.26
# --------------------------------------
@csrf_exempt
def del_job(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "GET":
		job_id = request.GET.get('id','')
		delJob = job.objects.get(id=job_id)
		delJob.delete()
		premissions = public_premissions(request)   #权限认证
		return render(request, "backend_href.html", {'title':"删除成功 :)", 'href':"message",'premissions':premissions})
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
	premissions = public_premissions(request)    #权限认证
	public_pages = public_page(request,lists,8)  #分页
	#渲染页面
	# return HttpResponse(currentpage_en)
	return render(request,template_name,{'public_pages':public_pages,'premissions':premissions})

# ======================================
# 	名字：留言回复表单处理
#   功能：回复留言信息
#   人员：杨凯
#   日期：2014.08.26
# --------------------------------------
@csrf_exempt
def message_replay_handle(request):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	if request.method == "POST":
		message_id = request.POST.get('id','')
		p = comments.objects.get(id=message_id)
		p.admin = request.user.username
		p.replay_content = request.POST.get('content','')
		p.replay_time = datetime.now() 
		p.save()
		return HttpResponseRedirect('/backend/message_list/')
	return HttpResponse('请求方法错误...')

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
		return render(request, "backend_href.html", {'title':"删除成功 :)", 'href':"message",'premissions':premissions})
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

	userInfos = User.objects.get(is_superuser=1)                         # 获取超级管理员
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
	return HttpResponse('请求方法错误...')

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
	
	if types == 'product':
		edit_type = u'修改佳易得产品'
	elif types == 'project':
		edit_type = u'修给工程应用'
	else:
		edit_type = u'修改资讯'
	premissions = public_premissions(request)

	# ueditor编辑器初始化
	form = UEditorForm()
	# ueditor编辑器初始化
	form_en = UEditorForm_en()

	param = {
		'new':new, 
		'type':types, 
		'form':form,
		'form_en':form_en,
		'p_id_name':p_id_name,
		's_id_name':s_id_name,
		'edit_type':edit_type,
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
@csrf_exempt
def edit_info_handle(request):
	if request.method == "POST":
		ids = request.POST['id']
		types = request.POST['type']
		print '*'*200
		print types
		title = request.POST['title']
		title_en = request.POST['title_en']
		remark = request.POST['remark']
		remark_en = request.POST['remark_en']
		hiddenImg = request.POST['hiddenImg']
		img = request.FILES.get('img', None)
		content = request.POST['content']
		content_en = request.POST['content_en']
		page_title = request.POST.get('page_title','')
		page_title_en = request.POST.get('page_title_en','')
		page_keywords = request.POST.get('page_keywords','')
		page_keywords_en = request.POST.get('page_keywords_en','')
		page_description = request.POST.get('page_description','')
		page_description_en = request.POST.get('page_description_en','')
		url = request.POST.get('url','')
		url_en = request.POST.get('url_en','')

		# 如果没有上传图片
		if not img:
			img = hiddenImg

		# 保存修改
		new = news.objects.get(id = ids)
		new.title = title
		new.title_en = title_en
		new.remark = remark
		new.remark_en = remark_en
		new.img = img
		new.content = content
		new.content_en = content_en
		page_title = page_title,
		page_title_en = page_title_en,
		page_keywords = page_keywords,
		page_keywords_en = page_keywords_en,
		page_description = page_description,
		page_description_en = page_description_en,
		url = url,
		url_en = url_en,
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
@csrf_exempt
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
@csrf_exempt
def navigation_edit_handle(request):
	if request.method == "POST":
		ids = request.POST['id']
		name = request.POST['name']
		name_en=request.POST['name_en']
		title = request.POST.get('title','')
		title_en = request.POST.get('title_en','')
		keywords = request.POST.get('keywords','')
		keywords_en = request.POST.get('keywords_en','')
		description = request.POST.get('description','')
		description_en = request.POST.get('description_en','')
		navs = nav.objects.get(id = ids)
		navs.name = name
		navs.name_en=name_en
		navs.title = title
		navs.title_en = title_en
		navs.keywords = keywords
		navs.keywords_en = keywords_en
		navs.description = description
		navs.description = description_en
		navs.save()

		return render(request, "backend_href.html", {'title':'修改成功 :)', 'href':'navigation'})
	else:
		return render(request, "backend_href.html", {'title':'修改失败，请重试 :(', 'href':'navigation'})

# ======================================
# 	名字：招聘修改
#   功能：招聘修改
#   人员：黄晓佳
#   日期：2014.08.26
# --------------------------------------
@csrf_exempt
def job_edit(request, template_name):
	if request.method == "GET":
		ids = request.GET.get('id', '')

	# ueditor编辑器初始化
	form = UEditorForm()
	jobs = job.objects.get(id = ids)
	premissions = public_premissions(request)
	return render(request, template_name, {'job': jobs, 'form': form ,'premissions':premissions})

# ======================================
# 	名字：招聘修改表单提交
#   功能：招聘修改
#   人员：黄晓佳
#   日期：2014.08.26
# --------------------------------------
@csrf_exempt
def job_edit_handle(request):
	if request.method == "POST":
		ids = request.POST.get('id', '')
		position = request.POST['position']
		position_en = request.POST.get('position_en','')
		content = request.POST['content']
		content_en = request.POST.get('content_en',
			'')
		jobs = job.objects.get(id = ids)
		jobs.position = position
		jobs.postition_en = position_en
		jobs.content = content
		jobs.content_en = content_en
		jobs.save()

		return render(request, "backend_href.html", {'title':"修改成功 :)", 'href':"job"})
	else:
		return render(request, "backend_href.html", {'title':"修改失败，请重试 :(", 'href':"job"})

# ======================================
# 	名字：管理员修改密码
#   功能：修改密码页面显示
#   人员：黄晓佳
#   日期：2014.08.27
# --------------------------------------
def admin_changePwd(request, template_name):
	premissions = public_premissions(request)
	return render(request, template_name, {'premissions':premissions})

# ======================================
# 	名字：管理员修改密码表单处理
#   功能：修改密码
#   人员：黄晓佳
#   日期：2014.08.27
# --------------------------------------
@csrf_exempt
def admin_changePwd_handle(request):
	if request.method == "POST":
		oldPwd = request.POST['oldPwd']            # 旧密码
		newPwd = request.POST['newPwd']            # 新密码

		# 旧密码如果一致，则修改密码
		if check_password(oldPwd, request.user.password): 
			users = User.objects.get(username = request.user.username)
			users.password = make_password(newPwd, None, 'pbkdf2_sha256')
			users.save()
			return render(request, "backend_href.html", {'title':"修改密码成功 :)", 'href':"home"})
		else:
			return render(request, "backend_href.html", {'title':"旧密码输入不一致 :(", 'href':"home"})

	return render(request, "backend_href.html", {'title':"请求失误 :(", 'href':"home"})

# ======================================
# 	名字：产品优势列表
#   功能：列表
#   人员：黄晓佳
#   日期：2014.09.06
# --------------------------------------
def advantages_list(request, template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	advantangeslist = advantages.objects.all()
	premissions = public_premissions(request)
	return render(request,template_name,{'advantangeslist':advantangeslist,'premissions':premissions})

# ======================================
# 	名字：产品优势修改
#   功能：修改
#   人员：黄晓佳
#   日期：2014.09.06
# --------------------------------------
@csrf_exempt
def advantages_edit(request, template_name):
	if not request.user.is_authenticated():
		return redirect('/backend/login/')
	premissions = public_premissions(request)

	if request.method == "GET":
		ids = request.GET.get('id', '')
		adv = advantages.objects.get(id = ids)
		return render(request,template_name,{'premissions':premissions, 'adv':adv})

# ======================================
# 	名字：产品优势修改表单处理
#   功能：修改表单处理
#   人员：黄晓佳
#   日期：2014.09.06
# --------------------------------------
@csrf_exempt
def advantages_edit_handle(request):
	if request.method == "POST":
		ids = request.POST.get('id', '')
		problem = request.POST['problem']
		big_title = request.POST['big_title']
		big_title_en = request.POST['big_title_en']
		title1 = request.POST['title1']
		title1_en = request.POST['title1_en']
		title2 = request.POST['title2']
		title2_en = request.POST['title2_en']
		solution1 = request.POST['solution1']
		solution2 = request.POST['solution2']
		solution3 = request.POST['solution3']
		solution4 = request.POST['solution4']
		problem_en = request.POST['problem_en']
		solution1_en = request.POST['solution1_en']
		solution2_en = request.POST['solution2_en']
		solution3_en = request.POST['solution3_en']
		solution4_en = request.POST['solution4_en']

		adv = advantages.objects.get(id = ids)
		adv.problem = problem
		adv.big_title = big_title
		adv.big_title_en = big_title_en
		adv.title1 = title1
		adv.title1_en = title1_en
		adv.title2 = title2
		adv.title2_en = title2_en
		adv.solution1 = solution1
		adv.solution2 = solution2
		adv.solution3 = solution3
		adv.solution4 = solution4
		adv.problem_en = problem_en
		adv.solution1_en = solution1_en
		adv.solution2_en = solution2_en
		adv.solution3_en = solution3_en
		adv.solution4_en = solution4_en
		adv.save()

		return render(request, "backend_href.html", {'title':"修改产品优势成功 :)", 'href':"advantages"})

	return render(request, "backend_href.html", {'title':"请求失误 :(", 'href':"advantages"})

# # ======================================
# # 	名字：各个页面关键字描述添加
# #   功能：页面关键字添加
# #   人员：杨凯
# #   日期：2014.09.12
# # --------------------------------------
# def page_keyword_list(request,template_name):
# 	keyword_list = page_keywords.objects.all()
# 	return render(request,template_name,{'keyword_list':keyword_list})

# # ======================================
# # 	名字：各个页面关键字描述添加
# #   功能：页面关键字添加
# #   人员：杨凯
# #   日期：2014.09.12
# # --------------------------------------
# def page_keyword_edit(request,template_name):
# 	keyword_list = nav.objects.filter(level=1)
# 	return render(request,template_name,{'keyword_list':keyword_list})

# # ======================================
# # 	名字：各个页面关键字描述添加处理
# #   功能：页面关键字添加表单处理
# #   人员：杨凯
# #   日期：2014.09.12
# # --------------------------------------
# def page_keyword_edit_handle(request):
# 	if method.request == "POST":
# 		nav_id = request.POST.get('id','')
# 		title = request.POST.get('title','')
# 		title_en = request.POST.get('title_en','')
# 		keywords = request.POST.get('keywords','')
# 		keywords_en = request.POST.get('keywords_en','')
# 		description = request.POST.get('description','')
# 		description_en = request.POSTE.get('descrption_en','')
# 		p = nav(
# 			nav_id = nav_id,
# 			title = title,
# 			title_en = title_en,
# 			keywords = keywords,
# 			keywords_en = keywords_en,
# 			description = description,
# 			description_en =description_en,
# 		)
# 		p.save()
# 		return HttpResponseRedirect('/backend/page__keyword_list/')