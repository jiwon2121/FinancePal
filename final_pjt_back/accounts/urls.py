from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('<str:username>/', views.profile),
    path('save/dummy_user_deposit_saving/', views.dummy_user_deposit_saving),
    path('permission/<str:username>/', views.permission),
]
