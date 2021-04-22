"""Dokumentaris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from tutorial.views import index
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('tutorial.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'tutorial.views.custom_page_not_found_view'
handler500 = 'tutorial.views.custom_error_view'
handler403 = 'tutorial.views.custom_permission_denied_view'
handler400 = 'tutorial.views.custom_bad_request_view'
