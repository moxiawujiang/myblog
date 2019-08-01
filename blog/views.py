from django.shortcuts import render
from blog.models import Article
# Create your views here.

def blog_index(request):
    blog_lists=Article.objects.all()
    return  render(request,"index.html",{'blog_list':blog_lists})
