from django.urls import path
from . import views


urlpatterns = [
     path('', views.lista_post, name='lista_post'),
     path('post/<int:pk>/', views.detalha_post, name='detalha_post'),
     path('post/novo/', views.cria_post, name='cria_post'),
     path('post/<int:pk>/editar/', views.edita_post, name = 'edita_post'),
     path('post/<int:pk>/deletar/', views.deleta_post, name = 'deleta_post'),
]


