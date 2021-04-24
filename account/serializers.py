from .models import Account
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Account
        # the fields that should be included in the serialized output
        fields = ['email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser']