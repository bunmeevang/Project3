from .models import Array, Push
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArraySerializer, PushSerializer


class ArrayViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Array.objects.all()
    # The serializer class for serializing output
    serializer_class = ArraySerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]


class PushViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Push.objects.all()
    # The serializer class for serializing output
    serializer_class = PushSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]