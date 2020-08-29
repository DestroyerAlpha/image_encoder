from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='form'),
    path('out/<int:imgid>', views.result, name='output'),
]
