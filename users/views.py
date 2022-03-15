from dataclasses import field
from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer
from users.models import CustomUser

from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_of_birth')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)