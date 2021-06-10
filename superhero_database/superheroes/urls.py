from django.urls import path
from .import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='hero_detail'),
    path('create/', views.create, name='create_superhero'),
]


