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
        for push_data in push_data:
            Push.objects.create(array=array, **push_data)
            Push.objects.create(push=push, **push_data)
        return array

    def update(self, instance, validated_data):
        push_data = validated_data.pop('push')
        pushs = (instance.push).all()
        pushs = list(pushs)
        instance.user = validated_data.get('user', instance.user)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        for push_data in push_data:
            push = pushs.pop(0)
            push.user = push_data.get('user', push.user)
            push.body = push_data.get('push', push.push)
            push.save()
        return instance


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Profile
        # the fields that should be included in the serialized output
        fields = ['id', 'firstname', 'lastname', 'genderpronouns', 'location', 'aboutme', 'linkedin']

