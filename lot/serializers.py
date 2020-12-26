from rest_framework import serializers
from lot import models
from account.serializers import AccountSerializers


class RecursiveSerializers(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class LotSerializers(serializers.ModelSerializer):
    #price = PriceSerializers
    #category = CategoryForLotSerializers(many=True)
    
    class Meta:
        model = models.Lot
        fields = ('id','lot_name','lot_description','lot_start_price','lot_image','lot_start_time')

class PriceSerializers(serializers.ModelSerializer):
    lots = LotSerializers()
    last_owner = AccountSerializers()
    class Meta:
        model = models.Price
        fields = ('id', 'lots', 'step_price', 'final_price', 'auto_price', 'last_owner')


class CategorySerializers(serializers.ModelSerializer):
    children = RecursiveSerializers(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'category_name', 'parent', 'children')



class CategoryForLotSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'category_name','slug')