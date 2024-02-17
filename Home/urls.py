from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('about/', views.about_page, name="about_page"),
]