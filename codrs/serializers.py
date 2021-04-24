from .models import Array, Push, Profile
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class ArraySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Array
        # the fields that should be included in the serialized output
        fields = ['id', 'user', 'body']

class PushSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Push
        # the fields that should be included in the serialized output
        fields = ['id', 'user', 'push', 'array']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Profile
        # the fields that should be included in the serialized output
        fields = ['id', 'firstname', 'lastname', 'genderpronouns', 'location', 'aboutme', 'linkedin']

