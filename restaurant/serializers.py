#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__' 