from django.urls import path
from . import views
from .views import HomePageListView


urlpatterns = [
    #path('', views.index, name='home'),
    path('', HomePageListView.as_view(), name='home'),
]