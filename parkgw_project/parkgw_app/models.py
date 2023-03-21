from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField
# Create your models here.

class Prod(models.Model):
    prod_id = CharField(primary_key=True, max_length=30, null=False)
    prod_name = CharField( max_length=40, null=False)
    prod_lgu = CharField(max_length=4, null=False)
    prod_buyer = CharField(max_length=6, null=False)
    prod_cost = IntegerField(max_length=10, null=False)
    prod_price = IntegerField(max_length=10, null=False)
    prod_sale = IntegerField(max_length=10, null=False)
    prod_outline = CharField(max_length=50, null=False)
    prod_img = CharField(max_length=40, null=False)
    prod_totalstock = IntegerField(max_length=10, null=False)
    prod_properstock = IntegerField(max_length=10, null=False)

    class Meta :
    ### 사용할 실제 테이블 이름 지정
        db_table = "prod"
    ### 현재 model을 사용할 앱 지정
        app_label = "parkgw_app"
    ### 테이블이 실제 DB에 존재하면 False(보통 false를 사용)
        managed = False