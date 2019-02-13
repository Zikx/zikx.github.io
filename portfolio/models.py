from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255) #title
    image = models.ImageField(upload_to='images/') # 업로드된 이미지들을 images폴더 안에 넣으라는 의미
    description = models.CharField(max_length=500) # 내용

    def __str__(self):
        return self.title # admin 상에서 object 넘버가 아닌 타이틀이 뜨기로

#pip install pillow = python으로 이미지를 효율적으로 표현할수있게 해주는 패키지 