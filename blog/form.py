from django import forms 
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog #어떤 모델을 기반으로 할지
        fields = ['title', 'body'] # 모델의 타이틀, 바디, 이미지필드를 이용함
        

    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])