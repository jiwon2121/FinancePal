from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from products.models import Deposit, Saving
from products.serializers import DepositSerializer, SavingSerializer, DepositOptionSerializer, SavingOptionSerializer
import random
import pandas as pd
import datetime


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        user_serializer = ProfileSerializer(user)
        deposit_products = user.deposit_products
        saving_products = user.saving_products
        return Response(user_serializer.data)
    
    
@api_view(['POST'])
def permission(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        res = {
            'is_super': user.is_superuser,
            'is_staff': user.is_staff,
        }
        return Response(res)



@api_view(['GET'])
def dummy_user_deposit_saving(request):
    users = User.objects.all()
    deposit_products = list(Deposit.objects.all())
    saving_products = list(Saving.objects.all())
    for user in users:
        if user.deposit_products.exists() or user.saving_products.exists():
            continue
        random_deposit_products = random.sample(deposit_products, random.randint(0, 3))
        random_saving_products = random.sample(saving_products, random.randint(0, 3))
        user.deposit_products.add(*random_deposit_products)
        user.saving_products.add(*random_saving_products)
    return Response({'msg': 'okay'})


@api_view(['GET'])
def recommend_by_profile(request, username):
    user = User.objects.get(username=username)
    def calc_age(birthdate):
        today = datetime.datetime.today()
        birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
        age = today.year-birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    user_age = calc_age(str(user.birth_date))
    deposit_products = user.deposit_products
    saving_products = user.saving_products
    deposit_serializer = DepositSerializer(deposit_products, many=True)
    saving_serializer = SavingSerializer(saving_products, many=True)
    return Response({'deposit_products': deposit_serializer.data, 'saving_products': saving_serializer.data})
    


@api_view(['GET'])
def recommend_by_portfolio(request):
    pass