from .models import Array, Comment, Profile
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment']


class ArraySerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)
    class Meta:
        model = Array
        fields = ['id', 'user', 'body', 'comment']

    def create(self, validated_data):
        comment_data = validated_data.pop('comment')
        array = Array.objects.create(**validated_data)
        for comment_data in comment_data:
            Comment.objects.create(array=array, **comment_data)
            Comment.objects.create(comment=comment, **comment_data)
        return array

    def update(self, instance, validated_data):
        comment_data = validated_data.pop('comment')
        comments = (instance.comment).all()
        comments = list(comments)
        instance.user = validated_data.get('user', instance.user)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        for comment_data in comment_data:
            comment = comments.pop(0)
            comment.user = comment_data.get('user', comment.user)
            comment.body = comment_data.get('comment', comment.comment)
            comment.save()
        return instance


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'firstname', 'lastname', 'genderpronouns', 'location', 'aboutme', 'linkedin']

