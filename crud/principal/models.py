from django.db import models
from django.utils import timezone

# Create your models here.
class bd_crud(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=11,decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.produto
    
class Carrinho(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5,decimal_places=2)
    quantidade = models.IntegerField()
    preço_total_quantidade = models.DecimalField(max_digits=11,decimal_places=2)

    def __str__(self):
        return self.produto
    
class relatorio_de_vendas(models.Model):
    data = models.DateField(auto_now=timezone.datetime.now())
    produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=11,decimal_places=2)
    quantidade = models.IntegerField()
    total_quantidade = models.DecimalField(max_digits=11,decimal_places=2)

    def __str__(self):
        return self.produto
