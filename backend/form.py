# coding:utf8
from django import forms
from DjangoUeditor.forms import UEditorField
	
# ueditor编辑器
class UEditorForm(forms.Form):
	content = UEditorField(u"", 
		initial  = "",
		toolbars = "full", 
		width    = "100%", 
		height   = 350, 
		settings = {"maximumWords" : 10000,
				    "scaleEnabled" : 1,
				    "elementPathEnabled" : 0
				    },
		imagePath= "")

# ueditor编辑器（英文版）
class UEditorForm_en(forms.Form):
	content_en = UEditorField(u"", 
		initial  = "",
		toolbars = "full", 
		width    = "100%", 
		height   = 300, 
		settings = {"maximumWords" : 10000,
				    "scaleEnabled" : 1,
				    "elementPathEnabled" : 0
				    },
		imagePath= "")
	
#登陆验证
class loginForm(forms.Form):
	username = forms.CharField(max_length=20,required=True,error_messages={'required':u'账号不能为空'})
	password = forms.CharField(max_length=20,required=True,error_messages={'required':u'密码不能为空'})


#添加管理员
class adminForm(forms.Form):
	username = forms.CharField(max_length=20,required=True,error_messages={'required':u'账号不能为空'})
	first_name = forms.CharField(max_length=20,required=True,error_messages={'required':u'管理员姓名不能为空'})
	password = forms.CharField(max_length=20,required=True,error_messages={'required':u'密码不能为空'})
	password2 = forms.CharField(max_length=20,required=True,error_messages={'required':u'两次密码输入不一致'})

#编辑管理员
class edit_user_Form(forms.Form):
	username = forms.CharField(max_length=20,required=True,error_messages={'required':u'账号不能为空'})
	first_name = forms.CharField(max_length=20,required=True,error_messages={'required':u'密码不能为空'})