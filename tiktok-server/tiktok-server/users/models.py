from django.db import models

from django.contrib.auth.models import AbstractBaseUser, User, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    name= models.CharField(max_length=50, default='')
    username=models.CharField(max_length=50, default='')
    last_name= models.CharField(max_length=60, default='')
    password=models.CharField(max_length=60, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

