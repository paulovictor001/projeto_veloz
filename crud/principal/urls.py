from . import views
from django.urls import  path


urlpatterns = [
    path('',views.pg_estoque,name='pg_estoque'),
    path('deletar/',views.deletar_produto,name='deletar'),
    path('editar/',views.editar_produto,name='editar'),
    path('pagina_vendas/',views.pagina_vendas,name='pagina_vendas'),
    path('carrinho/<int:id>',views.carrinho,name='carrinho'),
    path('deleta_produtos_carrinho/<int:id>',views.deleta_produtos_carrinhos,name='deleta_produtos_carrinho'),
    path('concluir_vendas/',views.concluir_venda,name='concluir_vendas'),
    path('pesquisa/',views.pesquisa_produto,name='pesquisa'),
    path('pg_relatorio_vendas/',views.pg_relatorio_vendas,name='pg_relatorio_vendas')
]
