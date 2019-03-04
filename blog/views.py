from django.shortcuts import render , get_object_or_404, redirect
from django.utils import timezone #timezone import 
from django.core.paginator import Paginator #pagination을 위함
from .models import Blog
from .form import BlogPost

# Create your views here.

def blog(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all().order_by('-id')#블로그 모든 글들을 대상으로 

    # 블로그 객체 3개를 한 페이지로 자른다
    paginator = Paginator(blog_list, 3) # blog_list객체를 대상으로 3개의 객체를 하나의 페이지로 삼겠다.
                                        # 페이지 3개씩 자름
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page') # key값이 page인 dict형 value 값을 page변수에 담아줌
    #request된 페이지를 얻어온 뒤 return 함
    posts = paginator.get_page(page) #get_page(page) page번호의 페이지를 가져오는함수
    #결과적으로 request에 해당하는 페이지의 번호가 posts에 담기게됨
    return render(request,'blog.html', {'blogs' : blogs, 'posts':posts })

def detail(request, blog_id): # 요청과 객체의 번호를 받는다.
    blog_detail = get_object_or_404(Blog, pk = blog_id)     
    # pk = primary key
    # 객체들의 이름표, 구분자, 데이터의 대표값
    # get_object_or_404(클래스, 몇번객체(pk값))
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): #new.html 을 띄워주는 역할
    return render(request, 'new.html')

def create(request): #입력받은 내용을 db에 넣는 함수 
    blog = Blog() #blog라는 객체를 생성한다.
    blog.title = request.GET['title'] #blog 라는 객체안에 title을 받고 blog 객체에 추가한다.
    blog.body = request.GET['body'] # 마찬가지로 body를 blog 객체에 추가
    blog.pub_date = timezone.datetime.now() # blog_pub 에는 지금시간을 저장하라.
    blog.save() # 쿼리셋 메소드중 하나인데, blog 라는 객체를 db에 저장해라. 
    #blog.delete() : db에 지워라
    return redirect('/blog/'+str(blog.id)) # url로 넘겨라. blog.id 는 int형으로 선언했기에 문자열로 강제형변환

    # redirect vs render
    # 상황에 따라 사용하는 방법이 달라짐.
    # 인자를 무엇을 주느냐에 따라 다름
    # render(요청, 실행, 키값)
    # redirect(url)
    # redirect 함수는 url을 받고, 다른 url(구글이라던지 네이버라던지) 을 받고, 함수를 수행하고 다른 url로 이동할수있음
    # render 함수는 세번째 함수로 키값을 받기에 파이썬 안에서 함수를 지지고 볶고서 이 프로젝트 내에서 활용하려고 할때 사용

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid(): # form에 입력이 되었는지를 확인하는 함수 맞으면 1리턴 
            post = form.save(commit=False) # 객체를 가져오되, 저장하지않고 가져온다!
            post.pub_date = timezone.now() 
            post.save()
            return redirect('blog')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})