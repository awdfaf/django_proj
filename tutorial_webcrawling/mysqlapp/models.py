from django.db import models
from django.db.models.fields import CharField, IntegerField
# Create your models here.
class Cart(models.Model) : 
    cart_no = CharField(primary_key=True, max_length=13, null=False)
    cart_prod = CharField(max_length=30, null=False)
    cart_member = CharField(max_length=15, null=False)
    cart_qty = IntegerField(max_length=10, null=False)
    
    ### DB 속성 정의 : 클래스이름 및 변수이름 변경 불가.. 
    class Meta :
        ### 사용할 실제 테이블 이름 지정
        db_table = "cart"
        ### 현재 model을 사용할 앱 지정
        app_label = "mysqlapp"
        ### 테이블이 실제 DB에 존재하면 False(보통 False 사용)
        managed = False

class Member(models.Model) : 
    mem_id = CharField(primary_key=True, max_length=15, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=10, null=False)
        
    ### DB 속성 정의 : 클래스이름 및 변수이름 변경 불가.. 
    class Meta :
        ### 사용할 실제 테이블 이름 지정
        db_table = "member"
        ### 현재 model을 사용할 앱 지정
        app_label = "mysqlapp"
        ### 테이블이 실제 DB에 존재하면 False(보통 False 사용)
        managed = False