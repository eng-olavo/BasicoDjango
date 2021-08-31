from django.urls import path
from . import views


#/hello
urlpatterns = [
    path('',views.home)
]