from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # Since "CustomUser" inherits from Django's built-in AbstractUser, not all fields are explicitly visible in this project's models.py or serializers.py. If you want to inspect what fields actually exist in the model place your cursor on "AbstractUser" and press F12 (or the equivalent "Go to Definition" key in your IDE). This will take you to the source code where all inherited fields are defined.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

    
