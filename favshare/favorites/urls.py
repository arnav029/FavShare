# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.favorites_list, name='favorites_list'),
    path('add/', views.add_favorite, name='add_favorite'),
]
