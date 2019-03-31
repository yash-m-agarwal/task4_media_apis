"""image_apis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from apis import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^images/$', views.all_images, name='all_images'),
    url(r'^image/(?P<pk>\d+)/$', views.image_view, name='image_view'),
    url(r'^image/new$', views.new_upload, name='new_upload'),
    url(r'^image/search_name$', views.find_image_by_name, name='find_image_by_name'),
    url(r'^image/(?P<username>[\w.@+-]+)/$', views.images_by_name, name='images_by_name'),
    url(r'^image/(?P<pk>\d+)/update/$', views.update_image, name='update_image'),
    url(r'^image/(?P<pk>\d+)/delete/$', views.delete_image, name='delete_image'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
