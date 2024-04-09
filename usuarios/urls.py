from django.urls import path, include
from . import views

urlpatterns = [
        path('users/', views.get_users, name='get_all_users'),
        path('user/<str:cpf>/', views.get_by_cpf, name='get_user_by_cpf'),
        path('login/', views.login, name='login'),
        path('login_view/', views.login_view, name='login_view'),
        path('cadastro/', views.cadastro_view, name='cadastro_view'),
    
]
