from django.urls import path

from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.AlunoListView.as_view(), name='listar'),
    path('criar/', views.AlunoCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', views.AlunoUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', views.AlunoDeleteView.as_view(), name='excluir'),
]