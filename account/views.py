from rest_framework.response import Response
from rest_framework.views import APIView
from account import serializers, models
from rest_framework import viewsets
from django.contrib.auth import login, authenticate
from account.forms import SignUpForm
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import action
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = models.BaseUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViews(APIView):

    def get(self, request):
        renderer_classes = [TemplateHTMLRenderer]
        form = SignUpForm()
        return Response({'form':form},template_name='registration.html')
       

    def post(self, request):
        print('user creation')
        queryset = models.BaseUser.objects.all()
        serializer_class = serializers.AccountSerializers
        renderer_classes = [TemplateHTMLRenderer]
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return Response({'new_user':new_user},template_name='after_first_registration.html')
        else:
            print('user creation is failed')
            form = SignUpForm()
        return Response({'form':form},template_name='registration.html')

"""def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
#from rest_framework.permissions import IsAdminUser


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.AccountSerializers
    renderer_classes = [TemplateHTMLRenderer]
    #permission_classes = [IsAdminUser]

    def list(self, request):
        form = SignUpForm()
        return Response({'form':form},template_name='registration.html')

    @action(detail=False, methods=['post'])
    def create_user(self, request):
        print('Enter post')
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(BaseUserManager().make_random_password())
            new_user.save()
            return Response({'new_user':new_user},template_name='after_first_registration.html')
        else:
            form = SignUpForm()
        return Response({'form':form},template_name='registration.html')"""