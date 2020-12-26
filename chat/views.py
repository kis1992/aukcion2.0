from rest_framework.response import Response
from rest_framework.views import APIView
from chat import serializers, models


class ChatView(APIView):
    
    def get(self,request):
        chats = models.Chat.objects.all()
        serializer = self.class_serializer(chats, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        chat = request.data
        serializer_elem = self.class_serializer(data=chat)

        if serializer_elem.is_valid():
            serializer_elem.save()
            return Response(serializer_elem.data)

        return Response({"status": "faild", "message": serializer_elem.errors})

class ChatPutDeleteView(APIView):
    class_serializer = serializers.ChatSerializers

    def get_chat_by_id(self,id):
        chat = None
        try:
            chat = models.Chat.objects.get(id=id)
        except models.Chat.DoesNotExist:
            return Response({'message':'This id is not exist!!!'})
        return chat
    
    def get(self,request,id):
        chat = self.get_chat_by_id(id)
        if not chat:
            return Response({"message":"NOT FOUND"})
        serializer = self.class_serializer(chat)
        return Response(serializer.data)

    def put(self,request,id):
        chat = self.get_chat_by_id(id)
        if not chat:
            return Response({"message":"NOT FOUND"})
        
        serializer = self.class_serializer(chat, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"Chat succesful updated!!!"})
        else:
            return Response({"message":"Chat is not updated!!!"})

    def delete(self,request,id):
        chat = self.get_chat_by_id(id)
        if not chat:
            return Response({"message":"NOT FOUND"})
        chat.delete()
        return Response({"message":"Chat deleted!!!"})





