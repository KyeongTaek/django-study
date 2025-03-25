from django.urls import path
from django.contrib import admin

from main.views import index, posting, login

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/',posting, name="posting"),
    path('login/', login, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
