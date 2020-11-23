from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['edad',  'Nombre', 'Salario']
