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