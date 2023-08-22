from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from core.models import Turma
from turma.forms import AddTurmaForm


class TurmaCreateView(CreateView):
    model = Turma
    form_class = AddTurmaForm
    template_name = 'turma/turma_form.html'

    def form_valid(self, form):
        turma = form.save(commit=False)
        turma.save()
        messages.success(self.request, 'Turma cadastrada com sucesso.')
        return redirect('turmas:listar')

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar turma.')
        print(form.errors)
        return super().form_invalid(form)


class TurmaListView(ListView):
    model = Turma
    template_name = 'turma/turma_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(TurmaListView, self).get_queryset()
        return queryset.order_by('nome')


class TurmaUpdateView(UpdateView):
    model = Turma
    form_class = AddTurmaForm
    template_name = 'turma/turma_form.html'

    def get_success_url(self):
        return reverse_lazy('turmas:listar')

    def form_valid(self, form):
        messages.success(self.request, 'Turma atualizada com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar turma.')
        return super().form_invalid(form)


class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = 'turma/turma_confirm_delete.html'
    success_url = reverse_lazy('turmas:listar')

    def get_success_url(self):
        messages.success(self.request, "Turma excluída com sucesso.")
        return super().get_success_url()

