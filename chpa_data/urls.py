from django.urls import path
from . import views

app_name = 'chpa_data'
urlpatterns = [
    path(r'index', views.index, name='index'),
]
