import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='whitegrid')

# Configuração da Página
st.set_page_config(
    page_title="Análise de Previsão de Renda",
    page_icon="💰",
    layout="wide",
)

st.title('🔎 Análise Exploratória da Previsão de Renda')

# Carregamento dos Dados
renda = pd.read_csv('./input/previsao_de_renda.csv')

# Filtros Interativos
st.sidebar.header('Filtros')
sexo = st.sidebar.multiselect('Sexo', renda['sexo'].unique(), default=renda['sexo'].unique())
tipo_renda = st.sidebar.multiselect('Tipo de Renda', renda['tipo_renda'].unique(), default=renda['tipo_renda'].unique())

# Aplicando Filtros
renda_filtrado = renda[(renda['sexo'].isin(sexo)) & (renda['tipo_renda'].isin(tipo_renda))]

# Gráficos ao longo do tempo
st.subheader('📊 Evolução da Renda ao Longo do Tempo')
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

# Gráficos Bivariados
st.subheader('📊 Comparações Bivariadas')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)    


st.caption('Projeto acadêmico desenvolvido para análise exploratória de renda.')
  