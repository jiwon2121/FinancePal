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
        if ExchangeRate.objects.filter(pk=obj.get('cur_unit')).exists():
            exchange_rate = ExchangeRate.objects.get(pk=obj['cur_unit'])
            exchange_rate.cur_unit = obj.get('cur_unit')
            exchange_rate.ttb = obj.get('ttb')
            exchange_rate.tts = obj.get('tts')
            exchange_rate.deal_bas_r = obj.get('deal_bas_r')
            exchange_rate.bkpr = obj.get('bkpr')
            exchange_rate.yy_efee_r = obj.get('yy_efee_r')
            exchange_rate.ten_dd_efee_r = obj.get('ten_dd_efee_r')
            exchange_rate.kftc_bkpr = obj.get('kftc_bkpr')
            exchange_rate.kftc_deal_bas_r = obj.get('kftc_deal_bas_r')
            exchange_rate.cur_nm = obj.get('cur_nm')
            exchange_rate.save()
        else:
            ExchangeRate.objects.create(
                cur_unit = obj.get('cur_unit'),
                ttb = obj.get('ttb'),
                tts = obj.get('tts'),
                deal_bas_r = obj.get('deal_bas_r'),
                bkpr = obj.get('bkpr'),
                yy_efee_r = obj.get('yy_efee_r'),
                ten_dd_efee_r = obj.get('ten_dd_efee_r'),
                kftc_bkpr = obj.get('kftc_bkpr'),
                kftc_deal_bas_r = obj.get('kftc_deal_bas_r'),
                cur_nm = obj.get('cur_nm'),
            )
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