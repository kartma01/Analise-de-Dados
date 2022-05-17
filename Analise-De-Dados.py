import plotly.express as px
import pandas as pd

#1 IMPORTAR A BASE DE DADOS
tabela = pd.read_csv('telecom_users.csv')

#2 VISUALIZAR A BASE DE DADOS
#ENTENDER AS INFORMAÇÕES QUE VOCÊ TEM
#PARA CORRIGIR AS CAGADAS DA BASE DE DADOS

# axis = 0 -> linha, axis = 1 -> coluna
tabela = tabela.drop('Unnamed: 0',axis=1)
print(tabela)

#3 TRATAMENTO DE DADO
#VER/AJUSTAR QUALQUE VALOR QUE ESTA SENDO RECONHECIDO DE FORMA ERRADA
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

#VALORES VAZIOS
# ANY = algum valor vazio, all = Completamente vazias
#COLUNAS VAZIAS - EXCLUI
tabela = tabela.dropna(how ='all', axis=1)

#LINHAS COM ALGUM VALOR VAZIO -> EXCLUI
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())
#4 ANALISE SIMPLES -> ENTENDER COMO ESTÃO ACONTECENDO OS CANCELAMENTOS
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) #ver em porcentagem

#5ANÁLISE MAIS COMPELTA -> ENTENDER A CAUSA DOS CANCELAMENTOS   /POSSIVEIS SOLUÇÕES
#CRIAR O GRAFICO
#para cada coluna da nossa base de dados, eu quero criar 1 gráfico
for coluna in tabela.columns:
    print(coluna)
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    #EXIBE/MOSTRA O GRÁFICO
    grafico.show()
