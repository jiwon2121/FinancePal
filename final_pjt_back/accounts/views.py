from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    user = User.objects.get(pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)