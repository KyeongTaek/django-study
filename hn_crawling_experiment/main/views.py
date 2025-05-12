from django.shortcuts import render
from .models import Post

from .serializers import PostSerializer
from rest_framework.response import Response

from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    def retrieve(self, request, pk=None): # posting function that requests posting.html
        queryset = Post.objects.get(pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def list(self, request): # index function that requests index.html
        self.queryset = Post.objects.all()
        serializer = self.get_serializer(self.queryset, many=True)
        

        return Response(serializer.data)