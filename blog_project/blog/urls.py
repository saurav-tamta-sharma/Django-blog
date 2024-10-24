from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('post/new/', views.create_post, name='post-create'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    # path('create/', views.create_post, name='blog-create'),
]
