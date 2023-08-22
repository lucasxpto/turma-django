from datetime import date

from django import forms

from core.models import Aluno


class AddAlunoForm(forms.ModelForm):
    class Meta:

        model = Aluno
        fields = ['nome', 'sobrenome', 'endereco', 'data_nascimento', 'turma']
        labels = {
            'nome': 'Nome do aluno',
            'sobrenome': 'Sobrenome',
            'endereco': 'Endereço',
            'data_nascimento': 'Data de nascimento',
            'turma': 'Turma',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input-text'}),
            'sobrenome': forms.TextInput(attrs={'class': 'input-text'}),
            'endereco': forms.TextInput(attrs={'class': 'input-text'}),
            'data_nascimento': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'input-text',
                    'type': 'date',
                    'max': date.today(),
                },
            ),
            'turma': forms.Select(attrs={'class': 'input-select'}),
        }
