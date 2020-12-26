from rest_framework.response import Response
from rest_framework.views import APIView
from account import serializers, models
from rest_framework import viewsets
#from rest_framework.permissions import IsAdminUser

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.AccountSerializers
    #permission_classes = [IsAdminUser]