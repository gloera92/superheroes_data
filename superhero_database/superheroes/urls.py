from django.urls import path
from .import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail_superhero'),
    path('create/', views.create, name='create_superhero'),
    path('update/<int:superhero_id>/', views.update, name='update_superhero'),
    path('delete/<int:superhero_id>/', views.delete, name='delete_superhero')
]


