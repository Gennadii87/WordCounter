from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_file, name='load'),
    path('wordcount/', views.word_count, name='word_count'),
    path('clear/', views.clear_memory, name='clear_memory'),
]
