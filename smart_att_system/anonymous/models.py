from django.db import models

# Create your models here.
class user_master(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    mobile=models.CharField(max_length=40)
    role_name=models.CharField(max_length=40)
    status=models.CharField(max_length=40)
    remark=models.CharField(max_length=40)