"""askme URL Configuration

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
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('ask/', views.new_question_page, name='ask'),
    path('login/', views.login_page, name='login'),
    path('question/<int:pk>/', views.question_page, name='question'),
    path('signup/', views.signup_page, name='signup'),
    path('settings/', views.settings_page, name='settings'),
    path('tag/<str:tag_name>/', views.tag_page, name='tag'),
    path('hot/', views.hot_questions_page, name='hot'),
    path('', views.index, name='root')
]
