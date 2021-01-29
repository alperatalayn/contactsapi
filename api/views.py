from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .models import Contact
from .serializers import ContactSerializer
import json
# Create your views here.


@api_view(['GET'])
def contactList(request):
    contacts = Contact.objects.all()
    print(contacts)
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contactSingle(request,pk):
    contacts = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contacts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createContact(request):
    serializer = ContactSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteContact(request,pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return Response("deleted")
    

@api_view(['POST'])
def updateContact(request,pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=contact,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)