from django.shortcuts import render,get_object_or_404 , redirect
from django.utils import timezone
from .models import blog
# Create your views here.

def home(request):
    blogs = blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request): 
    return render(request, 'new.html')

def create(request):
    Blog = blog()
    Blog.title = request.GET['title']
    Blog.body = request.GET['body']
    Blog.pub_date = timezone.datetime.now()
    Blog.save()
    return redirect('/blog/' + str(Blog.id))