import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Diagnóstico Status Marcenaria", layout="wide")

# Estilização com as cores da marca (Marrom e Dourado)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1, h2 { color: #634D3E; }
    .stAlert { background-color: #B59572; color: white; }
    </style>
    """, unsafe_allow_config=True)

# --- CAPA ---
st.title("DIAGNÓSTICO GERAL INTEGRADO")
st.subheader("Status Marcenaria - Visão Sistêmica")
st.info('"Sucesso nada mais é do que algumas disciplinas simples, praticadas todos os dias." - Jim Rohn')

# --- FATO CENTRAL ---
st.header("1. O Fato Central")
st.error("A empresa não opera por sistema, opera por compensação humana.")
st.write("""
O negócio se mantém funcional porque pessoas experientes antecipam problemas, apagam incêndios e improvisam soluções. 
**Isso mascara a ineficiência estrutural e impede a evolução.**
""")

# --- COMPARAÇÃO AS-IS / TO-BE ---
st.header("2. O que MUDA na prática (Choque Cultural)")
data_comp = {
    "Aspecto": ["Dono do pedido", "Entrada de pedidos", "PCP", "Produção", "Financeiro", "Logística", "Mudanças", "Controle"],
    "Hoje (Como é)": ["Inexistente", "Livre", "Lançador", "Executa urgência", "Reage", "Última a saber", "Informais", "Conversa"],
    "Com o Mapa (Desejado)": ["Gestor definido", "Gate técnico", "Controlador", "Executa plano", "Veta tecnicamente", "Co-define prazo", "Registradas", "Sistema"]
}
df_comp = pd.DataFrame(data_comp)
st.table(df_comp)

# --- GATES DE CONTROLE ---
st.header("3. Os 4 Gates Formais (Pontos de Bloqueio)")
col1, col2 = st.columns(2)

with col1:
    with st.expander("GATE 1 - Aceite Técnico"):
        st.write("**Responsável:** Dono do Pedido (DP)")
        st.write("- Projeto completo (medidas críticas)")
        st.write("- Escopo fechado")
        st.write("- Sem gate = pedido NÃO entra")

    with st.expander("GATE 2 - Liberação de Produção"):
        st.write("**Responsável:** PCP")
        st.write("- Sequenciamento definido")
        st.write("- Capacidade validada")
        st.write("- Produção NÃO inicia sem liberação")

with col2:
    with st.expander("GATE 3 - Material Garantido"):
        st.write("**Responsável:** Financeiro")
        st.write("- Material comprado e quantidade correta")
        st.write("- Financeiro validou impacto no caixa")
        st.write("- Produção BLOQUEADA sem material")

    with st.expander("GATE 4 - Liberação Logística"):
        st.write("**Responsável:** Dono do Pedido")
        st.write("- Produto final conferido")
        st.write("- Rota e frota definidas")
        st.write("- Entrega NÃO autorizada sem validação")

# --- REGRA DE OURO ---
st.warning("**REGRA DE OURO:** Mudança de projeto = novo mini-gate. Mudança sem registro não existe.")

# --- INDICADOR CHAVE ---
st.header("4. Indicador de Sucesso")
st.metric(label="% de pedidos que atravessam o fluxo sem quebra de gate", value="Meta: >85%", delta="Urgência Cai / Caixa Estabiliza")

st.sidebar.markdown("### Governança não se negocia, se impõe.")
