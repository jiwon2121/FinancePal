from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request, board_type):
    if request.method == 'GET':
        articles = get_list_or_404(Article, board_type=board_type)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        user_model = get_user_model()
        user = user_model.objects.get(username=request.data.get('username'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        user_model = get_user_model()
        user = user_model.objects.get(username=request.data.get('username'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['PUT', 'DELETE'])
def comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)