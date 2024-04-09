from django.contrib import admin
from django.urls import path
from home import views
from .views import submit_contact

urlpatterns = [
    path("",views.index,name='home'),
    path('contact.html/',views.contact),
    path('.main.py/<str:community>',views.main),
    path('run-main/', views.execute_main, name='main'),
    path('submit_contact/', submit_contact, name='submit_contact'),
]