from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('About/',views.index,name ='about'),
    path('Blog/',views.index,name ='blog'),
    path('Classes/',views.index,name ='class'),
]