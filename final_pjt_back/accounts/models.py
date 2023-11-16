from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True)
    # deposit_products = models.ManyToManyField()
    # saving_products = models.ManyToManyField()
    birth_date = models.DateField()
    gender = models.BooleanField() # true: 남자, false: 여자
    # profile_img = models.ImageField(blank=True)
    salary = models.IntegerField()
    balance = models.IntegerField()
    # follower = models.ManyToManyField()