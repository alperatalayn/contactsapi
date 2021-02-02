from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact,Adress
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
        print(validated_data)
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
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {'password':{'write_only':True}}
    def create(self,validated_data):
        try:    
            password = validated_data.pop('password',None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        except:
            raise Exception("Error while creating user")

class AdressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)
    def create(self, validated_data):
        try: 
            return Adress.objects.create(**validated_data)
        except:
            raise Exception("Error while creating adress")
    def update(self, instance, validated_data):
        try: 
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance
        except:
            raise Exception("Error while updating adress")
class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    adresses = AdressSerializer(many=True)
    first_name = serializers.CharField(default ="",max_length=50)
    last_name = serializers.CharField(default ="",max_length=50)
    phone = serializers.CharField(default ="",max_length=20)
    job =  serializers.CharField(default ="",max_length=50)

    def create(self, validated_data):
        try:    
            adresses_data = validated_data.pop('adresses')
            contact = Contact.objects.create(**validated_data)
            for adress_data in adresses_data:
                Adress.objects.create(contact=contact, **adress_data)
            return contact
        except:
            raise Exception("Error while creating Contact")
    def update(self, instance, validated_data):
        try:    
            adresses_data = validated_data.pop('adresses',instance.adresses)
            print(adresses_data)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.job = validated_data.get('job', instance.job)
            for adress in adresses_data:
                adress_id = adress.get('id')
                if (adress_id):
                    old_adress = Adress.objects.get(id= adress_id, contact=instance)
                    old_adress.title = adress.get('title', old_adress.title)
                    old_adress.content = adress.get('content', old_adress.content)
                    old_adress.save()
                else:
                    Adress.objects.create(contact=instance, **adress)
            instance.save()
            return instance
        except:
            raise Exception("Error while updating contact")
