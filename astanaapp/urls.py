from django.urls import path
from . import views, admin, views_auth

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views_auth.registration, name='registration'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    
]