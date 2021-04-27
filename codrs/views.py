from .models import Array, Comment, Profile
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArraySerializer, CommentSerializer, ProfileSerializer


class ArrayViewSet(viewsets.ModelViewSet):
    queryset = Array.objects.all()
    serializer_class = ArraySerializer
    permission_classes = [permissions.AllowAny]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

