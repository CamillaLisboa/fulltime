from rest_framework import serializers
from .models import Person, Bill

class PersonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BillSerializer (serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'