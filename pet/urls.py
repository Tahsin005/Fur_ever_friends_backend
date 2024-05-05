from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('list', views.PetViewSet)
router.register('category', views.CategoryViewSet)
router.register('review', views.ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
