from rest_framework import serializers 
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = (['user_name'])
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:     
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
        except:
            raise Exception("Error while creating user")