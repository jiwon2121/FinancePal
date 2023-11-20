from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from .serializers import ExchangeRateSerializer
from .models import ExchangeRate
# from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# @staff_member_required
@api_view(['GET'])
def save(request):
    api_key = settings.EXCHANGE_RATE_API_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'
    response = requests.get(url).json()
    for obj in response:
        if obj.get('cur_unit').endswith('(100)'):
            obj = {
                'cur_unit': obj.get('cur_unit')[-5:],
                'ttb': str(round(float(obj.get('ttb')) * 0.01), 2),
                'tts': str(round(float(obj.get('tts')) * 0.01, 2)),
                'deal_bas_r': str(round(float(obj.get('deal_bas_r')) * 0.01, 2)),
                'bkpr': str(round(float(obj.get('bkpr')) * 0.01, 2)),
                'yy_efee_r': obj.get('yy_efee_r'),
                'ten_dd_efee_r': obj.get('ten_dd_efee_r'),
                'kftc_bkpr': str(round(int(obj.get('ttb')) * 0.01), 2),
                'kftc_deal_bas_r': str(round(float(obj.get('kftc_deal_bas_r')) * 0.01, 2)),
                'cur_nm': obj.get('cur_nm'),
            }
        if ExchangeRate.objects.filter(pk=obj.get('cur_unit')).exists():
            instance = ExchangeRate.objects.get(pk=obj.get('cur_unit'))
            serializer = ExchangeRateSerializer(instance=instance, data=obj, partial=True)
        else:
            serializer = ExchangeRateSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
    return Response({'message':'okay'})


@api_view(['GET'])
def all(request):
    data = ExchangeRate.objects.all()
    serializer = ExchangeRateSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def by_country(request, pk):
    data = ExchangeRate.objects.get(pk=pk)
    serializer = ExchangeRateSerializer(data)
    return Response(serializer.data)