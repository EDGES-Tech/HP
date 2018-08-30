from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'top'
urlpatterns = [
    path('index', views.top,name='top')
]

#settings.pyで追加した画像がある場所を指定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)