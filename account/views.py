from rest_framework.response import Response
from rest_framework.views import APIView
from account import serializers, models
from rest_framework import viewsets
from django.contrib.auth import login, authenticate
from account.forms import SignUpForm
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
#from rest_framework.permissions import IsAdminUser

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.AccountSerializers
    #permission_classes = [IsAdminUser]

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.username = form.cleaned_data.get('full_name')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            token1 = get_tokens_for_user(user)
            return redirect('lots')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})