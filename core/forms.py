from django import forms

class buscaForm(forms.ModelForm):
    cidade = forms.ModelChoiceField(queryset=cidade.objects.all(),\
    empty_label='Selecione a cidade...',\
    widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        # abstract = True
        model = cidade
        fields = [
            'cidade',
        ]


class escolaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nome da escola',
        }
    ))

    quantidade_alunos = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Quantidade de Alunos',
        }
    ))

    renda = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Investimento recebido',
        }
    ))

    ocorrencias = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Observação',
            'rows': '3',
        }
    ))

    quantidade_professores = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ocorrências',
        }
    ))

    
    class Meta:
        model = escolas
        fields = [
            'nome', 
            'quantidade_alunos',
            'renda',
            'ocorrencias',
            'quantidade_professores'
        ]