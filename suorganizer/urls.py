from django.conf.urls import include, url
from django.contrib import admin

from organizer.views import tag_detail
from .views import redirect_root
from organizer import urls as organizer_urls
from blog import urls as blog_urls
from django.contrib.flatpages import urls as flatpages_urls
from user import urls as user_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'suorganizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(organizer_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^user/', include(user_urls, app_name='user', namespace='dj-auth')),
]
