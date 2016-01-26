__author__ = 'Carlos'
from django import forms
from models import *
import valor_em_caixa
import datetime

TIPO = ((u'Mensal','Mensal'),(u'Sazonal','Sazonal'))

class FormEntrada(forms.ModelForm):
    nome_entrada = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    tipo_de_entrada = forms.ChoiceField(choices=TIPO,widget=forms.Select(attrs={"class":"form-control"}))
    data_entrada = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}))
    valor_entrada = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    responsavel_por_entrada = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    class Meta:
        model = entradas
        fields = ['nome_entrada','tipo_de_entrada','data_entrada','valor_entrada','responsavel_por_entrada']

class FormSaida(forms.ModelForm):
    nome_saida = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    tipo_de_saida = forms.ChoiceField(choices=TIPO,widget=forms.Select(attrs={"class":"form-control"}))
    data_saida = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","data-inputmask=":"99.99.9999", "data-toggle":"masked"}))
    valor_saida = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    responsavel_por_saida = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","style":"width:20%;"}))
    motivo_saida = forms.Textarea()

    class Meta:
        model = saidas
        fields = ['nome_saida','tipo_de_saida','data_saida','valor_saida','responsavel_por_saida','motivo_saida']

class FormCaixa(forms.ModelForm):
    aux = valor_em_caixa
    hoje= datetime.date
    em_caixa = forms.FloatField(initial=aux.saldo, widget=forms.TextInput(attrs={"class":"form-control", "disabled":"disabled"}))
    data_da_atualizacao = forms.DateField(initial=hoje.today(),widget=forms.DateInput(format='%d.%m.%Y',attrs={"class":"form-control","disabled":"disabled"}))

    class Meta:
        model = caixa
        fields = ['em_caixa','data_da_atualizacao']