from unicodedata import name
from django.urls import path
from. import views

urlpatterns =[
    
    path('login/', views.login,),
    path('login/home/', views.home),
    path('login/cadastro/', views.cadastro),

]

