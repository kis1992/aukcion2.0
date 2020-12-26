from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from lot import serializers, models
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from lot import utils
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer

class LotViewSet(viewsets.ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializers
    renderer_classes = [TemplateHTMLRenderer]

    #@action(detail=True, methods=['get'])
    def list(self, request):
        prices = self.queryset
        serializer = self.serializer_class(prices,many = True)
        return Response({'prices':serializer.data},template_name='base.html')

class PriceViewSet(viewsets.ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializers
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request):
        prices = self.queryset
        serializer = self.serializer_class(prices,many = True)
        return Response({'prices':serializer.data},template_name='base.html')

class LotViews(ListAPIView):
    serializer_class = serializers.LotSerializers
    queryset = models.Lot.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # pagination_class = utils.BaseProductPagination
    ordering_fields = ['lot_start_price', 'lot_start_time']
    search_fields = ['lot_name', 'lot_description']
    filterset_fields = ['lot_start_price', 'lot_activity']