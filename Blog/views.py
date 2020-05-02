from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def all_blog(request):
    blogs = Blog.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request,'blog/all_blog.html',context)


def postDetails(request,post_id):
    blog = get_object_or_404(Blog,pk=post_id)
    context ={
        'blog':blog,
    }
    return render(request,'blog/blog_details.html',context)