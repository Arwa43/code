from rest_framework import serializers,validators
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name",)
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }
class CardSerializer(serializers.ModelSerializer):
    class Meta:
         model = card
         fields = '__all__'
         
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Payment
         fields = '__all__'
class requestSerializer(serializers.ModelSerializer):
    class Meta:
         model = requestes_id
         fields = '__all__'
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
         model = Report
         fields = '__all__'         
         
class reportSerializer(serializers.Serializer):
   start_date = serializers.DateField()
   end_date = serializers.DateField()
   
   