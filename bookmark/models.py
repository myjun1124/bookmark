from django.db import models
from django.urls import reverse

# Create your models here.

# 이게 테이블이 되는 것
class Bookmark(models.Model): # models에서 Model 상속받기
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # reverse 메소드는 URL 패턴의 이름과 추가 인자를 전달받아 URL 생성
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])