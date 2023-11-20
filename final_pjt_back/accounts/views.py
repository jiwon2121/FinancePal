from django.shortcuts import render
from .models import User
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)