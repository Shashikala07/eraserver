
from django.urls import path

from rec import views

urlpatterns = [
    path('', views.index, name='index'),
    

]