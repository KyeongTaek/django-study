from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',views.posting, name="posting"),
    path('login/', views.login, name='login'),
]
