from django.db import models
#AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

# Create your models here.
