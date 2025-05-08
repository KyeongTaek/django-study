from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

from .serializers import PostSerializer
from rest_framework.response import Response

from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    def retrieve(self, request): # posting function that requests posting.html
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post'])
    def create_post(self, request):
        return create(request)

    # def create(self, request): # new_post function that requests new_post.html
    #     if request.method == 'POST':
    #         new_article = JSONParser().parse(request)
    #         serializer = PostSerializer(data=new_article)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)

    def list(self, request): # index function that requests index.html
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# login function that requests login.html
def login(request):
    return render(request, 'main/login.html')

