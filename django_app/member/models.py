from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    pass

class MyUser(AbstractBaseUser):
    # 기본값
    # password
    # last_login
    # is_active
    username = models.CharField(max_length=40, unique=True)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

