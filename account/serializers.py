from rest_framework import serializers
from django.conf import settings
from account.models import BaseUser

class AccountSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = BaseUser
        fields = ( 'id' , 'username' )