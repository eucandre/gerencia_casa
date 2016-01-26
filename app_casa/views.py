from django.shortcuts import *
from forms import *
import datetime

def pagina_inicial(request):
    #serao analisados os 5 ultimos meses para o grafico de receitas, por enquanto nao esta editado

    tamanho_receitas = len(entradas.objects.all())
    tamanho_despesas = len(saidas.objects.all())

    obj_receitas=entradas.objects.get(pk=tamanho_receitas)
    obj_despesas=entradas.objects.get(pk=tamanho_despesas)

    nome_gasto = obj_despesas.nome_saida
    valor = obj_despesas.valor_saida
    lista_produtos_valorizados = []
    maior = 0
    maior1 = 0
    maior2 = 0
    maior3 = 0
    maior4 = 0
    maior5 = 0

    if nome_gasto=="":
        nome_gasto = "Gasto 0"
        valor = 0

    if nome_gasto!="":
        if valor>maior:
            lista_produtos_valorizados.insert(0,valor)
            maior = valor
        elif valor<=maior:
            lista_produtos_valorizados.append(valor)
    if len(lista_produtos_valorizados)==5:
          maior1 = lista_produtos_valorizados[0]
          maior2 = lista_produtos_valorizados[1]
          maior3 = lista_produtos_valorizados[2]
          maior4 = lista_produtos_valorizados[3]
          maior5 = lista_produtos_valorizados[4]


    return render_to_response("arquivos_para_sistema/pagina_apresentacao.html",
        {"saida":nome_gasto, "gasto":valor},
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