from django.urls import path
from . import views

app_name = 'network_drawer'
urlpatterns = [
    #path('', views.entry, name='entry'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    #path('index/', views.IndexView.as_view(), name="index"),
    path('index/', views.index, name="index"),
    path('create/', views.UserCreateView.as_view(), name="create"),
    path('top/', views.top, name='top'),
    path('top/network', views.draw_network, name='draw_network'),
    path('top/network/<int:pk>', views.draw_my_network, name='draw_my_network'),
    path('ones_view', views.ones_view, name='ones_view'),
    #path('my_network/', views.my_network, name='my_network'),
    # path('top/network0', views.draw_my_network, name='draw_my_network'),
    #path('', views.List_Player.as_view()),

]
