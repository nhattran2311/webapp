from django.urls import include, path
from rest_framework import routers
from blog.api.views import view_post, view_post_detail
from blog.api import views
from rest_framework.urlpatterns import format_suffix_patterns




router = routers.DefaultRouter()

urlpatterns =[
    path('', include(router.urls)),
    path('view_post/', view_post, name='view_post'),
    path('view_post_detail/<int:pk>/', view_post_detail, name='view_post_detail'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)