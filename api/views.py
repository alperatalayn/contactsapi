from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions,status,views
from .models import Contact
from .serializers import ContactSerializer, RegisterSerializer
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
@permission_classes([IsAuthenticated])
def createContact(request):
    permissions
    try:
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteContact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return Response("deleted")
    except:
        raise Exception("An error occured")
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateContact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        serializer = ContactSerializer(instance=contact,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
    except:
        raise Exception("An error occured")

@api_view(['POST'])
def createUser(request):
    try:
        reg_serializer = RegisterSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    except:
        raise Exception("An error occured")