from rest_framework import serializers
from chat.models import Chat
from lot.serializers import LotSerializers
from account.serializers import AccountSerializers



class ChatSerializers(serializers.ModelSerializer):
    lot = LotSerializers
    user = AccountSerializers

    class Meta:
        model = Chat
        fields = ('id','time','text','user')