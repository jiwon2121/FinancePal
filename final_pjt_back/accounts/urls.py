from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('<str:username>/', views.profile),
    path('save/dummy_user_deposit_saving/', views.dummy_user_deposit_saving),
    path('recommend_by_profile/<str:username>/', views.recommend_by_profile),
    # path('recommend_by_portfolio/<str:username>/', views.recommend_by_portfolio),
    path('permission/<str:username>/', views.permission),
]
