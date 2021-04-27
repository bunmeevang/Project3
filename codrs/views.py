from .models import Array, Comment, Profile
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArraySerializer, CommentSerializer, ProfileSerializer


class ArrayViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Array.objects.all()
    # The serializer class for serializing output
    serializer_class = ArraySerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Comment.objects.all()
    # The serializer class for serializing output
    serializer_class = CommentSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Profile.objects.all()
    # The serializer class for serializing output
    serializer_class = ProfileSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

