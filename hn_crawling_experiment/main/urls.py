from django.urls import path
from django.contrib import admin

from main.views import PostViewSet, login

from django.conf.urls.static import static
from django.conf import settings

post_specific_view = PostViewSet.as_view({
    'get': 'retrieve',
    'post': 'create_post',
})

post_list_view = PostViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('',post_list_view, name='index'),
    path('<int:pk>/',post_specific_view, name="posting"),
    path('login/', login, name='login'),
    path('new_post/',post_specific_view, name='new_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
