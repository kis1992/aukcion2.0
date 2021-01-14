from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import UserViews, MyObtainTokenPairView, RegisterView #AccountViewSet
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()

#create_user = AccountViewSet.as_view({'post':'create_user'})

#router.register(r'accounts', AccountViewSet, basename='account')


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserViews.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

#urlpatterns += router.urls