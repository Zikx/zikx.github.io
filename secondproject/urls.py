from django.contrib import admin
from django.urls import path , include

from django.conf import settings # settings에 있는 url을 가져올것이기때문
from django.conf.urls.static import static # 걍외워라~
import blog.views
import portfolio.views




urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static 부분은 병렬적으로 추가한것인데 
# urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 와 같은 의미임.