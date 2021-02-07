from django.shortcuts import render

from rest_framework import viewsets
from .serializer import Table2Serializer, TestTableSerializer
from .models import TestTable, Table2

# Create your views here.

class TestTableViewSet(viewsets.ModelViewSet):
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer

class Table2ViewSet(viewsets.ModelViewSet):
    queryset = Table2.objects.all()
    serializer_class = Table2Serializer
    
