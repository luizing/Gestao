#interface simplificada para alterar e analisar os dados de uma planilha xls

import pandas as pd
from datetime import date


#Le o arquivo

planilha = pd.read_excel(r"planilha.ods")


#Parte 1 : Alteração com Datas

hoje = date.today()                             #salva a data atual
datas = planilha['Data']                        #compila as datas da tabela
format_data = hoje.strftime('20%y-%m-%d')       #formata a data no modelo da tabela

linha_hj = planilha.loc[planilha['Data'] == format_data]      #pega as informações da tabela correspondentes a data de hoje

dataindex = planilha[planilha['Data'] == format_data].index   #pega o index da data de hoje

if linha_hj.empty == True:                      #caso não exista um linha correspondente a data de hoje
    format_data_df = "inserir as formulas para uma linha padronizada"
    planilha = planilha.append(format_data_df)


#Parte 2 : Gestão de Pedidos
pedidos_df = linha_hj

num_pedido = pedidos_df.loc[dataindex,'Pedidos']

novos_pedidos = int(input("Quantos novos pedidos foram feitos: "))

pedido_final = num_pedido + novos_pedidos

planilha.loc[dataindex,'Pedidos'] = pedido_final
#planilha.to_excel('planilha.ods',index=False)

print(planilha)


#Parte 3 : Gestão de Vendas

vendas_df = linha_hj

num_vendas = vendas_df.loc[dataindex,'Vendas']

novas_vendas = int(input("Quantas vendas foram feitas: "))

vendas_final = num_vendas + novas_vendas

planilha.loc[dataindex,'Vendas'] = vendas_final

"""if planilha.at[dataindex,'Pedidos'] > vendas_final :
    planilha.loc[dataindex,'Pedidos'] = pedido_final - vendas_final

if planilha.at[dataindex,'Pedidos'] - vendas_final < 0 :
    planilha.loc[dataindex,'Pedidos'] = 0"""



planilha.to_excel('planilha.ods',index=False)

print(planilha)