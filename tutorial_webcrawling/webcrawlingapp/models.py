from django.db import models
from django.db.models.fields import CharField, IntegerField
# Create your models here.

class Melon(models.Model):
    no = IntegerField(primary_key=True, max_length=13, null=False)
    title = CharField(max_length=100, null=False)
    singer = CharField(max_length=100, null=False)
    
    class Meta:
        db_table = "melon"
        app_label = "webcrawlingapp"
        managed = False