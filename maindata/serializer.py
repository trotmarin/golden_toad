from rest_framework import serializers
from .models import TestTable, Table2

class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = '__all__'

class Table2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table2
        fields = '__all__'
