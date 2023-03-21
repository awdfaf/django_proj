
from django.urls import path

from . import views


# url을 만들어서 views.py의 함수와 매핑
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든것은 
    # views.py의 index() 함수를 자동으로 호출 실행해
    # 함수 내부의 내용을 리턴(응답)해 준다.
    # http://127.0.0.1:8000/second/xxxxx
    
    path('test/', views.test),
    path('cart_list/', views.cart_list),
    path('cart_view/', views.cart_view),
    path('cart_insert_form/', views.cart_insert_form),
    path('cart_insert/', views.cart_insert),
    path('cart_update_view/', views.cart_update_view),
    path('cart_update/', views.cart_update),
    path('cart_delete/', views.cart_delete),
    
    path('login_form/', views.login_form),
    path('login/', views.login),
    path('logout/', views.logout),
    
]
