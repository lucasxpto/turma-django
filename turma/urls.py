from django.urls import path

from . import views

app_name = 'turmas'

urlpatterns = [
    path('', views.TurmaListView.as_view(), name='listar'),
    path('criar/', views.TurmaCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', views.TurmaUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', views.TurmaDeleteView.as_view(), name='excluir'),
]