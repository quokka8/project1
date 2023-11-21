from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('book-catalog/', views.book_catalog, name='book-catalog'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)