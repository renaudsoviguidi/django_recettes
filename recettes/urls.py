from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recettes.index'),
    path('create/', views.create, name='recettes.create'),
    path('create/store', views.store, name='recettes.store'),
    path('edit/<int:id>/', views.edit, name='recettes.edit'),
    path('edit/update/<int:id>/', views.update, name='recettes.update'),
    path('delete/<int:id>/', views.delete, name='recettes.delete'),
]