#coding: utf-8
import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^backend/', include('backend.urls')),		    # 后台
    url(r'^ueditor/', include('DjangoUeditor.urls' )),  # ueditor编辑器
    url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.PROJECT_PATH}),                                               #配置media的url
)

# ueditor编辑器显示图片
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
