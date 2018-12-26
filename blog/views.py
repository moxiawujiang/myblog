from django.shortcuts import render
from blog.models import BlogsPost
# Create your views here.

def blog_index(request):
    blog_lists=BlogsPost.objects.all()
    return  render(request,"index.html",{'blog_list':blog_lists})
