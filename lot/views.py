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
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LotViewSet(viewsets.ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializers
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #@action(detail=True, methods=['get'])
    def list(self, request):
        prices = self.queryset
        serializer = self.serializer_class(prices,many = True)
        if request.user.is_anonymous:
            return Response({'prices':serializer.data, 'anonymous':True},template_name='base.html')
        return Response({'prices':serializer.data},template_name='base.html')


    #@action(detail=True,renderer_classes=[TemplateHTMLRenderer])
    def retrieve(self, request, pk=None):
        price = self.get_object()
        self.template_name='get_lot.html'
        #serializer = self.serializer_class(price)
        if request.user.is_anonymous:
            return Response({'price':price,'anonymous':True})
        return Response({'price':price})

    def update(self, request, pk=None):
        print('partial is activate')
        price = self.queryset.get(pk=pk)
        one_step = price.final_price+price.step_price
        self.template_name='get_lot.html'
        serializer = self.serializer_class(price)
        serializer.save(final_price=one_step,last_owner=self.request.user)
        if request.user.is_anonymous:
            return Response({'price':price})
        return Response({'price':price})


class PriceViewSet(viewsets.ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializers
    renderer_classes = [TemplateHTMLRenderer,JSONRenderer]

    def list(self, request):
        prices = self.queryset
        serializer = self.serializer_class(prices,many = True)
        return Response({'prices':serializer.data},template_name='base.html')
    
    #@action(detail=True,renderer_classes=[TemplateHTMLRenderer])
    def retrieve(self, request, pk=None):
        price = self.get_object()
        self.template_name='get_lot.html'
        #serializer = self.serializer_class(price)
        return Response({'price':price})

    def partial_update(self, request, *args, **kwargs):
        price = self.get_object()
        one_step = price.final_price+price.step_price
        self.template_name='get_lot.html'
        serializer = self.serializer_class(price)
        serializer.save(final_price=one_step,last_owner=self.request.user)
        return Response({'price':price})

class LotViews(ListAPIView):
    serializer_class = serializers.LotSerializers
    queryset = models.Lot.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # pagination_class = utils.BaseProductPagination
    ordering_fields = ['lot_start_price', 'lot_start_time']
    search_fields = ['lot_name', 'lot_description']
    filterset_fields = ['lot_start_price', 'lot_activity']