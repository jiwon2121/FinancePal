from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/', views.article_detail),
    path('<str:board_type>/', views.article_list),
    path('comment/<int:comment_pk>/', views.comment),
]
