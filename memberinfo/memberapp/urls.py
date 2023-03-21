
from django.urls import path

from . import views


# url을 만들어서 views.py의 함수와 매핑
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든것은 
    #  views.py의 index() 함수를 자동으로 호풀 실행해
    # 함수 내부의 내용을 리턴(응답)해 준다.
    # http://127.0.0.1:8000/practice/xxxxx
    
    
    path('list/', views.mem_list),
    path('detail/', views.mem_detail),
    path('insert/', views.mem_insert),
    path('insert_save/', views.mem_insert_save),
    path('update/', views.mem_update),
    path('update_save/', views.mem_update_save),
]
