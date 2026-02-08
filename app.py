import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Status Marcenaria - Diagnóstico", layout="wide")

# Correção do Erro de Estilização e Cores (Marrom #634D3E e Dourado #B59572)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1, h2, h3 { color: #634D3E !important; }
    .stAlert { background-color: #B59572; color: white; }
    div[data-testid="stMetricValue"] { color: #634D3E; }
    </style>
    """, unsafe_allow_html=True)

# --- CAPA ---
# Ajustado para procurar o arquivo .png
try:
    st.image("Status Apresentação.png", use_container_width=True)
except:
    st.error("Arquivo 'Status Apresentação.png' não encontrado. Verifique o nome no GitHub.")

st.title("DIAGNÓSTICO GERAL INTEGRADO")
st.subheader("Status Marcenaria - Visão Sistêmica")
st.markdown("---")

# --- FATO CENTRAL (Direto do PDF) ---
st.header("1. O Fato Central")
st.error("A empresa não opera por sistema, opera por compensação humana.")
st.write("""
O negócio se mantém funcional porque pessoas experientes antecipam problemas, apagam incêndios e improvisam soluções. 
**Isso mascara a ineficiência estrutural e impede a evolução.**
""")
st.info("💡 'Onde há pessoas boas, o sistema não é forçado a existir.'")

# --- TABELA DE MUDANÇA (AS-IS / TO-BE) ---
st.header("2. O que MUDA na prática (Choque Cultural)")
data_comp = {
    "Aspecto": ["Dono do pedido", "Entrada de pedidos", "PCP", "Produção", "Financeiro", "Logística", "Mudanças"],
    "Hoje (Como é)": ["Inexistente", "Livre", "Lançador", "Executa urgência", "Reage", "Última a saber", "Informais"],
    "Com o Mapa (Desejado)": ["Gestor definido", "Gate técnico", "Controlador", "Executa plano", "Veta tecnicamente", "Co-define prazo", "Registradas"]
}
df_comp = pd.DataFrame(data_comp)
st.table(df_comp)

# --- GATES DE CONTROLE ---
st.header("3. Mapa de Governança: Os 4 Gates Formais")
st.write("O pedido que quebra o gate **NÃO** avança. Se avançar, a governança foi quebrada.")

col1, col2 = st.columns(2)

with col1:
    with st.expander("✅ GATE 1 - Aceite Técnico"):
        st.write("**Responsável:** Dono do Pedido")
        st.write("- Projeto completo e escopo fechado.")
        st.write("- Sem este gate, o pedido não entra no sistema.")

    with st.expander("🏭 GATE 2 - Liberação de Produção"):
        st.write("**Responsável:** PCP")
        st.write("- Sequenciamento definido e capacidade validada.")
        st.write("- A produção não inicia sem esta liberação.")

with col2:
    with st.expander("💰 GATE 3 - Material Garantido"):
        st.write("**Responsável:** Financeiro")
        st.write("- Material comprado e impacto financeiro validado.")
        st.write("- Bloqueio total se o material crítico não estiver disponível.")

    with st.expander("🚛 GATE 4 - Liberação Logística"):
        st.write("**Responsável:** Dono do Pedido")
        st.write("- Produto conferido e rota/frota definidas.")
        st.write("- A entrega só acontece com a validação final.")

# --- REGRA DE OURO ---
st.warning("**REGRA DE OURO:** Toda mudança de projeto exige um 'mini-gate'. Se não há registro, a mudança não existe.")

# --- INDICADORES ---
st.header("4. Indicador de Sucesso")
st.metric(label="% de pedidos que atravessam o fluxo sem quebra de gate", value="Meta Inicial: ≥ 85%")

st.sidebar.markdown("### Governança Status")
st.sidebar.write("A reunião semanal deve focar na quebra dos gates, não na operação.")
