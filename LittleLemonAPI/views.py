from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics , viewsets
from restaurant.models import Booking,Menu  # ← import from restaurant app
from .serializers import MenuItemSerializer , BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):  
    return HttpResponse({"message":"This view is protected"})

# GET all + POST new item
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


# GET single + PUT + DELETE
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


