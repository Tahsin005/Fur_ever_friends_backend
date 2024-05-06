from django.shortcuts import render
from rest_framework.views import APIView
from . models import Transaction
from . serializers import TransactionSerializer, PetAdoptSerializer
from rest_framework.response import Response
# Create your views here.

class TransactionApiView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            transaction = serializer.save()
            response_data = {'message' : 'Deposit successfull', 'transaction_id' : transaction.id,}
            
            return Response(response_data)
        else:
            return Response(serializer.errors)

class PetAdoptApiView(APIView):
    def post(self, request):
        serializer = PetAdoptSerializer(data=request.data)
        if serializer.is_valid():
            adopted_pet = serializer.save()
            return Response({"message": f"You have successfully adopted the pet: {adopted_pet.name}"})
        return Response(serializer.errors)
