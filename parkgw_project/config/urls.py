"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
# sns 로그인/로그아웃을 위해 사용되는 패키지
from django.contrib.auth import views as auth_views
from parkgw_app import views

urlpatterns = [
    path('prod/', include('parkgw_app.urls')),
    path('admin/', admin.site.urls),
    # 일parkgw_app의 view 함수
    path('',views.login_logout, name='login_logout'),
    
    # sns 로그인/로그아웃을 위해 사용되는 함수
    # 최초 sns로그인 시 사용되는 urls 패턴
    path('accounts', include('allauth.urls')),
    # sns 로그인 이후 이동할 페이지
    path('accounts/login/',auth_views.LoginView.as_view(template_name='parkgw_app/prod/prod_list.html'),name='login'),
    # sns 로그아웃 후 이동할 페이지
    path('accounts/logout/',auth_views.LogoutView.as_view(), name='logout'),
    
]

