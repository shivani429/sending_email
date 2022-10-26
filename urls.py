from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [
    
    path('email', views.email, name='email'),
    path('empdata', views.empdata, name='empdata'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
    path('edata', views.edata, name='edata'),
    path('mail', views.mail, name='mail'),
]
