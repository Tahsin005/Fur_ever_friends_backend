from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.TransactionApiView.as_view(), name='deposit'),
]
