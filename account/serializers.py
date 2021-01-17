from rest_framework import serializers
from django.conf import settings
from account.models import BaseUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail

def send_password_mail(email,username,passwd):
    send_mail(
    subject="First authorization in aukcion.com",
    message="Dear "+username+", your secret passwd is "+passwd,
    from_email=email,
    recipient_list=[email],
    fail_silently=False,)


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=BaseUser.objects.all())]
            )

    #password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    #password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'first_name')
        extra_kwargs = {
            'first_name': {'required': True}
        }

    def create(self, validated_data):
        user = BaseUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name']
        )

        password = BaseUserManager().make_random_password()
        print(password)
        user.set_password(password)
        user.save()
        send_password_mail(user.email,user.username,password)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class AccountSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = BaseUser
        fields = ('id', 'username' , 'photo')
    

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(AccountSerializers, self).update(instance, validated_data)