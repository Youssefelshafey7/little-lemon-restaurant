from rest_framework.serializers import ModelSerializer
from restaurant.models import Booking,Menu  # ← import from restaurant app

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'



class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'