from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.conf import settings

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
    max_length=255
    )
    address = serializers.CharField(
        allow_blank=True,
        max_length = 255,
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    gender = serializers.BooleanField()
    salary = serializers.IntegerField(required=False)
    balance = serializers.IntegerField(required=False)

    # financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)

    # deposit_products = models.ManyToManyField()
    # saving_products = models.ManyToManyField()
    # profile_img = models.ImageField(blank=True)
    # follower = models.ManyToManyField()

    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'email': self.validated_data.get('email', ''),
        'first_name': self.validated_data.get('first_name', ''),
        'last_name': self.validated_data.get('last_name', ''),
        'password1': self.validated_data.get('password1', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'address': self.validated_data.get('address', ''),
        'birth_date': self.validated_data.get('birth_date', ''),
        'gender': self.validated_data.get('gender', ''),
        'balance': self.validated_data.get('balance', ''),
        'salary': self.validated_data.get('salary', ''),
        # 'financial_products': self.validated_data.get('financial_products', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'nickname', 'address', 'birth_date', 'gender', 'salary', 'balance', 'deposit_products', 'saving_products')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'birth_date', 'gender', 'salary', 'balance')