from .models import Account
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AccountSerializer
# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Account.objects.all()
    # The serializer class for serializing output
    serializer_class = AccountSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

