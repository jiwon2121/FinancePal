from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from .serializers import DepositSerializer, DepositOptionSerializer, SavingSerializer, SavingOptionSerializer
from .models import Deposit, DepositOption, Saving, SavingOption
# from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

'''
예금 상품 조회
'''
# @staff_member_required
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.PRODUCT_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for obj in response.get('result').get("baseList"):
        if Deposit.objects.filter(pk=obj.get('fin_prdt_cd')).exists():
            instance = Deposit.objects.get(pk=obj.get('fin_prdt_cd'))
            products_serializer = DepositSerializer(instance=instance, data=obj, partial=True)
        else:
            products_serializer = DepositSerializer(data=obj)
        if products_serializer.is_valid(raise_exception=True):
            products_serializer.save()
    for obj in response.get('result').get('optionList'):
        product = Deposit.objects.get(pk=obj.get('fin_prdt_cd'))
        if DepositOption.objects.filter(product=obj.get('fin_prdt_cd'), save_trm=obj.get('save_trm')).exists():
            instance = DepositOption.objects.get(product=obj.get('fin_prdt_cd'), save_trm=obj.get('save_trm'))
            options_serializer = DepositOptionSerializer(instance=instance, data=obj, partial=True)
        else:
            options_serializer = DepositOptionSerializer(data=obj)
        if options_serializer.is_valid(raise_exception=True):
            options_serializer.save(product=product)
    return Response({'message':'okay'})


@api_view(['GET'])
def deposits(request):
    if request.method == "GET":
        products = Deposit.objects.all()
        serializer = DepositSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def deposit_detail(request, pk):
    if request.method == "GET":
        product = Deposit.objects.get(pk=pk)
        serializer = DepositSerializer(product)
        return Response(serializer.data)
    

'''
적금 상품 조회
'''
@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.PRODUCT_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for obj in response.get('result').get("baseList"):
        if Saving.objects.filter(pk=obj.get('fin_prdt_cd')).exists():
            instance = Saving.objects.get(pk=obj.get('fin_prdt_cd'))
            products_serializer = SavingSerializer(instance=instance, data=obj, partial=True)
        else:
            products_serializer = SavingSerializer(data=obj)
        if products_serializer.is_valid(raise_exception=True):
            products_serializer.save()
    for obj in response.get('result').get('optionList'):
        product = Saving.objects.get(pk=obj.get('fin_prdt_cd'))
        if SavingOption.objects.filter(rsrv_type=obj.get('rsrv_type'), product=obj.get('fin_prdt_cd'), save_trm=obj.get('save_trm')).exists():
            instance = SavingOption.objects.get(rsrv_type=obj.get('rsrv_type'), product=obj.get('fin_prdt_cd'), save_trm=obj.get('save_trm'))
            options_serializer = SavingOptionSerializer(instance=instance, data=obj, partial=True)
        else:
            options_serializer = SavingOptionSerializer(data=obj)
        if options_serializer.is_valid(raise_exception=True):
            options_serializer.save(product=product)
    return Response({'message':'okay'})


@api_view(['GET'])
def savings(request):
    if request.method == "GET":
        products = Saving.objects.all()
        serializer = SavingSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def saving_detail(request, pk):
    # pk = fin_prdt_cd
    if request.method == "GET":
        product = Saving.objects.get(pk=pk)
        serializer = SavingSerializer(product)
        return Response(serializer.data)
