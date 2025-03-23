from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist':postlist})

# login function that requests login.html
def login(request):
    return render(request, 'main/login.html')

