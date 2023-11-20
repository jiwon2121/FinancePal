from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('save_deposit_products/', views.save_deposit_products),
    path('save_saving_products/', views.save_saving_products),
    path('deposits/', views.deposits),
    path('deposits/<str:pk>/', views.deposit_detail),
    path('savings/', views.savings),
    path('savings/<str:pk>/', views.saving_detail),
]
