from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Person, Bill
from .serializers import PersonSerializer, BillSerializer

import json

@api_view(['GET','POST','PUT'])
def get_person(request):
    if request.method == 'GET':
        try:
            person = Person.objects.all()

            serializer = PersonSerializer(person, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':

        new_person = request.data

        serializer = PersonSerializer(data = new_person)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method == 'PUT':
        id = request.data['id']
        updated_person = Person.objects.get(id=id)

        serializer = PersonSerializer(updated_person, data=request.data)
    return Response(status=status.HTTP_404_NOT_FOUND)
   
   
@api_view(['GET','POST','PUT'])
def get_bill(request):
    if request.method == 'GET':
        bill = Bill.objects.all()

        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        new_bill = request.data

        serializer = BillSerializer(data = new_bill)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)
    


