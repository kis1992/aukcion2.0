from django.urls import path
from .views import ChatView,ChatPutDeleteView

urlpatterns = [
    path('', ChatView.as_view()),
    path('<int:id>',ChatPutDeleteView.as_view())
]
