
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
urlpatterns = [
    path('', include('blog.urls')),
    path('crawldata/', include('crawldata.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/',include('blog.api.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)