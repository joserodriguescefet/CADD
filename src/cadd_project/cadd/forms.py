from django import forms
from django.forms import TextInput, Textarea, Select, CheckboxInput, HiddenInput, \
                            NumberInput, TimeInput

from .models import Comissao, Membro, Horario, ItemHorario
from sca.models import Curso, Professor, Turma, Disciplina

class ComissaoForm(forms.ModelForm):
    """Classe de uso do sistema para o formulário de comissões"""

    def __init__(self,*args,**kwargs):
        super (ComissaoForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['curso'].queryset = Curso.objects.using('sca').distinct().order_by('nome')
        self.fields['curso'].empty_label = 'Selecione o curso'

    class Meta:
        model = Comissao
        exclude = (id, )
        widgets = {
            'curso': Select(attrs={'class': 'form-control',
                                   'data-rules': 'required'}),
            'descricao': Textarea(attrs={'class': 'form-control',
                                         'data-rules': 'required',
                                         'placeholder': 'Informe a descrição'})
        }

class MembroForm(forms.ModelForm):
    """Classe de uso do sistema para o formulário de membros"""

    def __init__(self,*args,**kwargs):
        super (MembroForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['professor'].queryset = Professor.objects.using('sca').distinct().order_by('nome')
        self.fields['professor'].empty_label = 'Selecione o professor'

    class Meta:
        model = Membro
        exclude = (id, 'comissao', )
        widgets = {
            'professor': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'}),
            'portaria': TextInput(attrs={'class': 'form-control',
                                         'data-rules': 'required',
                                         'placeholder': 'Informe a portaria'}),
            'presidente': CheckboxInput(attrs={'class': 'form-control'}),
            'ativo': CheckboxInput(attrs={'class': 'form-control'})
        }


class HorarioForm(forms.ModelForm):
    """Classe de uso do sistema para o formulário de horários"""

    def __init__(self,*args,**kwargs):
        super (HorarioForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['curso'].queryset = Curso.objects.using('sca').distinct().order_by('nome')
        self.fields['curso'].empty_label = 'Selecione o curso'

    class Meta:
        model = Horario
        exclude = (id, )
        widgets = {
            'curso': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required',
                                         'empty_label': 'Selecione o curso'}),
            'ano': NumberInput(attrs={'class': 'form-control',
                                         'data-rules': 'required',
                                         'min': 2016, 'max': 2050, 'step': 1,
                                         'empty_label': 'Selecione o ano'}),
            'periodo': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'})
        }


class ItemHorarioForm(forms.ModelForm):
    """Classe de uso do sistema para o formulário de itens de horário"""

    def __init__(self,*args,**kwargs):
        super (ItemHorarioForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['turma'].queryset = Turma.objects.using('sca').distinct().order_by('codigo')
        self.fields['disciplina'].queryset = Disciplina.objects.using('sca').distinct().order_by('nome')
        self.fields['professor'].queryset = Professor.objects.using('sca').distinct().order_by('nome')
        self.fields['periodo'].empty_label = 'Selecione o período'
        self.fields['turma'].empty_label = 'Selecione a turma'
        self.fields['disciplina'].empty_label = 'Selecione a disciplina'
        self.fields['professor'].empty_label = 'Selecione o professor'
        self.fields['departamento'].empty_label = 'Selecione o departamento'

    class Meta:
        model = ItemHorario
        exclude = (id, 'horario', )
        widgets = {
            'periodo': TextInput(attrs={'class': 'form-control',
                                         'data-rules': 'required',
                                         'placeholder': 'Informe o periodo'}),
            'turma': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'}),
            'disciplina': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'}),
            'professor': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'}),
            'diasemana': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'}),
            'inicio': TimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Informe a hora de início'}),
            'fim': TimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Informe a hora final'}),
            'departamento': Select(attrs={'class': 'form-control',
                                         'data-rules': 'required'})
        }
