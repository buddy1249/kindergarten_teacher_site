from cgi import parse

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),# http://127.0.0.1:8000
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('parent/', views.parent, name='parent'),
    path('progress/', views.progress, name='progress'),
    path('ntd/', views.ntd, name='ntd'),
]