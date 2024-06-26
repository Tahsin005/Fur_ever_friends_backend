from django.shortcuts import render
from rest_framework import viewsets
from . models import Pet, Category, Review
from . serializers import PetSerializer, CategorySerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories__slug', 'categories__name']
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pet__id']
    