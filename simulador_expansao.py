import streamlit as st

st.title('Simulador de Expansão - FTC')

st.subheader("Parâmetros da Unidade")
custo_implantacao = st.number_input('Custo de implantação (R$)', value=25000)
custo_fixo_mensal = st.number_input('Custo fixo mensal por unidade (R$)', value=10000)
ticket_medio = st.number_input('Ticket médio mensal por aluno (R$)', value=210.0)
custo_variavel_aluno = st.number_input('Custo variável mensal por aluno (R$)', value=30.0)
meta_lucro = st.number_input('Meta de lucro mensal por unidade (R$)', value=0)
num_alunos = st.number_input('Nº de alunos por unidade', value=80)
num_unidades = st.number_input('Nº de unidades', value=1)

# Cálculos por unidade
faturamento = num_alunos * ticket_medio
despesa = custo_fixo_mensal + (num_alunos * custo_variavel_aluno)
lucro = faturamento - despesa

# Break-even: mínimo de alunos p/ empatar
if ticket_medio > custo_variavel_aluno:
    alunos_break_even = custo_fixo_mensal / (ticket_medio - custo_variavel_aluno)
else:
    alunos_break_even = 0

# Payback da unidade
if lucro > 0:
    payback_meses = custo_implantacao / lucro
else:
    payback_meses = 0

st.markdown("### Resultado por Unidade")
st.write(f"Faturamento mensal: R$ {faturamento:,.2f}")
st.write(f"Despesa mensal: R$ {despesa:,.2f}")
st.write(f"Lucro/Prejuízo mensal: R$ {lucro:,.2f}")
st.write(f"Alunos para break-even: {alunos_break_even:.1f}")
st.write(f"Payback (meses): {payback_meses:.1f}")

# Expansão (total)
faturamento_total = faturamento * num_unidades
despesa_total = despesa * num_unidades
lucro_total = lucro * num_unidades
invest_total = custo_implantacao * num_unidades

st.markdown("### Resultado Total (todas unidades)")
st.write(f"Faturamento total: R$ {faturamento_total:,.2f}")
st.write(f"Despesa total: R$ {despesa_total:,.2f}")
st.write(f"Lucro total: R$ {lucro_total:,.2f}")
st.write(f"Investimento total: R$ {invest_total:,.2f}")
