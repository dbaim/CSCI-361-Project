from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_welcome, name='welcome_page'),
    path('login', views.login, name='login'),
    path('about-us', views.about, name='about')
]
