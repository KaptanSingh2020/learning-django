from django.conf.urls import url
from .views import post_list, post_detail, PostList

# urlpatterns = [
#     url(r'^$', post_list, name='blog_post_list'),
#     url(r'ˆ(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', 
#         post_detail, 
#         name='blog_post_detail'),
# ]

# This code uses class-based views. 
urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog_post_list'),
    url(r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', 
        post_detail, 
        name='blog_post_detail'),
]