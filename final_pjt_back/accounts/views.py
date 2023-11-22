from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from products.models import Deposit, Saving
from products.serializers import DepositSerializer, SavingSerializer, DepositOptionSerializer, SavingOptionSerializer
import random
import pandas as pd
import sqlite3
import datetime


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        user_serializer = ProfileSerializer(user)
        return Response(user_serializer.data)
    
    
@api_view(['POST'])
def permission(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=username)
            res = {
                'is_super': user.is_superuser,
                'is_staff': user.is_staff,
            }
            return Response(res)
        
    else:
        return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)



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
    if request.user.is_authenticated():
        def calc_age(birthdate):
            today = datetime.datetime.today()
            birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
            age = today.year-birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        
        user = User.objects.get(username=username)
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

        user_age = df_deposit[df_deposit['username']==user.username]['age'].values[0]
        user_salary = df_deposit[df_deposit['username'] == user.username]['salary'].values[0]
        user_age_balance = df_deposit[df_deposit['username'] == user.username]['balance'].values[0]
        user_deposit_products = df_deposit[df_deposit['username'] == user.username]['deposit_id'].values

        df_deposit['age_diff'] = abs(df_deposit['age']-user_age)
        df_deposit['salary_diff'] = abs(df_deposit['salary']-user_salary)
        df_deposit['balance_diff'] = abs(df_deposit['balance']-user_age_balance)

        df_deposit = df_deposit[~df_deposit['deposit_id'].isin(user_deposit_products)]
        df_deposit = df_deposit.groupby('deposit_id')[['age_diff', 'balance_diff', 'salary_diff']].mean()
        df_deposit['points'] = df_deposit['age_diff'] + df_deposit['salary_diff']//1000000 + df_deposit['balance_diff']//1000000
        df_deposit = df_deposit.sort_values('points')

        df_saving = pd.merge(users, saving_products, left_on='id', right_on='user_id', how='inner')
        df_saving['age'] = df_saving['birth_date'].apply(calc_age)
        user_saving_products = df_saving[df_saving['username'] == user.username]['saving_id'].values

        df_saving['age_diff'] = abs(df_saving['age']-user_age)
        df_saving['salary_diff'] = abs(df_saving['salary']-user_salary)
        df_saving['balance_diff'] = abs(df_saving['balance']-user_age_balance)

        df_saving = df_saving[~df_saving['saving_id'].isin(user_saving_products)]
        df_saving = df_saving.groupby('saving_id')[['age_diff', 'balance_diff', 'salary_diff']].mean()
        df_saving['points'] = df_saving['age_diff'] + df_saving['salary_diff']//1000000 + df_saving['balance_diff']//1000000
        df_saving = df_saving.sort_values('points')


        json_response = {
            'deposits': df_deposit.head(5).index,
            'savings': df_saving.head(5).index,
        }
        return Response({'recommendations': json_response})
    
    else:
        return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    
