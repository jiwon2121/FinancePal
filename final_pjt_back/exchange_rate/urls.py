from django.urls import path
from . import views

app_name = 'exchange_rate'
urlpatterns = [
    path('save/', views.save),
    path('all/', views.all),
    path('<str:pk>/', views.by_country),
]
