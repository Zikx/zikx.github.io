from django import forms
from .models import Portfolio

class PortfolioPost(forms.ModelForm):
    class Meta:
        model = Portfolio #어떤 모델을 기반으로 할지 
        fields = ['title','image','description'] #모델의 타이틀, 바디, 이미지필드를 이용함