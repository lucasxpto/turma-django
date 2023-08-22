from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from core.models import Aluno
from aluno.forms import AddAlunoForm


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AddAlunoForm
    template_name = 'aluno/aluno_form.html'

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.save()
        messages.success(self.request, 'Aluno cadastrado com sucesso.')
        return redirect('alunos:listar')

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar aluno.')
        print(form.errors)
        return super().form_invalid(form)


class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(AlunoListView, self).get_queryset()
        return queryset.order_by('nome')


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AddAlunoForm
    template_name = 'aluno/aluno_form.html'

    def get_success_url(self):
        return reverse_lazy('alunos:listar')

    def form_valid(self, form):
        messages.success(self.request, 'Aluno atualizada com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar aluno.')
        return super().form_invalid(form)


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = reverse_lazy('alunos:listar')

    def get_success_url(self):
        messages.success(self.request, "Aluno excluída com sucesso.")
        return super().get_success_url()

