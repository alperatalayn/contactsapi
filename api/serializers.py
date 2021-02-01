from rest_framework import serializers
from .models import Contact,Adress

"""
class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['title', 'content']

class ContactSerializer(serializers.ModelSerializer):
    adresses = AdressSerializer(many=True)

    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        adresses_data = validated_data.pop('adresses')
        contact = Contact.objects.create(**validated_data)
        for adress_data in adresses_data:
            Adress.objects.create(contact=contact, **adress_data)
        return contact
    def update(self, instance, validated_data):
        adresses_data = validated_data.pop('adresses')
        adresses = instance.adresses
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.job = validated_data.get('job', instance.job)
        for adress in adresses.all():
            adress.delete()
        for adress_data in adresses_data:
            Adress.objects.create(contact=instance, **adress_data)
        instance.save()

        return instance
"""

#Serializers with default library

class AdressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)
    def create(self, validated_data):
        return Adress.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    adresses = AdressSerializer(many=True)
    first_name = serializers.CharField(default ="",max_length=50)
    last_name = serializers.CharField(default ="",max_length=50)
    phone = serializers.CharField(default ="",max_length=20)
    job =  serializers.CharField(default ="",max_length=50)

    def create(self, validated_data):
        adresses_data = validated_data.pop('adresses')
        contact = Contact.objects.create(**validated_data)
        for adress_data in adresses_data:
            Adress.objects.create(contact=contact, **adress_data)
        return contact
    def update(self, instance, validated_data):
        adresses_data = validated_data.pop('adresses')
        adresses = instance.adresses
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.job = validated_data.get('job', instance.job)
        for adress in adresses.all():
            adress.delete()
        for adress_data in adresses_data:
            Adress.objects.create(contact=instance, **adress_data)
        instance.save()

        return instance