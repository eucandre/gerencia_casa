from django.db import models

TIPO = ((u'Mensal','Mensal'),(u'Sazonal','Sazonal'))

class entradas(models.Model):
    nome_entrada = models.CharField(max_length=150)
    tipo_de_entrada = models.CharField(choices=TIPO, max_length=8)
    data_entrada = models.DateField()
    valor_entrada = models.FloatField()
    responsavel_por_entrada = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome_entrada

class saidas(models.Model):
    nome_saida = models.CharField(max_length=150)
    tipo_de_saida = models.CharField(choices=TIPO, max_length=8)
    data_saida = models.DateField()
    valor_saida = models.FloatField()
    responsavel_por_saida = models.CharField(max_length=150)
    motivo_saida = models.TextField()

    def __unicode__(self):
        return self.nome_saida

class caixa(models.Model):
    em_caixa = models.FloatField()
    data_da_atualizacao = models.DateField()

    def __unicode__(self):
        return self.em_caixa

class investimentos_adiquiridos(models.Model):
    nome_investimento = models.CharField(max_length=150)
    valor_investido = models.FloatField()
    data_investimento = models.DateField()

class Planos(models.Model):
    nome_plano = models.CharField(max_length=150)
    valor_para_realizar = models.FloatField()
    detalhes_plano = models.TextField()

    def __unicode__(self):
        return self.nome_plano



