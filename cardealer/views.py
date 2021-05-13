from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dealers, Cars
from .serializers import DealersSerializer, CarsSerializer


def index(request):
    return render(request, template_name='cardealer/index.html', context={})


class DealersViewSet(viewsets.ModelViewSet):
    queryset = Dealers.objects.all()
    serializer_class = DealersSerializer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
