from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginreq, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_req, name="logout"),
    path('files/', views.files, name="files"),
]