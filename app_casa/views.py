from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.shortcuts import *
from forms import *
import datetime

@login_required()
def pagina_inicial(request):
    global maior
    #serao analisados os 5 ultimos meses para o grafico de receitas, por enquanto nao esta editado

    tamanho_receitas = len(entradas.objects.all())
    tamanho_despesas = len(saidas.objects.all())
    maior = 0
    maior1=maior
    maior2=maior
    maior3=maior
    maior4=maior
    maior5=maior
    nome_saida1 =""
    nome_saida2 =""
    nome_saida3 =""
    nome_saida4 =""
    nome_saida5 =""
    nome_saida = ""
    if tamanho_despesas ==0:
        nome_saida = "Nada"
        nome_saida1 = "Nada"
        nome_saida2 = "Nada"
        nome_saida3 = "Nada"
        nome_saida4 = "Nada"
        nome_saida5 = "Nada"
        valor = 0
        maior =0

        #obj_despesa = saidas.objects.get(pk=tamanho_despesas)
        #nome_saida = obj_despesa.nome_saida
        #valor = obj_despesa.valor_saida

    elif tamanho_despesas >=5:
        obj_despesa1 = saidas.objects.get(pk=tamanho_despesas)
        obj_despesa2 = saidas.objects.get(pk=tamanho_despesas-1)
        obj_despesa3 = saidas.objects.get(pk=tamanho_despesas-2)
        obj_despesa4 = saidas.objects.get(pk=tamanho_despesas-3)
        obj_despesa5 = saidas.objects.get(pk=tamanho_despesas-4)
        lista_cinco_maiores = []

        if obj_despesa1.valor_saida>maior:
            maior1 = obj_despesa1.valor_saida
            nome_saida1 = obj_despesa1.nome_saida
            valor = maior1


        elif obj_despesa2.valor_saida>maior:
            maior2 = obj_despesa2.valor_saida
            nome_saida2 = obj_despesa2.nome_saida
            valor2 = maior2

        elif obj_despesa3.valor_saida>maior:
            maior3 = obj_despesa3.valor_saida
            nome_saida3 = obj_despesa3.nome_saida
            valor3 = maior3

        if obj_despesa4.valor_saida>maior:
            maior4 = obj_despesa4.valor_saida
            nome_saida4 = obj_despesa4.nome_saida
            valor4 = maior4

        if obj_despesa5.valor_saida>maior:
            maior5 = obj_despesa5.valor_saida
            nome_saida5 = obj_despesa5.nome_saida
            valor5 = maior5
        lista_cinco_maiores=[maior1,maior2,maior3,maior4,maior5].sort()
        lista_nomes_saidas = [nome_saida1,nome_saida2,nome_saida3,nome_saida4,nome_saida5]

    return render_to_response("arquivos_para_sistema/pagina_apresentacao.html",
        {"valor":maior1,"valor2":maior2,"valor3":maior3,"valor4":maior4,"valor5":maior5, "saida1":nome_saida1,"saida2":nome_saida2,"saida3":nome_saida3,"saida4":nome_saida4,"saida5":nome_saida5,},
                              context_instance=RequestContext(request))
@login_required()
def receita_casa(request):
    if request.method =='post':
        form = FormEntrada(request.FILES, request.POST)
        if form.is_valid():
            item =form.save(commit=false)
            item.save()
    else:
        form = FormEntrada()

    return render_to_response('arquivos_para_sistema/receitas_da_casa.html',{"form":form},context_instance=RequestContext(request))
#@login_required("/")
def despesas_casa(request):
    if request.method =='post':
        form = FormSaida(request.FILES, request.POST)
        if form.is_valid():
            item =form.save(commit=false)
            item.save()
    else:
        form = FormSaida()

    return render_to_response('arquivos_para_sistema/despesas.html',{"form":form},context_instance=RequestContext(request))

#@login_required("/")
def caixa(request):
    if request.method =='post':
        form = FormCaixa(request.FILES, request.POST)
        if form.is_valid():
            item =form.save(commit=false)
            item.save()
    else:
        form = FormCaixa()
    return render_to_response("arquivos_para_sistema/caixa.html",{"form":form},context_instance=RequestContext(request))