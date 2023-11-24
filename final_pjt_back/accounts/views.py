from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
from products.models import Deposit, Saving
from products.serializers import DepositSerializer, SavingSerializer
import random
import pandas as pd
import sqlite3
import datetime


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user_model = get_user_model()
        user = user_model.objects.get(username=username)
        user_serializer = ProfileSerializer(user)
        return Response(user_serializer.data)
    
    
@api_view(['POST'])
def permission(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_model = get_user_model()
            user = user_model.objects.get(username=username)
            res = {
                'is_super': user.is_superuser,
                'is_staff': user.is_staff,
            }
            return Response(res)
        
    else:
        return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def dummy_user_deposit_saving(request):
    user_model = get_user_model()
    users = user_model.objects.all()
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
    if request.user.is_authenticated:
        def calc_age(birthdate):
            today = datetime.datetime.today()
            birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
            age = today.year-birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        
        user_model = get_user_model()
        user = user_model.objects.get(username=username)
        con = sqlite3.connect("db.sqlite3")
        query = 'SELECT * FROM accounts_user_deposit_products'
        deposit_products = pd.read_sql(query, con)
        con.close()

        con = sqlite3.connect("db.sqlite3")
        query = 'SELECT * FROM accounts_user_saving_products'
        saving_products = pd.read_sql(query, con)
        con.close()

        con = sqlite3.connect("db.sqlite3")
        query = 'SELECT * FROM accounts_user'
        users = pd.read_sql(query, con)
        con.close()

        df_deposit = pd.merge(users, deposit_products, left_on='id', right_on='user_id', how='inner')
        df_deposit['age'] = df_deposit['birth_date'].apply(calc_age)

        user_age = calc_age(str(user.birth_date))
        user_salary = user.salary
        user_balance = user.balance
        user_deposit_products = df_deposit[df_deposit['username'] == user.username]['deposit_id'].values

        df_deposit['age_diff'] = abs(df_deposit['age']-user_age) 
        df_deposit['salary_diff'] = abs(df_deposit['salary']-user_salary)
        df_deposit['balance_diff'] = abs(df_deposit['balance']-user_balance)

        df_deposit = df_deposit[~df_deposit['deposit_id'].isin(user_deposit_products)]
        df_deposit = df_deposit.groupby('deposit_id')[['age_diff', 'balance_diff', 'salary_diff']].mean()
        df_deposit['points'] = df_deposit['age_diff'] + df_deposit['salary_diff']//1000000 + df_deposit['balance_diff']//1000000
        df_deposit = df_deposit.sort_values('points')

        df_saving = pd.merge(users, saving_products, left_on='id', right_on='user_id', how='inner')
        df_saving['age'] = df_saving['birth_date'].apply(calc_age)
        user_saving_products = df_saving[df_saving['username'] == user.username]['saving_id'].values

        df_saving['age_diff'] = abs(df_saving['age']-user_age)
        df_saving['salary_diff'] = abs(df_saving['salary']-user_salary)
        df_saving['balance_diff'] = abs(df_saving['balance']-user_balance)

        df_saving = df_saving[~df_saving['saving_id'].isin(user_saving_products)]
        df_saving = df_saving.groupby('saving_id')[['age_diff', 'balance_diff', 'salary_diff']].mean()
        df_saving['points'] = df_saving['age_diff'] + df_saving['salary_diff']//1000000 + df_saving['balance_diff']//1000000
        df_saving = df_saving.sort_values('points')

        deposit_list = []
        for prdt_cd in df_deposit.head(5).index:
            deposit = Deposit.objects.get(pk = prdt_cd)
            deposit_serializer = DepositSerializer(deposit)
            deposit_list.append(deposit_serializer.data)
            
        saving_list = []
        for prdt_cd in df_saving.head(5).index:
            saving = Saving.objects.get(pk = prdt_cd)
            saving_serializer = SavingSerializer(saving)
            saving_list.append(saving_serializer.data)
        
        json_response = {
            'deposits': deposit_list,
            'savings': saving_list,
        }
        return Response({'recommendations': json_response})
    else:
        return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def join(request, prdt_type, prdt_cd):
    user = request.user
    if prdt_type == 'deposits':
        prdt = Deposit.objects.get(pk=prdt_cd)
        user.deposit_products.add(prdt)
    elif prdt_type == 'savings':
        prdt = Saving.objects.get(pk=prdt_cd)
        user.saving_products.add(prdt)

    return Response({'msg': 'okay'},status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def cancel(request, prdt_type, prdt_cd):
    user = request.user
    if prdt_type == 'deposits':
        prdt = Deposit.objects.get(pk=prdt_cd)
        user.deposit_products.remove(prdt)
    elif prdt_type == 'savings':
        prdt = Saving.objects.get(pk=prdt_cd)
        user.saving_products.remove(prdt)

    return Response({'msg': 'okay'},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def username_validation(request, username):
    user_model = get_user_model()
    return Response({'exists': user_model.objects.filter(username=username).exists()})

@api_view(['GET'])
def nickname_validation(request, nickname):
    user_model = get_user_model()
    return Response({'exists': user_model.objects.filter(nickname=nickname).exists()})
