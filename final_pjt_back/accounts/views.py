from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from products.models import Deposit, Saving
import random


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    
@api_view(['POST'])
def permission(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        res = {
            'is_super': user.is_superuser,
            'is_staff': user.is_staff,
            'pk': user.pk
        }
        return Response(res)



@api_view(['GET'])
def dummy_user_deposit_saving(request):
    API_KEY = settings.PRODUCT_API_KEY
    users = User.objects.all()
    deposit_products = list(Deposit.objects.all())
    saving_products = list(Saving.objects.all())
    for user in users:
        random_deposit_products = random.sample(deposit_products, random.randint(0, 3))
        random_saving_products = random.sample(saving_products, random.randint(0, 3))
        user.deposit_products.add(*random_deposit_products)
        user.saving_products.add(*random_saving_products)
    return Response({'msg': 'okay'})