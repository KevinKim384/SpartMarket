from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class NewUser(models.Model):
    id = models.TextField(primary_key=True)
    password = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add = True) # add는 생성때 추가
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    
class Users(AbstractUser):
    pass