from django.conf.urls import url

from .views import tag_detail, startup_detail, tag_create, StartupList, TagList, TagCreate

urlpatterns = [
    url(r'^$', StartupList.as_view(), name='organizer_startup_list'),
    #url(r'^tag/create/$', tag_create, name='organizer_tag_create'),
    url(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
    #url(r'^startup/$', startup_list, name='organizer_startup_list'),
    url(r'ˆstartup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'), 
    url(r'^tag/$', TagList.as_view(), name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
]