from django.contrib import admin

from .models import Aluno, Turma, Boletim, Disciplina


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'disciplinasturma',)

    def disciplinasturma(self, turma):
        return ', '.join(d.nome for d in turma.disciplina_set.all()[:2])

    disciplinasturma.short_description = 'Disciplinas'


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomecompleto', 'data_nascimento', 'endereco', 'turma')

    def nomecompleto(self, aluno):
        return f'{aluno.nome} {aluno.sobrenome}'


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'aluno')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')
