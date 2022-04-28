from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/',views.home, name="home"),
    path('all_clubs/',views.all_clubs, name="all_clubs"),
    path('home/<slug:club_slug>',views.a_club, name="aclub"),
    path('login/', 
        LoginView.as_view(template_name='home/login.html'),name="login"
    ),
    path('register/',views.register, name="register")
]
