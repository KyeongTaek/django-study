from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

# index function that requests index.html
def index(request):
    page = request.GET.get('page', '1') # page
    postlist = Post.objects.all()
    paginator = Paginator(postlist, 5) # show 5 posts per page
    page_obj = paginator.get_page(page)
    context = {'postlist':postlist}
    return render(request, 'main/index.html', context)

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
