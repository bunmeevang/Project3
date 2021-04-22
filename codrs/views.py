from .models import Array
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CodrSerializer


class CodrViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Array.objects.all()
    # The serializer class for serializing output
    serializer_class = CodrSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]