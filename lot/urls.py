from django.urls import path
from .views import LotViews
from lot.views import LotViewSet, PriceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lots', LotViewSet, basename='lot')
router.register(r'prices', PriceViewSet, basename='price')
urlpatterns = router.urls


#urlpatterns = [
    #path('price/', PriceViews.as_view()),
    #path('category/', CategoryViews.as_view()),
    #path('', LotViews.as_view()),
    #path('lot/<int:id>', LotPutDelete.as_view()),
    #path('lot/delete/<int:id>', LotPutDelete.as_view()),
#]
