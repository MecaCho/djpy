#coding=utf-8
from django.shortcuts import render
from blog.models import BlogPost
from django.shortcuts import render_to_response
from django.http import Http404
#from django.core.files.base import ContentFile


# Create your views here.

'''def getImg(request):
    file_content = ContentFile(request.FILES['img'].read())
    img = ImageStore(name=request.FILES['img'].name, img= request.FILES['img'])
    img.save()'''


def index(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})


def detail(request):
    return render_to_response('detail.html')