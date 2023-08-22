from django import forms

from core.models import Turma


class AddTurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'turno']
        labels = {
            'nome': 'Nome da turma',
            'turno': 'Turno da turma',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input-text'}),
            'turno': forms.Select(attrs={'class': 'input-select'}),
        }
