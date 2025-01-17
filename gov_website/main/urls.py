from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home_logged_in/', views.home_logged_in, name='home_logged_in'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
