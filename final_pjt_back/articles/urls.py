from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<str:board_type>/', views.article_list),
    path('<str:board_type>/<int:article_pk>/', views.article_detail),
]
