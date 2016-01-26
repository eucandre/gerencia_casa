__author__ = 'Carlos'
from app_casa.models import *
receitas = entradas()
despesas = saidas()
def saldo():
   if receitas.valor_entrada==None and despesas.valor_saida==None:
       return 0.0
   elif (int(receitas.valor_entrada)!=None) and (int(despesas.valor_saida)==None):
       return int(receitas.valor_entrada)
   elif (int(receitas.valor_entrada)!=None) and (int(despesas.valor_saida)!=None):
       return int(receitas.valor_entrada)-int(despesas.valor_saida)
