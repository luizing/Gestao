#interface simplificada para alterar e analisar os dados de uma planilha xls

import pandas as pd
from datetime import date


#Le o arquivo

planilha = pd.read_excel(r"planilha.ods")


#Parte 1 : Alteração com Datas

hoje = date.today()                             #salva a data atual
datas = planilha['Data']                        #compila as datas da tabela
format_data = hoje.strftime('20%y-%m-%d')       #formata a data no modelo da tabela


linha_hj = planilha.loc[planilha['Data'] == format_data]        #pega as informações da tabela correspondentes a data de hoje

print(linha_hj)

if linha_hj.empty == True:                      #caso não exista um linha correspondente a data de hoje
    format_data_df = "inserir as formulas para uma linha padronizada"
    planilha = planilha.append(format_data_df)





#Parte 2 : Gestão de Pedidos

pedidos = linha_hj['Pedidos']
linha_hj['Pedidos'] = 2
print(pedidos)