from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .models import Contact
from .serializers import ContactSerializer
# Create your views here.


@api_view(['GET'])
def contactList(request):
    contacts = Contact.objects.all()
    print(contacts)
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contactSingle(request,input):
    contacts = Contact.objects.get(id=input)
    serializer = ContactSerializer(contacts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createContact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteContact(request,input):
    contact = Contact.objects.get(id=input)
    contact.delete()
    return Response("deleted")
    

@api_view(['POST'])
def updateContact(request,input):
    contact = Contact.objects.get(id=input)
    serializer = ContactSerializer(instance=contact,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)