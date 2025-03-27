from django.shortcuts import render, redirect
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

# new_post function that requests new_post.html
def new_post(request):
    if request.method == 'POST':
        if "mainphoto" in request.FILES:
            new_article=Post.objects.create(
                    postname=request.POST['postname'],
                    contents=request.POST['contents'],
                    mainphoto=request.FILES['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                    postname=request.POST['postname'],
                    contents=request.POST['contents'],
            )
        return redirect('/')
    return render(request, 'main/new_post.html')
