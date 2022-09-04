from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="Logout"),
    path('register/', views.registerPage, name="Register"),
    path('home/', views.home, name="Home"),
    path('cryptoMK/', views.cryptoMK, name="CryptoMK"),
    path('cryptoEN/', views.cryptoEN, name="CryptoEN"),
    path('aiMK/', views.aiMK, name="aiMK"),
    path('aiEN/', views.aiEN, name="aiEN"),
    path('ipMK/', views.ipMK, name="ipMK"),
    path('ipEN/', views.ipEN, name="ipEN"),
    path('oopMK/', views.oopMK, name="oopMK"),
    path('oopEN/', views.oopEN, name="oopEN"),
    path('coursesEN/', views.coursesEN, name="coursesEN"),
    path('coursesMK/', views.coursesMK, name="coursesMK"),
]