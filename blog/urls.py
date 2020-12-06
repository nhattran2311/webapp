from django.urls import path,include
from . import views
# from ckeditor.widgets import CKEditorWidget
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
urlpatterns = [
    path('',views.home, name='blog-home'),
    path('article/',PostListView.as_view(), name='blog-article'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),#pk la primary key
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),#pk la primary key
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),#pk la primary key
    path('model_canvas/',views.model_canvas, name='blog-threejs-canvas'),
    path('model_periodic/',views.model_periodic, name='blog-threejs-periodic'),
]