from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Person, Bill
from .serializers import PersonSerializer, BillSerializer

import json

@api_view(['GET'])
def get_person(request):
    if request.method == 'GET':
        person = Person.objects.all()

        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_bill(request):
    if request.method == 'GET':
        bill = Bill.objects.all()

        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)