from .models import Array, Push, Profile
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PushSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Push
        # the fields that should be included in the serialized output
        fields = ['id', 'user', 'push']


class ArraySerializer(serializers.ModelSerializer):
    # push = serializers.StringRelatedField(many=True)
    push = PushSerializer(many=True)
    class Meta:
        model = Array
        fields = ['id', 'user', 'body', 'push']

    def create(self, validated_data):
        push_data = validated_data.pop('push')
        array = Array.objects.create(**validated_data)
        for push_data in pushs_data:
            Push.objects.create(array=array, **push_data)
        return array


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Profile
        # the fields that should be included in the serialized output
        fields = ['id', 'firstname', 'lastname', 'genderpronouns', 'location', 'aboutme', 'linkedin']

# Our TodoSerializer
# class ArraySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # The model it will serialize
#         model = Array
#         # the fields that should be included in the serialized output
#         fields = ['id', 'user', 'body']


# class ArraySerializer(serializers.ModelSerializer):
#     push = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Array
#         fields = "__all__"


