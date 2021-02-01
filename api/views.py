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
    try:
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
@api_view(['GET'])
def contactSingle(request,pk):
    try:
        contacts = Contact.objects.get(id=pk)
        serializer = ContactSerializer(contacts, many=False)
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
@api_view(['POST'])
def createContact(request):
    try:
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
@api_view(['DELETE'])
def deleteContact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return Response("deleted")
    except:
        raise Exception("An error occured")
@api_view(['POST'])
def updateContact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        serializer = ContactSerializer(instance=contact,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
    except:
        raise Exception("An error occured")