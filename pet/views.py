from django.shortcuts import render
from rest_framework import viewsets
from . models import Pet, Category, Review
from . serializers import PetSerializer, CategorySerializer, ReviewSerializer
# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    