from django.urls import path
from . import views

app_name = 'chpa'
urlpatterns = [
    path(r'index', views.index, name='index'),
    path(r'search/<str:column>/<str:kw>', views.search, name='search'),
]
