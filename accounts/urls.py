from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    #path('logout/', views.logout, name='logout'),
]
