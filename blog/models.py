from django.db import models

# Create your models here.
class Blog(models.Model):
        title = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        body = models.TextField()

        def __str__(self):
            return self.title # 제목을 리턴한다.
        
        def summary(self): # self : 자기 자신을 받음
            return self.body[:100] # 100글자를 상한선으로 리턴하라.