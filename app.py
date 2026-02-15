import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Status Marcenaria - Diagnóstico Completo", layout="wide")

# Estilização com a paleta de cores Status (Marrom #634D3E e Dourado #B59572)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #634D3E !important; }
    .stAlert { background-color: #B59572; color: white; }
    .css-17l6sh2 { color: #634D3E; }
    .st-emotion-cache-1kyx06n { background-color: #634D3E; }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL INTEGRAL COM S1 E S2 ---
st.sidebar.image("Status Apresentação.png", use_container_width=True)
st.sidebar.title("DIAGNÓSTICO E GOVERNANÇA")
secao = st.sidebar.radio(
    "Navegue pelo conteúdo:",
    [
        "S1 - 0. Capa e Introdução",
        "S1 - 1. Fato Central",
        "S1 - 2. Lógica Sistêmica (Causa)",
        "S1 - 3. Manifestação por Área",
        "S1 - 4. Pontos Cegos Estratégicos",
        "S1 - 5. Riscos Reais",
        "S1 - 6. Leitura Executiva",
        "S1 - 7. Direção Lógica",
        "S1 - 8. Mapa de Governança",
        "S1 - 9. Papéis-Chave",
        "S1 - 10. Gates Formais (Bloqueios)",
        "S1 - 11. Regras e Indicadores",
        "S1 - 12. Visão Atual vs Esperada",
        "S1 - 13. RACI e Recomendações",
        "S1 - 14. Checklists Detalhados",
        "S1 - 15. Rotina Semanal de Governança",
        "S2 - 1. Módulo de Medição (Terceirizados)",
        "S2 - 2. Governança Operacional e Resultados",
        "S2 - 3. Diagnóstico Geral - Produção",
        "S2 - 4. Diagnóstico Organizacional - RH",
        "S2 - 5. Atualizações e Próximos Passos"
    ]
)

# --- CONTEÚDO INTEGRAL ---

if secao == "S1 - 0. Capa e Introdução":
    st.image("Status Apresentação.png", use_container_width=True)
    st.title("DIAGNÓSTICO GERAL INTEGRADO")
    st.subheader("Status Marcenaria – Visão Sistêmica")
    st.markdown("---")
    st.info('“Sucesso nada mais é do que algumas disciplinas simples, praticadas todos os dias.”')
    st.write("**Jim Rohn** – empreendedor americano e grande influência na gestão industrial dos EUA.")
    st.write("**Legenda:** Gate = Ponto de controle.")

elif secao == "S1 - 1. Fato Central":
    st.header("1️⃣ Fato Central")
    st.error("A empresa não opera por sistema, opera por compensação humana.")
    st.write("""
    O negócio se mantém funcional porque pessoas são experientes:
    * **Antecipam** problemas,
    * **Apagam** incêndios,
    * **Improvisam** soluções.
    
    Isso mascara a ineficiência estrutural, gera sensação de controle e impede evolução.
    **Onde há pessoas boas, o sistema não é forçado a existir.**
    """)

elif secao == "S1 - 2. Lógica Sistêmica (Causa)":
    st.header("2️⃣ Lógica Sistêmica do Problema (cadeia causal)")
    
    st.subheader("❌ CAUSA PRIMÁRIA: Inexistência de governança do pedido ponta a ponta")
    st.write("""
    O pedido:
    * Entra sem gate técnico,
    * Muda sem controle,
    * É executado sem responsável único,
    * Explode tardiamente em compras, financeiro e logística.
    
    **Não existe a figura do “dono do pedido” com autoridade real.**
    """)
    
    st.subheader("❌ CAUSA SECUNDÁRIA: Produção e PCP sem papel decisório")
    st.write("""
    * PCP lança, mas não controla.
    * Produção executa, mas não programa.
    * Alterações são feitas sem rastreabilidade.
    * Gargalos são conhecidos, mas não têm dono nem KPI (Indicadores).
    
    **Resultado:** o erro só aparece no final, quando já é caro.
    """)
    
    st.subheader("❌ CAUSA TERCIÁRIA: Governança informal se sobrepõe à hierarquia formal")
    st.write("""
    * Financeiro conhece o caixa, mas não tem poder de veto.
    * Compras sofre pressão para “dar um jeito”.
    * Logística recebe datas prontas, sem participar da decisão.
    * Gestores “pulam o processo” quando precisam.
    """)
    st.warning("👉 O sistema real é: **quem grita mais alto, decide.**")

elif secao == "S1 - 3. Manifestação por Área":
    st.header("3️⃣ Como isso se manifesta por área (efeito, não culpa)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🟥 Produção / PCP")
        st.write("* Principal gerador de urgência sistêmica.")
        st.write("* Trabalha sem horizonte mínimo confiável.")
        st.write("* Não fecha o ciclo do pedido.")
        st.write("* Não mede desperdício, retrabalho ou impacto de mudanças.")
        st.write("➡️ **Gera instabilidade para toda a empresa.**")
        
        st.markdown("### 🟦 Compras")
        st.write("* Atua além do papel técnico.")
        st.write("* Apaga incêndios criados upstream (fases anteriores).")
        st.write("* Compra com informação incompleta.")
        st.write("* Vive urgência como rotina.")
        st.write("➡️ **É amortecedor do caos, não causa.**")

    with col2:
        st.markdown("### 🟩 Financeiro")
        st.write("* Conhece o caixa atual.")
        st.write("* Não controla o fluxo futuro.")
        st.write("* Prioriza pagamento por urgência, não por planejamento.")
        st.write("* O “Não” técnico não é respeitado.")
        st.write("➡️ **Funciona como caixa, não como gestor financeiro.**")
        
        st.markdown("### 🟨 Gerência Geral (Wilson)")
        st.write("* Centraliza decisões por ausência de método.")
        st.write("* Distribui obras sem critério formal.")
        st.write("* Acompanha por conversa.")
        st.write("* Resolve exceções diariamente.")
        st.write("➡️ **Virou o sistema informal da empresa.**")

    st.markdown("### 🟪 Logística")
    st.write("* Totalmente reativa.")
    st.write("* Não participa da definição de prazos.")
    st.write("* Sem processos, checklists ou KPIs.")
    st.write("* Frota subutilizada ou sobrecarregada alternadamente.")
    st.write("➡️ **Última a saber, primeira a sofrer.**")

elif secao == "S1 - 4. Pontos Cegos Estratégicos":
    st.header("4️⃣ Pontos Cegos Estratégicos (onde a empresa se engana)")
    
    st.subheader("⚠️ “Planejamento puxa a empresa”")
    st.error("❌ Falso. Quem puxa é a urgência.")
    
    st.subheader("⚠️ “Não temos medo de controle”")
    st.warning("❌ Parcial. O que existe é medo de perder poder informal.")
    
    st.subheader("⚠️ “Reduzir urgência é objetivo”")
    st.write("❌ Urgência não se reduz por meta, se reduz por:")
    st.write("* Gate,")
    st.write("* Dono do pedido,")
    st.write("* Programação,")
    st.write("* Governança de mudança.")

elif secao == "S1 - 5. Riscos Reais":
    st.header("5️⃣ Riscos Reais se nada mudar")
    st.markdown("""
    * Margem corroída por retrabalho invisível.
    * Caixa sempre sob stress.
    * Fornecedores caros viram “salvadores”.
    * Dependência de pessoas-chave (risco operacional).
    * Escala impossível.
    * Qualidade e prazo baseados em heróis, não em processo.
    """)

elif secao == "S1 - 6. Leitura Executiva":
    st.header("6️⃣ Leitura Executiva Correta")
    st.success("O problema da Status não é operacional, é estrutural.")
    st.write("""
    **Sem:**
    * Dono do pedido,
    * PCP com poder,
    * Produção programada,
    * Governança real,
    
    Qual qualquer melhoria em compras, financeiro ou logística será paliativa.
    """)

elif secao == "S1 - 7. Direção Lógica":
    st.header("7️⃣ Direção lógica (não plano ainda)")
    st.subheader("Ordem obrigatória de ataque:")
    st.write("1. **Dono do pedido** (autoridade real)")
    st.write("2. **Gate formal** de entrada e mudança")
    st.write("3. **PCP controlador** (não lançador)")
    st.write("4. **Programação mínima** obrigatória")
    st.write("5. **Governança financeira** com veto técnico")
    st.write("6. **Logística integrada** ao prazo, não executora cega")

elif secao == "S1 - 8. Mapa de Governança":
    st.header("MAPA ÚNICO DE GOVERNANÇA DO PEDIDO")
    st.subheader("Status Marcenaria — Pedido do início ao fim")
    
    st.markdown("### 1️⃣ Princípio inegociável")
    st.error("Todo pedido tem UM dono.")
    st.write("Quem não tem dono, vira problema coletivo — e ninguém resolve.")
    
    st.write("**Esse mapa responde 3 perguntas que hoje não têm resposta clara:**")
    st.write("1. Quem decide?")
    st.write("2. Com base em quê?")
    st.write("3. Em que momento o pedido pode (ou não) seguir?")
    
    st.markdown("### 2️⃣ Visão Geral do Fluxo (macro)")
    st.write("Comercial ➡️ Gate 1 ➡️ PCP/Produção ➡️ Gate 2 ➡️ Compras ➡️ Gate 3 ➡️ Produção/Montagem ➡️ Logística ➡️ Entrega/Fechamento")

elif secao == "S1 - 9. Papéis-Chave":
    st.header("3️⃣ Papéis-Chave (quem manda no quê)")
    
    st.subheader("🔴 DONO DO PEDIDO (Gestor de Produção)")
    st.write("**Autoridade real do pedido do início ao fim.**")
    st.write("Responsável por: Prazo, Material, Mudanças, Entrega.")
    st.info("👉 Se algo falhar, a pergunta é uma só: 'O dono do pedido validou?'")
    
    st.subheader("🟠 PCP (Controlador, não lançador)")
    st.write("* Controla fluxo e protege gargalo.")
    st.write("* Enxerga impacto antes do atraso.")
    st.write("* Pode barrar pedido mal definido.")
    
    st.subheader("🟡 Financeiro (Veto Técnico)")
    st.write("* Valida caixa e impacto. Pode dizer NÃO.")
    st.write("* Prioridade não é urgência, é plano.")
    
    st.subheader("🟢 Compras (Execução Técnica)")
    st.write("* Compra com informação completa.")
    st.write("* Não decide prazo e não apaga incêndio criado por falha de governança.")
    
    st.subheader("🔵 Logística (Planejamento de Entrega)")
    st.write("* Participa da definição de prazo.")
    st.write("* Executa com antecedência mínima.")
    st.write("* Não recebe data “goela abaixo”.")

elif secao == "S1 - 10. Gates Formais (Bloqueios)":
    st.header("4️⃣ Gates Formais (onde o pedido pode morrer)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🚧 GATE 1 — Aceite Técnico")
        st.write("*Antes de virar produção.*")
        st.write("**Checklist:** Projeto completo, Escopo fechado, Prazo preliminar, Dono definido.")
        st.write("**Aprova:** PCP + Gestor do Pedido.")
        st.error("❌ Sem gate = pedido NÃO entra.")
        
        st.markdown("### 🚧 GATE 2 — Liberação de Produção")
        st.write("*Antes de cortar material.*")
        st.write("**Checklist:** Sequenciamento definido, Capacidade validada, Gargalo protegido, Alterações registradas.")
        st.write("**Aprova:** PCP + Dono do Pedido.")

    with col2:
        st.markdown("### 🚧 GATE 3 — Material Garantido")
        st.write("*Antes de iniciar produção.*")
        st.write("**Checklist:** Material comprado, Quantidade correta, Lead time respeitado, Financeiro validou.")
        st.write("**Aprova:** Compras + Financeiro + Dono do Pedido.")
        
        st.markdown("### 🚧 GATE 4 — Liberação Logística")
        st.write("*Antes de prometer entrega.*")
        st.write("**Checklist:** Produto conferido, Checklist de carga, Rota/Frota definidas, Prazo confirmado.")
        st.write("**Aprova:** Logística + Dono do Pedido.")

elif secao == "S1 - 11. Regras e Indicadores":
    st.header("5️⃣ Regra de Ouro (sem exceção)")
    st.error("❗ Mudança de projeto = novo mini-gate")
    st.write("Toda mudança exige: registro escrito, impacto em prazo, impacto em custo e nova validação.")
    st.warning("👉 Mudança sem registro = não existe.")
    
    st.header("7️⃣ Indicador-chave de sucesso")
    st.metric("% de pedidos que atravessam o fluxo sem quebra de gate", "Se sobe: Urgência cai / Retrabalho cai")
    
    st.header("8️⃣ Verdade dura")
    st.write("Se este mapa não for implantado integralmente, ele vira “mais um desenho bonito” e o sistema informal vence de novo.")
    st.success("Governança não se negocia, se impõe.")

elif secao == "S1 - 12. Visão Atual vs Esperada":
    st.header("MAPA DE GOVERNANÇA DO PEDIDO")
    
    st.subheader("🚩 ATUAL (Fluxo Real Observado)")
    st.write("Cliente ➡️ Pedido Incompleto ➡️ Wilson distribui informalmente ➡️ Gestor tenta tocar ➡️ Produção inicia sem material ➡️ Compras corre atrás ➡️ Financeiro reage ➡️ Logística recebe prazo pronto ➡️ Entrega sob pressão.")
    
    st.subheader("✅ ESPERADO (Fluxo Único Permitido)")
    st.write("Entrada ➡️ **GATE 1** ➡️ Planejamento ➡️ **GATE 2** ➡️ Compras ➡️ **GATE 3** ➡️ Produção (com Mini-Gate se houver mudança) ➡️ **GATE 4** ➡️ Entrega.")
    
    st.subheader("O que muda estruturalmente")
    data_mudanca = {
        "Aspecto": ["Dono do pedido", "Entrada de pedidos", "PCP", "Produção", "Compras", "Financeiro", "Logística", "Mudanças", "Controle"],
        "AS-IS (Como é)": ["Inexistente", "Livre", "Lançador", "Executa urgência", "Apaga incêndio", "Reage", "Última a saber", "Informais", "Conversa"],
        "TO-BE (Desejado)": ["Gestor definido", "Gate técnico", "Controlador", "Executa plano", "Executa planejamento", "Veta tecnicamente", "Co-define prazo", "Registradas", "Sistema"]
    }
    st.table(pd.DataFrame(data_mudanca))

elif secao == "S1 - 13. RACI e Recomendações":
    st.header("RACI (ERCI) FORMAL – GOVERNANÇA DO PEDIDO")
    
    st.markdown("""
    **Legenda oficial**
    * **E (Executor)** → Executa a atividade
    * **R (Responsável)** → Dono final / responde pelo resultado
    * **C (Consultado)** → Consultado antes da decisão
    * **I (Informado)** → Informado após a decisão
    """)
    st.info("Regra inegociável: cada atividade tem UM único R.")

    st.markdown("---")

    st.subheader("1️⃣ Papéis (mantidos)")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write("* **COM** – Comercial")
        st.write("* **DP** – Dono do Pedido (Gestor da Obra/Produção)")
        st.write("* **PCP** – Planejamento e Controle da Produção")
        st.write("* **PROD** – Produção / Fábrica")
    with col_p2:
        st.write("* **COMP** – Compras")
        st.write("* **FIN** – Financeiro")
        st.write("* **LOG** – Logística")
        st.write("* **GG** – Gerência Geral")

    st.markdown("---")

    # Gate 1 - Baseado na Imagem Entrada do Pedido
    st.subheader("2️⃣ Entrada do Pedido - GATE 1 (Aceite Técnico)")
    df_g1 = pd.DataFrame({
        "Atividade": ["Registrar pedido no sistema", "Validar escopo técnico", "Validar viabilidade inicial de prazo", "Autorizar entrada do pedido"],
        "COM": ["E", "C", "I", "I"],
        "DP": ["I", "R", "R", "R"],
        "PCP": ["I", "E", "E", "E"],
        "FIN": ["I", "I", "C", "I"],
        "GG": ["I", "I", "I", "I"]
    })
    st.table(df_g1)
    st.error("🔒 Sem R (DP) definido → pedido NÃO entra")

    # Gate 2 - Baseado na Imagem Planejamento e Sequenciamento
    st.subheader("3️⃣ Planejamento e Sequenciamento - GATE 2 (Liberação de Produção)")
    df_g2 = pd.DataFrame({
        "Atividade": ["Sequenciar pedidos", "Validar capacidade produtiva", "Proteger gargalo", "Liberar produção"],
        "DP": ["C", "C", "I", "I"],
        "PCP": ["R", "R", "R", "R"],
        "PROD": ["I", "I", "E", "C"],
        "GG": ["I", "I", "I", "I"]
    })
    st.table(df_g2)
    st.info("👉 PCP responde pelo plano. Produção executa.")

    # Gate 3 - Baseado na Imagem Compras e Materiais
    st.subheader("4️⃣ Compras e Materiais - GATE 3 (Material Garantido)")
    df_g3 = pd.DataFrame({
        "Atividade": ["Definir lista de materiais", "Planejar compras", "Validar impacto no caixa", "Autorizar compra"],
        "DP": ["R", "I", "I", "I"],
        "PCP": ["C", "C", "I", "I"],
        "COMP": ["E", "R", "C", "E"],
        "FIN": ["I", "I", "R", "R"]
    })
    st.table(df_g3)
    st.info("🔴 Financeiro é R na autorização → veto técnico real")

    # Produção e Mudanças - Baseado na Imagem Produção e Mudanças
    st.subheader("5️⃣ Produção e Mudanças de Escopo")
    df_prod = pd.DataFrame({
        "Atividade": ["Executar produção", "Controlar avanço do pedido", "Aprovar mudança de escopo", "Replanejar após mudança"],
        "DP": ["I", "C", "R", "C"],
        "PCP": ["I", "R", "C", "R"],
        "PROD": ["R", "I", "I", "I"]
    })
    st.table(df_prod)
    st.warning("⚠️ Mudança sem R (DP) = inválida")

    # Gate 4 - Baseado na Imagem Logística e Entrega
    st.subheader("6️⃣ Logística e Entrega - GATE 4 (Liberação de Entrega)")
    df_g4 = pd.DataFrame({
        "Atividade": ["Planejar entrega", "Definir frota e rota", "Validar prazo final", "Liberar entrega"],
        "DP": ["C", "I", "R", "R"],
        "LOG": ["R", "R", "C", "E"],
        "FIN": ["I", "I", "I", "I"]
    })
    st.table(df_g4)
    st.info("👉 Logística planeja, DP responde pelo prazo prometido")

    # Fechamento - Baseado na Imagem Fechamento do Pedido
    st.subheader("7️⃣ Fechamento do Pedido")
    df_fecha = pd.DataFrame({
        "Atividade": ["Confirmar entrega ao cliente", "Encerrar pedido no sistema", "Analisar impacto financeiro final"],
        "DP": ["R", "I", "I"],
        "PCP": ["I", "R", "I"],
        "FIN": ["I", "I", "R"]
    })
    st.table(df_fecha)

    # Papel da GG - Baseado na Imagem Papel da Gerência Geral
    st.subheader("8️⃣ Papel da Gerência Geral (GG) — blindagem do sistema")
    st.markdown("""
    | Atividade | GG |
    | :--- | :---: |
    | Decidir operação diária | ❌ |
    | Quebrar gate | ❌ |
    | Resolver exceções recorrentes | ❌ |
    | Garantir cumprimento do RACI | ✅ |
    | Escalonamento crítico | ⚠️ Somente se formal |
    """)
    st.info("👉 GG é guardião da governança, não executor informal")

    st.markdown("---")

    st.subheader("9️⃣ Onde normalmente tentam burlar (alerta)")
    st.markdown("""
    * “Só dessa vez libera”
    * “Depois a gente formaliza”
    * “É urgente”
    * “Sempre foi assim”
    """)
    st.error("👉 Qualquer exceção mata o ERCI.")

    st.markdown("---")

    st.subheader("1️⃣0️⃣ Recomendações práticas")
    st.markdown("""
    1. Esse ERCI deve virar documento oficial assinado
    2. Gate sem R definido = pedido devolvido
    3. Primeiro mês vai gerar atrito → isso é sinal de sucesso
    4. Quem reclamar está perdendo poder informal
    """)
elif secao == "S1 - 14. Checklists Detalhados":
    st.header("CHECKLISTS OPERACIONAIS POR GATE")
    st.markdown("---")

    # GATE 1
    with st.expander("📝 GATE 1 — ACEITE TÉCNICO DO PEDIDO"):
        st.write("**Objetivo:** impedir entrada de pedido mal definido")
        st.write("**Momento:** antes de qualquer planejamento ou promessa interna")
        st.write("**Responsável (R):** Dono do Pedido (DP) | **Executor (E):** PCP")
        
        st.markdown("### Checklist Obrigatório")
        st.markdown("#### 🔹 Informações Comerciais")
        st.checkbox("Pedido registrado no sistema", key="g1_c1")
        st.checkbox("Cliente identificado", key="g1_c2")
        st.checkbox("Tipo de obra definido (residencial / corporativa / construtora)", key="g1_c3")
        st.checkbox("Responsável do cliente identificado", key="g1_c4")
        
        st.markdown("#### 🔹 Escopo Técnico")
        st.checkbox("Projeto mínimo recebido (plantas / medidas críticas)", key="g1_e1")
        st.checkbox("Ambientes definidos", key="g1_e2")
        st.checkbox("Materiais principais definidos (MDF, pintura, especiais)", key="g1_e3")
        st.checkbox("Itens fora do padrão identificados", key="g1_e4")
        
        st.markdown("#### 🔹 Prazo (prévia)")
        st.checkbox("Prazo solicitado pelo comercial registrado", key="g1_p1")
        st.checkbox("Prazo avaliado tecnicamente", key="g1_p2")
        st.checkbox("Risco de prazo identificado (se houver)", key="g1_p3")
        
        st.markdown("#### 🔹 Governança")
        st.checkbox("Dono do Pedido definido", key="g1_g1")
        st.checkbox("PCP validou viabilidade inicial", key="g1_g2")
        st.checkbox("Pedido aprovado formalmente", key="g1_g3")
        
        st.error("❌ **Critérios de BLOQUEIO:** Projeto incompleto, Dono do pedido indefinido, Prazo inviável sem ajuste. ➡️ **Pedido BLOQUEADO até correção**")

    # GATE 2
    with st.expander("📝 GATE 2 — LIBERAÇÃO DE PRODUÇÃO"):
        st.write("**Objetivo:** garantir que a produção execute plano, não urgência")
        st.write("**Momento:** antes de cortar material")
        st.write("**Responsável (R):** PCP | **Executor (E):** Produção")
        
        st.markdown("### Checklist Obrigatório")
        st.markdown("#### 🔹 Planejamento")
        st.checkbox("Pedido sequenciado na programação", key="g2_pl1")
        st.checkbox("Capacidade validada", key="g2_pl2")
        st.checkbox("Gargalo identificado", key="g2_pl3")
        st.checkbox("Gargalo protegido no plano", key="g2_pl4")
        
        st.markdown("#### 🔹 Projeto")
        st.checkbox("Projeto técnico liberado", key="g2_pr1")
        st.checkbox("Medidas conferidas", key="g2_pr2")
        st.checkbox("Versão do projeto registrada", key="g2_pr3")
        
        st.markdown("#### 🔹 Comunicação")
        st.checkbox("Produção ciente do plano", key="g2_co1")
        st.checkbox("Prazo interno registrado", key="g2_co2")
        st.checkbox("Alterações registradas (se houver)", key="g2_co3")
        
        st.error("❌ **Critérios de BLOQUEIO:** Pedido fora da sequência, Gargalo saturado sem ajuste, Projeto sem liberação formal. ➡️ **Produção NÃO inicia**")

    # GATE 3
    with st.expander("📝 GATE 3 — MATERIAL GARANTIDO"):
        st.write("**Objetivo:** eliminar produção sem material")
        st.write("**Momento:** antes do início físico da produção")
        st.write("**Responsável (R):** Financeiro | **Executor (E):** Compras")
        
        st.markdown("### Checklist Obrigatório")
        st.markdown("#### 🔹 Materiais")
        st.checkbox("Lista de materiais validada", key="g3_ma1")
        st.checkbox("Quantidades conferidas", key="g3_ma2")
        st.checkbox("Materiais especiais identificados", key="g3_ma3")
        
        st.markdown("#### 🔹 Compras")
        st.checkbox("Fornecedores definidos", key="g3_com1")
        st.checkbox("Lead times confirmados", key="g3_com2")
        st.checkbox("Datas de entrega registradas", key="g3_com3")
        
        st.markdown("#### 🔹 Financeiro")
        st.checkbox("Impacto no caixa validado", key="g3_fin1")
        st.checkbox("Compra autorizada formalmente", key="g3_fin2")
        st.checkbox("Forma de pagamento definida", key="g3_fin3")
        
        st.error("❌ **Critérios de BLOQUEIO:** Material crítico não comprado, Impacto financeiro não aprovado, Lead time incompatível. ➡️ **Produção BLOQUEADA**")

    # GATE 4
    with st.expander("📝 GATE 4 — LIBERAÇÃO DE ENTREGA"):
        st.write("**Objetivo:** garantir entrega sem retrabalho e improviso")
        st.write("**Momento:** antes de prometer data ao cliente")
        st.write("**Responsável (R):** Dono do Pedido | **Executor (E):** Logística")
        
        st.markdown("### Checklist Obrigatório")
        st.markdown("#### 🔹 Produto")
        st.checkbox("Produção concluída", key="g4_pro1")
        st.checkbox("Qualidade conferida", key="g4_pro2")
        st.checkbox("Itens separados por pedido", key="g4_pro3")
        
        st.markdown("#### 🔹 Logística")
        st.checkbox("Checklist de carga preenchido", key="g4_log1")
        st.checkbox("Frota definida", key="g4_log2")
        st.checkbox("Rota planejada", key="g4_log3")
        
        st.markdown("#### 🔹 Prazo")
        st.checkbox("Data validada com logística", key="g4_prz1")
        st.checkbox("Cliente informado", key="g4_prz2")
        st.checkbox("Equipe de montagem alinhada", key="g4_prz3")
        
        st.error("❌ **Critérios de BLOQUEIO:** Produto incompleto, Falta de frota adequada, Prazo não validado. ➡️ **Entrega NÃO autorizada**")

    st.markdown("---")
    st.info("**REGRA GERAL (vale para todos os Gates):** Gate sem checklist preenchido = Gate inexistente. Pedido que pula Gate = quebra de governança.")
    
    st.subheader("Recomendações práticas (experiência de campo)")
    st.write("1. Cada checklist vira formulário simples (Google / ERP).")
    st.write("2. Checklists assinados (nome + data).")
    st.write("3. Auditoria semanal: pedidos que passaram sem checklist.")
    st.write("4. Primeiras 3 semanas terão atrito — isso é esperado.")

elif secao == "S1 - 15. Rotina Semanal de Governança":
    st.header("ROTINA SEMANAL DE GOVERNANÇA")
    st.subheader("1️⃣ Princípio da rotina")
    st.write("Essa reunião não é operacional. Ela não resolve incêndio. Ela existe para impedir que o incêndio exista na semana seguinte.")
    
    st.subheader("2️⃣ Frequência e Participantes")
    st.write("* **Frequência:** Semanal, 45 minutos (cravado).")
    st.write("* **Participantes:** Donos de Pedido ativos, PCP, Financeiro, Compras, Logística, Wilson (GG).")
    
    st.subheader("3️⃣ Agenda Fixa")
    st.write("1. **Abertura (5 min):** 'Vamos avaliar fluxo, não esforço individual'.")
    st.write("2. **Indicadores (15 min):** Somente os 5 indicadores fixos.")
    st.write("3. **Quebra de Gate (15 min):** Qual pedido furou? Qual gate? Quem era o R?")
    st.write("4. **Ações Estruturais (10 min):** Ações que evitem repetição.")
    
    st.subheader("4️⃣ Indicadores Semanais (Os únicos permitidos)")
    st.write("1. % de pedidos que passaram por TODOS os Gates (Meta: ≥ 85%).")
    st.write("2. Quantidade de pedidos que quebraram Gate (Meta: cair sempre).")
    st.write("3. Urgências geradas por falha de planejamento.")
    st.write("4. Pedidos com mudança sem mini-gate (Meta: ZERO).")
    st.write("5. Lead time médio real vs planejado.")
    
   st.error("Governança vive de repetição, não de discurso.")

# --- INÍCIO DA SEMANA 02 (S2) - CONTEÚDO INTEGRAL SEM RESUMOS ---

elif secao == "S2 - 1. Módulo de Medição (Terceirizados)":
    st.header("Módulo de Medição – Terceirizados")
    st.info("Desenvolvido módulo específico para controle de terceiros com:")
    st.markdown("""
    * ✔ Cálculo automático por produção
    * ✔ Deduplicação de lançamentos
    * ✔ Retenção automática de 15%
    * ✔ Exportação para Excel
    * ✔ Integração com financeiro
    """)
    st.success("**Objetivo:** Eliminar pagamento duplicado e falta de controle de medição.")

elif secao == "S2 - 2. Governança Operacional e Resultados":
    st.header("GOVERNANÇA OPERACIONAL")
    st.write("Foi estruturada rotina semanal com:")
    st.markdown("""
    * Indicador de quebra de Gate
    * Lead time planejado vs realizado
    * Análise de urgências geradas por falha de processo
    * Registro formal de decisões
    """)
    st.warning("**Regra:** Sem registro, não existe decisão.")

    st.header("RESULTADOS ESPERADOS (PROJETADOS)")
    st.markdown("""
    * Redução de retrabalho
    * Aumento da previsibilidade
    * Melhoria no controle de margem
    * Redução de conflitos internos
    * Maior clareza hierárquica
    * Base para crescimento escalável
    """)

    st.header("PRÓXIMOS PASSOS (90 DIAS)")
    st.markdown("""
    * Consolidação do uso obrigatório do sistema
    * Treinamento formal por área
    * Auditoria interna mensal de Gates
    * Implantação de indicadores financeiros vinculados aos CTRs
    * Evolução para dashboard executivo
    """)

    st.header("CONCLUSÃO ESTRATÉGICA")
    st.write("A Status Marcenaria deixou de operar por improviso e passou a operar por estrutura.")
    st.write("A governança agora não depende de memória, pressão ou boa vontade. Depende de sistema.")
    st.info("""
    **O modelo implantado cria base para:**
    * Escala
    * Profissionalização
    * Proteção de margem
    * Governança de longo prazo
    """)

elif secao == "S2 - 3. Diagnóstico Geral - Produção":
    st.header("DIAGNÓSTICO GERAL – PRODUÇÃO STATUS MARCENARIA")
    st.subheader("1️⃣ Conclusão Executiva")
    st.error("O problema não é técnico individual. É sistêmico.")
    st.write("""
    A produção hoje opera em: Modelo reativo, Prazo comercial dominante, Comunicação fragmentada, 
    Ausência de gate técnico estruturado, Ausência de medição de desperdício, Autoridade informal e instável, 
    Cultura predominantemente crítica e centralizadora.
    """)
    st.write("**O sistema funciona por esforço individual, não por método.**")

    st.subheader("2️⃣ Padrões Repetidos em Todos os Gestores")
    
    st.markdown("### A. Prazo nasce comercial")
    st.write("Todos confirmam: Prazo imposto pelo cliente/construtora, Validação concentrada na diretoria, Revisão técnica tardia, Comunicação de atraso ocorre quando já está crítico.")
    st.info("Diagnóstico: Prazo técnico não é premissa do processo.")

    st.markdown("### B. Ausência de Gate Técnico Real")
    st.write("Recorrência: Compra antes de aprovação, Produção sem medida in loco validada, Mudança de projeto após início, Aprovação de SD como gargalo tardio, Falta de checklist consolidado.")
    st.info("Diagnóstico: O pedido entra na fábrica sem estar maduro.")

    st.markdown("### C. Comunicação Pulverizada")
    st.write("Constatação geral: WhatsApp + e-mail + comunicação verbal, Engenharia falando direto com gestor, Gerência executando antes de formalizar, Problemas indo direto à diretoria, Gestor não é o ponto único institucionalizado.")
    st.info("Diagnóstico: Não existe “dono formal do fluxo”.")

    st.markdown("### D. Qualidade em Declínio")
    st.write("Relatos críticos: “Qualidade de mal a pior”, Cliente acostumando com erro, Falta de controle antes da saída, Terceiros entregando fora do padrão, MDF usado errado, Mistura de materiais semelhantes.")
    st.info("Diagnóstico: Controle de qualidade é corretivo, não preventivo.")

    st.markdown("### E. Retrabalho Não Mensurado")
    st.write("Todos afirmam: Não há indicador, Não há métrica, Só percepção, Custo é invisível.")
    st.info("Diagnóstico: A empresa opera no escuro.")

    st.markdown("### F. PCP Frágil")
    st.write("PCP hoje: Mensageiro, Intermediário, Não trava fluxo, Não gera alerta formal, Não mede gargalo.")
    st.info("Diagnóstico: PCP não é sistema de controle. É amortecedor de ruído.")

    st.markdown("### G. Terceirização Desgovernada")
    st.write("Problemas recorrentes: Preço baixo gera qualidade baixa, Fornecedor pega outros serviços no meio, Falta de tabela clara, Falta de padrão de cobrança, Falta de inspeção antes de envio, Falta de contrato técnico robusto.")
    st.info("Diagnóstico: Economia aparente gera prejuízo oculto.")

    st.markdown("### H. Autoridade Instável dos Gestores")
    st.write("Padrão comum: Responsabilidade alta, Autonomia baixa, Interferência direta da diretoria, Decisão empírica (“feeling”), Hierarquia limita ação, Gestor é cobrado por informação que não recebeu.")
    st.info("Diagnóstico: A estrutura não sustenta o papel do gestor.")

    st.markdown("### I. Cultura Organizacional")
    st.write("Elementos recorrentes: Comunicação crítica em grupo, Exposição pública, Jovens saindo, Ambiente de “pisar em ovos”, Centralização excessiva, Profissionalismo exigido sem método consolidado.")
    st.info("Diagnóstico: Cultura atual amplifica falhas de processo.")

    st.subheader("3️⃣ Mapa de Causa-Raiz")
    st.write("Comercial frágil ➡️ Orçamento desalinhado ➡️ Projeto técnico imaturo ➡️ Produção inicia sem gate ➡️ Mudanças no meio do caminho ➡️ Retrabalho ➡️ Pressão de prazo ➡️ Queda de qualidade ➡️ Cliente tolera erro ➡️ Padrão normalizado para baixo.")

    st.subheader("7️⃣ Diagnóstico Final (Sem Suavizar)")
    st.write("Hoje a produção: Funciona por esforço (não por sistema), funciona por experiência (não por governança), funciona por correção (não por prevenção).")
    st.warning("O modelo atual depende de: Wilson, Feeling, Improvisação, Sobre-esforço e Heróis operacionais. Isso não escala.")

    st.subheader("8️⃣ Direção Estratégica Obrigatória")
    st.write("""
    * Gate técnico inegociável antes da produção
    * Prazo técnico obrigatório antes do fechamento comercial
    * Gestor como ponto único formal do pedido
    * PCP com poder de travamento
    * Sistema de medição de retrabalho
    * Redesenho da governança de terceiros
    * Checklist técnico obrigatório antes da saída
    * Reformulação cultural da comunicação interna
    """)

elif secao == "S2 - 4. Diagnóstico Organizacional - RH":
    st.header("DIAGNÓSTICO ORGANIZACIONAL – RECURSOS HUMANOS (RH)")
    st.subheader("1. Diagnóstico Geral (Resumo Executivo)")
    st.error("O RH não opera como área estruturada de gestão de pessoas. Funciona como setor operacional multifuncional e setor tampão.")
    
    st.subheader("2. Papel Real (Executado)")
    st.write("""
    O RH acumula funções que extrapolam completamente sua responsabilidade:
    * Gestão integral de viagens (passagens, alimentação, hospedagem, controle diário) - Consome 95% do tempo.
    * Manutenção da fábrica.
    * Gestão de conflitos operacionais.
    * Execução de demissões por incapacidade dos líderes.
    * Tratativa de alvarás e licenças (bombeiros, vigilância sanitária e ambiental).
    """)

    st.subheader("4. Desvios de Função Estruturais")
    st.markdown("""
    | Atividade | Impacto |
    | :--- | :--- |
    | Gestão de viagens | Consome aproximadamente 95% do tempo do RH |
    | Manutenção da fábrica | Desvio técnico e operacional |
    | Gestão de conflitos como decisor | Inversão de papel |
    | Demissões conduzidas pelo RH | Risco jurídico elevado |
    """)

    st.subheader("10. Direcionamentos Estruturais")
    st.success("""
    * Retirar imediatamente do RH: Gestão de viagens, Manutenção da fábrica e Decisões de demissão.
    * Definir donos claros: Viagens (Logística), Manutenção (Responsável técnico), Conflitos (Líder direto).
    * Tratar riscos urgentes: Regularizar horas extras e implantar sistema de ponto confiável.
    """)

elif secao == "S2 - 5. Atualizações e Próximos Passos":
    st.header("ATUALIZAÇÕES E PRÓXIMOS PASSOS")
    st.info("Nesta semana: Criamos o sistema de controle de gates com método ERCI e foi encaminhado para o PCP validar. Produção prevista para início de março.")
    st.write("* Conversado com a gestora da Ademicon para estratégias de investimento e aquisição de máquina.")
    st.write("* Dados enviados para empresa recomendada pelo Eduardo dia 16 para proposta de máquina.")
    st.write("* Apresentado para Eduarda estratégia de acúmulo de milhas usando inteligência.")

# --- RODAPÉ LATERAL (FINAL DE TUDO) ---
st.sidebar.markdown("---")
st.sidebar.caption("Status Marcenaria - Visão Sistêmica 2026")
