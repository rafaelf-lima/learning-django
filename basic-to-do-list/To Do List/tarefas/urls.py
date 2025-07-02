from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefa_list, name = 'tarefa_list'),
    path('update/<int:pk>/', views.tarefa_update, name='tarefa_update'),
    path('delete/<int:pk>/', views.tarefa_delete, name='tarefa_delete'),
]



