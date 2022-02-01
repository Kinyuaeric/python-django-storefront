from django.urls import path
from . import views


#urlConfg
urlpatterns = [
     
    path('index',views.say_index),
    path('counter',views.say_counter),
    path('register',views.say_register,name='register'),
    path('login',views.say_login, name='login'),
   
]