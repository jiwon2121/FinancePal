from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request, board_type):
    if request.method == 'GET':
        articles = get_list_or_404(Article.objects.order_by('-pk'), board_type=board_type)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, article=article)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'PUT':
        if request.user.is_authenticated:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT', 'DELETE'])
def comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        if request.user.is_authenticated:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
