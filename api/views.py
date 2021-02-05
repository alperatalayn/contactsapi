from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin
from rest_framework import status, views
from .models import Contact
from .serializers import ContactSerializer, RegisterSerializer
import json
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pdfReport(request):
    try:
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        data = [["Ad","Soyad","Telefon No."]]
        if request.user.is_superuser: 
            contacts = Contact.objects.all()
        else:
            contacts = Contact.objects.filter(owner=request.user)
        for contact in contacts:
            data.append([contact.first_name,contact.last_name,contact.phone])

        table = Table(data,colWidths=570/3)

        style = TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.aliceblue),
            ('TEXTCOLOR',(0,0),(-1,0),colors.black),
            ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
            ('FONTSIZE',(0,0),(-1,0),22),
            ('BOTTOMPADDING',(0,0),(-1,0),20),
        ])
        table.setStyle(style)

        rowNum = len(data)
        for i in range(1,rowNum):
            if i%2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige
            ts = TableStyle(
                [('BACKGROUND',(0,i),(-1,i),bc)]
            )
            table.setStyle(ts)
        ts = TableStyle(
                [
                    ('BOX',(0,0),(-1,-1),2,colors.black),
                    ('GRID',(0,1),(-1,-1),2,colors.black)
                ]
            )
        table.setStyle(ts)
        table.wrapOn(pdf,1,1)
        table.drawOn(pdf,10,832-table._height)
        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer,filename="report.pdf",as_attachment=True)
    except:
        raise Exception("An error occured")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def contactList(request):
    try:
        if request.user.is_superuser: 
            contacts = Contact.objects.all()
        else:
            contacts = Contact.objects.filter(owner=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def createContact(request):
    try:
        serializer = ContactSerializer(data=request.data)
        serializer.create(validated_data=request.data,user=request.user)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except:
        raise Exception("An error occured")
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsOwnerOrAdmin])
def deleteContact(request,pk):
    contact = Contact.objects.get(id=pk)
    try:
        if(IsOwnerOrAdmin.has_object_permission(IsOwnerOrAdmin,request=request,view=deleteContact,obj= contact)):
            contact.delete()
            return Response("deleted")
        else:
            return Response(status= status.HTTP_403_FORBIDDEN)
    except:
        raise Exception("An error occured")
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateContact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        if(IsOwnerOrAdmin.has_object_permission(IsOwnerOrAdmin,request=request,view=updateContact,obj= contact)):
            serializer = ContactSerializer(instance=contact,data=request.data)
            serializer.update(instance= contact,validated_data=request.data)
        
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data) 
        else:
            return Response(status= status.HTTP_403_FORBIDDEN)
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
