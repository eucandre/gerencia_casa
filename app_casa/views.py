from django.shortcuts import *
from forms import *
import datetime

def pagina_inicial(request):
    #serao analisados os 5 ultimos meses para o grafico de receitas, por enquanto nao esta editado

    tamanho_receitas = len(entradas.objects.all())
    tamanho_despesas = len(saidas.objects.all())
    nome_saida = ""
    if tamanho_despesas ==0:
        nome_saida = "Nada"
        valor = 0
    else:
        obj_despesa = saidas.objects.get(pk=tamanho_despesas)
        nome_despesa = obj_despesa.nome_saida
    return render_to_response("arquivos_para_sistema/pagina_apresentacao.html",
        {"valor":valor, "saida":nome_saida},
                              context_instance=RequestContext(request))

def receita_casa(request):
    if request.method =='post':
        form = FormEntrada(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormEntrada()

    return render_to_response('arquivos_para_sistema/receitas_da_casa.html',{"form":form},context_instance=RequestContext(request))

def despesas_casa(request):
    if request.method =='post':
        form = FormSaida(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormSaida()

    return render_to_response('arquivos_para_sistema/despesas.html',{"form":form},context_instance=RequestContext(request))


def caixa(request):
    if request.method =='post':
        form = FormCaixa(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormCaixa()
    return render_to_response("arquivos_para_sistema/caixa.html",{"form":form},context_instance=RequestContext(request))