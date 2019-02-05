from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios' : portfolios}) # {'key' : value }

def newport(request): #new.html 을 띄워주는 역할
    return render(request, 'newport.html')

def portcreate(request): #입력받은 내용을 db에 넣는 함수 
    portfolio = Portfolio() #blog라는 객체를 생성한다.
    portfolio.title = request.GET['title'] #blog 라는 객체안에 title을 받고 blog 객체에 추가한다.
    portfolio.image = request.GET['image']
    portfolio.description = request.GET['body'] # 마찬가지로 body를 blog 객체에 추가
    portfolio.save() # 쿼리셋 메소드중 하나인데, blog 라는 객체를 db에 저장해라. 
    #blog.delete() : db에 지워라
    return render(request, 'portfolio/portfolio.html')

    # redirect vs render
    # 상황에 따라 사용하는 방법이 달라짐.
    # 인자를 무엇을 주느냐에 따라 다름
    # render(요청, 실행, 키값)
    # redirect(url)
    # redirect 함수는 url을 받고, 다른 url(구글이라던지 네이버라던지) 을 받고, 함수를 수행하고 다른 url로 이동할수있음
    # render 함수는 세번째 함수로 키값을 받기에 파이썬 안에서 함수를 지지고 볶고서 이 프로젝트 내에서 활용하려고 할때 사용
