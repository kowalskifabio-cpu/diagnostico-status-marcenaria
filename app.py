import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Status Marcenaria - Diagnóstico", layout="wide")

# Estilização Profissional
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1, h2, h3 { color: #634D3E !important; }
    .stAlert { background-color: #B59572; color: white; }
    .sidebar .sidebar-content { background-image: linear-gradient(#634D3E, #332F2E); color: white; }
    .css-17l6sh2 { color: #634D3E; }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL (SEQUÊNCIA DO DOCUMENTO) ---
st.sidebar.image("Status Apresentação.png", use_container_width=True)
st.sidebar.title("Navegação")
secao = st.sidebar.radio(
    "Ir para:",
    [
        "Capa",
        "1. Fato Central",
        "2. Lógica Sistêmica",
        "3. Manifestação por Área",
        "4. Pontos Cegos",
        "5. Riscos Reais",
        "6. Leitura Executiva",
        "7. Direção Lógica",
        "8. Mapa de Governança",
        "9. Gates de Controle",
        "10. O que Muda (AS-IS/TO-BE)",
        "11. Checklists dos Gates",
        "12. Rotina Semanal"
    ]
)

# --- CONTEÚDO ---

if secao == "Capa":
    st.image("Status Apresentação.png", use_container_width=True)
    st.title("DIAGNÓSTICO GERAL INTEGRADO")
    st.header("Status Marcenaria – Visão Sistêmica")
    st.info('“Sucesso nada mais é do que algumas disciplinas simples, praticadas todos os dias.” — Jim Rohn')
    st.write("**Legenda:** Gate = Ponto de controle.")

elif secao == "1. Fato Central":
    st.header("1️⃣ Fato Central")
    st.error("A empresa não opera por sistema, opera por compensação humana.")
    st.write("""
    O negócio se mantém funcional porque pessoas experientes:
    * **Antecipam** problemas
    * **Apagam** incêndios
    * **Improvisam** soluções
    
    Isso mascara a ineficiência estrutural, gera sensação de controle e impede evolução.
    **Onde há pessoas boas, o sistema não é forçado a existir.**
    """)

elif secao == "2. Lógica Sistêmica":
    st.header("2️⃣ Lógica Sistêmica do Problema (Cadeia Causal)")
    
    st.subheader("❌ CAUSA PRIMÁRIA: Inexistência de governança")
    st.write("O pedido entra sem gate técnico, muda sem controle e explode no final.")
    
    st.subheader("❌ CAUSA SECUNDÁRIA: Produção e PCP sem papel decisório")
    st.write("O PCP lança mas não controla. O erro só aparece no final, quando já é caro.")
    
    st.subheader("❌ CAUSA TERCIÁRIA: Governança informal")
    st.warning("O sistema real é: quem grita mais alto, decide.")

elif secao == "3. Manifestação por Área":
    st.header("3️⃣ Manifestação por Área (Efeito, não culpa)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🟥 Produção / PCP")
        st.write("Principal gerador de urgência. Trabalha sem horizonte mínimo.")
        st.markdown("### 🟦 Compras")
        st.write("Amortecedor do caos. Vive a urgência como rotina.")
    with col2:
        st.markdown("### 🟩 Financeiro")
        st.write("Funciona como caixa, não como gestor. 'Não' técnico não é respeitado.")
        st.markdown("### 🟨 Gerência Geral (Wilson)")
        st.write("Centraliza decisões por ausência de método. Virou o sistema informal.")

elif secao == "4. Pontos Cegos":
    st.header("4️⃣ Pontos Cegos Estratégicos")
    st.write("⚠️ **Falso:** 'Planejamento puxa a empresa'. **Real:** Quem puxa é a urgência.")
    st.write("⚠️ **Falso:** 'Reduzir urgência é objetivo'. **Real:** Urgência se reduz com GATES e GOVERNANÇA.")

elif secao == "5. Riscos Reais":
    st.header("5️⃣ Riscos Reais se nada mudar")
    st.markdown("""
    * Margem corroída por retrabalho invisível
    * Caixa sempre sob stress
    * Dependência de pessoas-chave (risco operacional)
    * Escala impossível
    * Qualidade e prazo baseados em heróis, não em processo
    """)

elif secao == "6. Leitura Executiva":
    st.header("6️⃣ Leitura Executiva Correta")
    st.success("O problema da Status não é operacional, é estrutural.")
    st.write("Qualquer melhoria isolada em compras ou financeiro será paliativa sem um PCP com poder e produção programada.")

elif secao == "7. Direção Lógica":
    st.header("7️⃣ Direção Lógica de Ataque")
    st.write("1. **Dono do pedido** (Autoridade real)")
    st.write("2. **Gate formal** de entrada e mudança")
    st.write("3. **PCP controlador** (Não lançador)")
    st.write("4. **Governança financeira** com veto técnico")

elif secao == "8. Mapa de Governança":
    st.header("8️⃣ Mapa Único de Governança")
    st.subheader("Princípio Inegociável: Todo pedido tem UM dono.")
    st.write("**Fluxo:** Comercial ➡️ Gate 1 ➡️ PCP ➡️ Gate 2 ➡️ Compras ➡️ Gate 3 ➡️ Produção ➡️ Gate 4 ➡️ Logística")
    
    st.info("O Dono do Pedido (Gestor de Produção) responde por: Prazo, Material, Mudanças e Entrega.")

elif secao == "9. Gates de Controle":
    st.header("9️⃣ Os 4 Gates Formais (Onde o pedido pode morrer)")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🚧 GATE 1 — Aceite Técnico")
        st.write("Antes de virar produção. Requer projeto completo e dono definido.")
        st.markdown("#### 🚧 GATE 2 — Liberação de Produção")
        st.write("Antes de cortar material. Requer sequenciamento e capacidade validada.")
    with c2:
        st.markdown("#### 🚧 GATE 3 — Material Garantido")
        st.write("Antes de iniciar produção. Requer material em mãos e aval do financeiro.")
        st.markdown("#### 🚧 GATE 4 — Liberação Logística")
        st.write("Antes de prometer data. Requer produto conferido e rota definida.")

elif secao == "10. O que Muda (AS-IS/TO-BE)":
    st.header("1️⃣0️⃣ O que MUDA na prática")
    data = {
        "Aspecto": ["Dono do pedido", "Entrada", "PCP", "Produção", "Financeiro", "Logística", "Wilson"],
        "Hoje (AS-IS)": ["Inexistente", "Livre", "Lançador", "Urgência", "Reage", "Apaga Incêndio", "Resolve Tudo"],
        "Esperado (TO-BE)": ["Gestor Definido", "Gate Técnico", "Controlador", "Plano", "Veta tecnicamente", "Planeja", "Sistema resolve"]
    }
    st.table(pd.DataFrame(data))
    st.warning("REGRA DURA: Pedido que quebra gate NÃO avança. Se avançar, a governança morreu.")

elif secao == "11. Checklists dos Gates":
    st.header("1️⃣1️⃣ Checklists Operacionais")
    aba1, aba2, aba3, aba4 = st.tabs(["Gate 1", "Gate 2", "Gate 3", "Gate 4"])
    with aba1:
        st.write("**Bloqueio se:** Projeto incompleto ou Dono indefinido.")
        st.checkbox("Projeto mínimo recebido?")
        st.checkbox("Dono do pedido definido?")
    with aba2:
        st.write("**Bloqueio se:** Pedido fora da sequência ou gargalo saturado.")
        st.checkbox("Capacidade validada?")
    with aba3:
        st.write("**Bloqueio se:** Material crítico não comprado.")
        st.checkbox("Financeiro autorizou a compra?")
    with aba4:
        st.write("**Bloqueio se:** Produto incompleto ou frota sem rota.")
        st.checkbox("Qualidade conferida?")

elif secao == "12. Rotina Semanal":
    st.header("1️⃣2️⃣ Rotina Semanal de Governança")
    st.write("**Duração:** 45 min (Cravados)")
    st.write("**Foco:** Avaliar quebras de Gate, não resolver problemas do dia.")
    st.markdown("### Indicadores Semanais")
    col_a, col_b = st.columns(2)
    col_a.metric("% Pedidos sem quebra de Gate", "Meta > 85%")
    col_b.metric("Mudanças sem mini-gate", "Meta ZERO")
    st.error("Ata de 1 página obrigatória: Sem ata, a reunião não existiu.")

st.sidebar.markdown("---")
st.sidebar.write("Governança não se negocia, se impõe.")
