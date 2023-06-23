from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),#we named this blog-home so that it would not coinciede with any other path
    
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update')
    ,path('about/',views.about,name='blog-about'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
     path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
     path('user/<str:username>/',UserPostListView.as_view(),name='user-post')    
]
# looking for html file @ <app_name>/<model_name>_<view_type> 