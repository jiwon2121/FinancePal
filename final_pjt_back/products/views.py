from django.shortcuts import render
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
    for li in response.get('result').get("baseList"):
        products = {
            'dcls_month': li.get('dcls_month'),
            'fin_co_no': li.get('fin_co_no'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_way': li.get('join_way'),
            'mtrt_int': li.get('mtrt_int'),
            'spcl_cnd': li.get('spcl_cnd'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'etc_note': li.get('etc_note'),
            'max_limit': li.get('max_limit'),
            'dcls_strt_day': li.get('dcls_strt_day'),
            'dcls_end_day': li.get('dcls_end_day'),
            'fin_co_subm_day': li.get('fin_co_subm_day'),
        }

        products_serializer = DepositSerializer(data=products)
        if products_serializer.is_valid(raise_exception=True):
            products_serializer.save()

    for li in response.get('result').get('optionList'):
        options = {
            'intr_rate_type': li.get('intr_rate_type'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'save_trm': li.get('save_trm'),
            'intr_rate': li.get('intr_rate') if li.get('intr_rate') != None else -1,
            'intr_rate2': li.get('intr_rate2'),
        }

        product = Deposit.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
        options_serializer = DepositOptionSerializer(data=options)

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
    # pk = fin_prdt_cd
    if request.method == "GET":
        product = Deposit.objects.get(pk=pk)
        detail = DepositSerializer(product)
        options = DepositOption.objects.filter(product=pk)

        options_list = []
        for option in options:
            option_serializer = DepositOptionSerializer(option)
            options_list.append(option_serializer.data)
        serializer = {
            'detail': detail.data,
            'options': options_list,
        }
        return Response(serializer)
    

'''
적금 상품 조회
'''
@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.PRODUCT_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response.get('result').get("baseList"):
        products = {
            'dcls_month': li.get('dcls_month'),
            'fin_co_no': li.get('fin_co_no'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_way': li.get('join_way'),
            'mtrt_int': li.get('mtrt_int'),
            'spcl_cnd': li.get('spcl_cnd'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'etc_note': li.get('etc_note'),
            'max_limit': li.get('max_limit'),
            'dcls_strt_day': li.get('dcls_strt_day'),
            'dcls_end_day': li.get('dcls_end_day'),
            'fin_co_subm_day': li.get('fin_co_subm_day'),
        }

        products_serializer = SavingSerializer(data=products)
        if products_serializer.is_valid(raise_exception=True):
            products_serializer.save()

    for li in response.get('result').get('optionList'):
        options = {
            'intr_rate_type': li.get('intr_rate_type'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'rsrv_type': li.get('rsrv_type'),
            'rsrv_type_nm': li.get('rsrv_type_nm'),
            'save_trm': li.get('save_trm'),
            'intr_rate': li.get('intr_rate') if li.get('intr_rate') != None else -1,
            'intr_rate2': li.get('intr_rate2'),
        }

        product = Saving.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
        options_serializer = SavingOptionSerializer(data=options)

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
