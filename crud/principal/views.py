from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import bd_crud,Carrinho,relatorio_de_vendas
from datetime import datetime

def pg_estoque (request):
    if request.method == 'GET':
        print('get')
        bd = bd_crud.objects.all()
        
        return render(request,'pg_estoque.html',{'dados':bd})
    
    elif request.method == 'POST':
        dados = request.POST
        print(dados)
        produto = request.POST.get('produto')
        preço = request.POST.get('preço')
        estoque = request.POST.get('estoque')
        print(produto,preço,estoque)

        bd = bd_crud(
            produto=produto,
            valor=preço,
            estoque=estoque,
        )
        bd.save()

        return redirect('pg_estoque')
    
def pesquisa_produto(request):
    if request.method == 'POST':
        pesquisa = request.POST.get('pesquisa_produto')
        resultado_pesquisa = bd_crud.objects.filter(produto__contains=pesquisa)

        if len(resultado_pesquisa) == 0:
            return redirect('pg_estoque')
        else:
            return render(request,'pg_estoque.html',{'dados':resultado_pesquisa})
        
# deleta produtos do estoque
def deletar_produto(request):
    id_produto_deletado = request.POST.get('id_produto')
    bd = bd_crud.objects.get(id=id_produto_deletado)
    bd.delete()
    
    return redirect('pg_estoque')

def editar_produto(request):
    resposta = request.POST
    id_produto = int(resposta.get('id_produto'))
    produto = resposta.get('produto')
    valor = resposta.get('valor')
    estoque = resposta.get('estoque')

    print(id_produto,produto,valor,estoque)

    tb_estoque = bd_crud.objects.get(id=id_produto)
    tb_estoque.produto = produto
    tb_estoque.valor = valor 
    tb_estoque.estoque = estoque

    tb_estoque.save()

    return redirect('pg_estoque')


def pagina_vendas(request):
    if request.method == 'GET':
        bd = bd_crud.objects.all()
        carrinho = Carrinho.objects.all()

        valores_totais = Carrinho.objects.values_list('preço_total_quantidade') # pega apenas a coluna do preço total
        total = 0
        for c in valores_totais:
            total += c[0]
        
        print(total)

        return render(request,'pagina_vendas.html',{'dados':bd,'carrinho':carrinho,'total':total})
    
    elif request.method == 'POST':
        pesquisa = request.POST.get('nome_produto')
        bd = bd_crud.objects.filter(produto__contains=pesquisa)
        print(bd)
        if len(bd) == 0:
            print('aqui')
            return redirect('pagina_vendas')
        
        return render(request,'pagina_vendas.html',{'dados':bd})

def carrinho(request,id):
    bd = bd_crud.objects.get(id=id)
    nome = bd.produto
    preço = float(bd.valor)
    quantidade = float(request.POST['quantidade'])
    preço_total_quantidade = quantidade*preço

    car = Carrinho(
        produto = nome,
        valor = preço,
        quantidade = quantidade,
        preço_total_quantidade = preço_total_quantidade
    )
    car.save()

    return redirect('pagina_vendas')

# deleta produtos do carrinho
def deleta_produtos_carrinhos(request,id):
    bd = Carrinho.objects.get(id=id)
    bd.delete()
    return redirect('pagina_vendas')

def concluir_venda(request):
    tb_carrinho = Carrinho.objects.all()
    for c in tb_carrinho:
        print(c.produto,c.quantidade,'-=-=-=-=')
        estoque = bd_crud.objects.filter(produto__exact=c.produto).values('estoque')[0]['estoque']
        bd = bd_crud.objects.get(produto=c.produto)
        novo_estoque = estoque-c.quantidade

        if novo_estoque<0:
            print('não a quandidade suficiente no estoque')
            return redirect('pagina_vendas')
        
        bd.estoque =  novo_estoque # atualiza o estoque
        bd.save()
        

    # trasfera as vendas para o relatorio de vendas
    for row in tb_carrinho:
        tb_relatorio = relatorio_de_vendas(
        produto = row.produto,
        valor = row.valor,
        quantidade = row.quantidade,
        total_quantidade = row.preço_total_quantidade,
        )

        tb_relatorio.save()

    tb_carrinho.delete()


    return redirect('pagina_vendas')

def pg_relatorio_vendas(request):
    data_atual = datetime.now().date()

    if request.method == "GET":
        tb_relatorio = relatorio_de_vendas.objects.filter(data__exact=data_atual)

        return render(request,'pg_relatorio_vendas.html',{'relatorio':tb_relatorio})
    
    elif request.method == "POST":
        datas = request.POST

        data_inicial = datas['data_inicial']
        data_final = datas['data_final']
        print(data_inicial,data_final)

        tb_relatorio_coluna_data = relatorio_de_vendas.objects.filter(data__exact=data_inicial)
        print(tb_relatorio_coluna_data,'-=-=-=-=data inicial-=-=-=-')
        # verifica se a data é valida
        if len(tb_relatorio_coluna_data) == 0 :
            return redirect('pg_relatorio_vendas')

        return render(request,'pg_relatorio_vendas.html',{'relatorio':tb_relatorio_coluna_data})

# Create your views here.
