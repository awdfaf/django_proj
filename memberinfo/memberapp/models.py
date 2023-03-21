from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField
# Create your models here.

class Member(models.Model):
    mem_id = CharField(primary_key=True, max_length=20, null=False)
    mem_pass = CharField( max_length=20, null=False)
    mem_name = CharField(max_length=20, null=False)
    mem_bir = DateTimeField(max_length=20, null=False)
    mem_add1 = CharField(max_length=60, null=False)
    mem_add2 = CharField(max_length=50, null=False)
    mem_hp = CharField(max_length=20, null=False)
    mem_regno1 = CharField(max_length=20, null=False)
    mem_regno2 = CharField(max_length=20, null=False)
    mem_zip = CharField(max_length=20, null=False)
    mem_hometel = CharField(max_length=20, null=False)
    mem_mail = CharField(max_length=20, null=False)
    mem_comtel = CharField(max_length=20, null=False)
    

    class Meta :
    ### 사용할 실제 테이블 이름 지정
        db_table = "member"
    ### 현재 model을 사용할 앱 지정
        app_label = "memberapp"
    ### 테이블이 실제 DB에 존재하면 False(보통 false를 사용)
        managed = False