from django.db import models
from django.db.models.fields import CharField, IntegerField
# Create your models here.

class Lprod(models.Model):
    lprod_id = IntegerField(max_length=20, null=False)
    lprod_gu = CharField(primary_key=True, max_length=20, null=False)
    lprod_nm = CharField(max_length=20, null=False)
    

    class Meta :
    ### 사용할 실제 테이블 이름 지정
        db_table = "lprod"
    ### 현재 model을 사용할 앱 지정
        app_label = "practiceapp"
    ### 테이블이 실제 DB에 존재하면 False(보통 false를 사용)
        managed = False