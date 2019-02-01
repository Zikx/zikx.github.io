from django.shortcuts import render , get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,'home.html', {'blogs' : blogs})

def admin(request):
    return render(request,'admin/admin.html')

def detail(request, blog_id): # 요청과 객체의 번호를 받는다.
    blog_detail = get_object_or_404(Blog, pk = blog_id) 
    # pk = primary key
    # 객체들의 이름표, 구분자, 데이터의 대표값
    # get_object_or_404(클래스, 몇번객체(pk값))
    return render(request, 'detail.html', {'blog':blog_detail})
