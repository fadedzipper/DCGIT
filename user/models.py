from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 已有属性
    # id
    # password
    # last_login
    # is_superuser
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    GENDER = ((1,'男'),(2,'女'))
    tel = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    gender = models.IntegerField(choices=GENDER,default=1)
    info = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ('user_management','用户管理'),
            ('group_management','角色管理'),
            ('permission_management', '权限管理'),

        )

