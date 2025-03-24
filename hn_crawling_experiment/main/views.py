from django.shortcuts import render
from .models import Post

# Create your views here.

# index function that requests index.html
def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist':postlist})

# posting function that requests posting.html
def posting(request, pk):
    post = Post.objects.get(pk=pk) # get a post by its primary key
    return render(request, 'main/posting.html', {'post':post})


# login function that requests login.html
def login(request):
    return render(request, 'main/login.html')

