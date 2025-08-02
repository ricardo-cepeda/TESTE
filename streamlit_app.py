import streamlit as st

st.title('Simulador de Escala FTC')

num_alunos = st.number_input('Número de alunos', value=188)
ticket_medio = st.number_input('Ticket médio mensal (R$)', value=210.0)
alunos_unidade = st.number_input('Alunos por unidade (média)', value=62.6)
meta_anual = st.number_input('Meta anual de faturamento (R$)', value=1_000_000)

faturamento_mensal = num_alunos * ticket_medio
faturamento_anual = faturamento_mensal * 12
unidades_necessarias = num_alunos / alunos_unidade

st.write(f"**Faturamento mensal:** R$ {faturamento_mensal:,.2f}")
st.write(f"**Faturamento anual:** R$ {faturamento_anual:,.2f}")
st.write(f"**Unidades necessárias (atual):** {unidades_necessarias:.1f}")

alunos_meta = meta_anual / (ticket_medio * 12)
unidades_meta = alunos_meta / alunos_unidade

st.write(f"---")
st.write(f"**Alunos necessários para meta:** {alunos_meta:.0f}")
st.write(f"**Unidades necessárias para meta:** {unidades_meta:.1f}")
