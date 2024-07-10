from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lists, name='post_lists'),
]