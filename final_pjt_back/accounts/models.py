from django.db import models
from products.models import Deposit, Saving
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True)
    birth_date = models.DateField(blank=True)
    gender = models.BooleanField(null=True, default=0) # true: 남자, false: 여자
    salary = models.IntegerField()
    balance = models.IntegerField()
    deposit_products = models.ManyToManyField(to=Deposit, blank=True)
    saving_products = models.ManyToManyField(to=Saving, blank=True)


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        address = data.get("address")
        birth_date = data.get("birth_date")
        gender = data.get("gender")
        salary = data.get("salary")
        balance = data.get("balance")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if address:
            user.address = address
        if birth_date:
            user.birth_date = birth_date
        if gender:
            user.gender = gender
        if salary:
            user.salary = salary
        if balance:
            user.balance = balance
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
        # Ability not to commit makes it easier to derive from
        # this adapter by adding
            user.save()
        return user
