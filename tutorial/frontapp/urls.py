
from django.urls import path

from . import views


# url을 만들어서 views.py의 함수와 매핑
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든것은 
    # frontapp의 views.py의 index() 함수를 자동으로 호출 실행해
    # 함수 내부의 내용을 리턴(응답)해 준다.
    # http://127.0.0.1:8000/front/xxxxx
    
    path('blog/', views.blog),
    path('about_me/', views.about_me),
    path('index_css/', views.index_css),
    path('index_css2/', views.index_css2),
    path('index_css3/', views.index_css3),
    path('index_javascript1/', views.index_javascript1),
    path('index_javascript2/', views.index_javascript2),
    path('index_bootstrap1/', views.index_bootstrap1),
    path('login_form/', views.login_form),
    path('login_form_check/', views.login_form_check),
    
    
    
    path('hello/', views.hello),
    path('sample/', views.sample),
    path('index/', views.index),
    path('', views.index),
    
]