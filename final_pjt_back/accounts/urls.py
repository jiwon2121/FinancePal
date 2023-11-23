from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('<str:username>/', views.profile),
    path('save/dummy_user_deposit_saving/', views.dummy_user_deposit_saving),
    path('recommend_by_profile/<str:username>/', views.recommend_by_profile),
    path('permission/<str:username>/', views.permission),
    path('join/<str:prdt_type>/<str:prdt_cd>/', views.join),
    path('cancel/<str:prdt_type>/<str:prdt_cd>/', views.cancel),
    path('username/validation/<str:username>/', views.username_validation),
    path('nickname/validation/<str:nickname>/', views.nickname_validation)
]
