from django import forms
from helloworld.models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):
    #novos campos
    chefe = forms.BooleanField(
        label='Chefe ?',
        required=True,
    )

    biografia = forms.CharField(
        label= 'Biografia',
        required = False,
        widget = forms.Textarea
    )

    # Modelo base
    class Meta:

        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao',
        ]

        # Campos que não estarão no form
        exclude = [
            'tempo_de_servico'
        ]