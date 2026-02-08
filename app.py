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

# --- MENU LATERAL INTEGRAL ---
st.sidebar.image("Status Apresentação.png", use_container_width=True)
st.sidebar.title("DIAGNÓSTICO E GOVERNANÇA")
secao = st.sidebar.radio(
    "Navegue pelo conteúdo:",
    [
        "0. Capa e Introdução",
        "1. Fato Central",
        "2. Lógica Sistêmica (Causa)",
        "3. Manifestação por Área",
        "4. Pontos Cegos Estratégicos",
        "5. Riscos Reais",
        "6. Leitura Executiva",
        "7. Direção Lógica",
        "8. Mapa de Governança",
        "9. Papéis-Chave",
        "10. Gates Formais (Bloqueios)",
        "11. Regras e Indicadores",
        "12. Visão Atual vs Esperada",
        "13. RACI e Recomendações",
        "14. Checklists Detalhados",
        "15. Rotina Semanal de Governança"
    ]
)

# --- CONTEÚDO INTEGRAL ---

if secao == "0. Capa e Introdução":
    st.image("Status Apresentação.png", use_container_width=True)
    st.title("DIAGNÓSTICO GERAL INTEGRADO")
    st.subheader("Status Marcenaria – Visão Sistêmica")
    st.markdown("---")
    st.info('“Sucesso nada mais é do que algumas disciplinas simples, praticadas todos os dias.”')
    st.write("**Jim Rohn** – empreendedor americano e grande influência na gestão industrial dos EUA.")
    st.write("**Legenda:** Gate = Ponto de controle.")

elif secao == "1. Fato Central":
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

elif secao == "2. Lógica Sistêmica (Causa)":
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

elif secao == "3. Manifestação por Área":
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
        st.write("* Apaga incêndios criados upstream.")
        st.write("* Compra com informação incompleta.")
        st.write("* Vive urgência como rotina.")
        st.write("➡️ **É amortecedor do caos, não causa.**")

    with col2:
        st.markdown("### 🟩 Financeiro")
        st.write("* Conhece o caixa atual.")
        st.write("* Não controla o fluxo futuro.")
        st.write("* Prioriza pagamento por urgência, não por planejamento.")
        st.write("* “Não” técnico não é respeitado.")
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

elif secao == "4. Pontos Cegos Estratégicos":
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

elif secao == "5. Riscos Reais":
    st.header("5️⃣ Riscos Reais se nada mudar")
    st.markdown("""
    * Margem corroída por retrabalho invisível.
    * Caixa sempre sob stress.
    * Fornecedores caros viram “salvadores”.
    * Dependência de pessoas-chave (risco operacional).
    * Escala impossível.
    * Qualidade e prazo baseados em heróis, não em processo.
    """)

elif secao == "6. Leitura Executiva":
    st.header("6️⃣ Leitura Executiva Correta")
    st.success("O problema da Status não é operacional, é estrutural.")
    st.write("""
    **Sem:**
    * Dono do pedido,
    * PCP com poder,
    * Produção programada,
    * Governança real,
    
    Qualquer melhoria em compras, financeiro ou logística será paliativa.
    """)

elif secao == "7. Direção Lógica":
    st.header("7️⃣ Direção lógica (não plano ainda)")
    st.subheader("Ordem obrigatória de ataque:")
    st.write("1. **Dono do pedido** (autoridade real)")
    st.write("2. **Gate formal** de entrada e mudança")
    st.write("3. **PCP controlador** (não lançador)")
    st.write("4. **Programação mínima** obrigatória")
    st.write("5. **Governança financeira** com veto técnico")
    st.write("6. **Logística integrada** ao prazo, não executora cega")

elif secao == "8. Mapa de Governança":
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

elif secao == "9. Papéis-Chave":
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

elif secao == "10. Gates Formais (Bloqueios)":
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

elif secao == "11. Regras e Indicadores":
    st.header("5️⃣ Regra de Ouro (sem exceção)")
    st.error("❗ Mudança de projeto = novo mini-gate")
    st.write("Toda mudança exige: registro escrito, impacto em prazo, impacto em custo e nova validação.")
    st.warning("👉 Mudança sem registro = não existe.")
    
    st.header("7️⃣ Indicador-chave de sucesso")
    st.metric("% de pedidos que atravessam o fluxo sem quebra de gate", "Se sobe: Urgência cai / Retrabalho cai")
    
    st.header("8️⃣ Verdade dura")
    st.write("Se este mapa não for implantado integralmente, ele vira “mais um desenho bonito” e o sistema informal vence de novo.")
    st.success("Governança não se negocia, se impõe.")

elif secao == "12. Visão Atual vs Esperada":
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

elif secao == "13. RACI e Recomendações":
    st.header("RACI (ERCI) FORMAL – GOVERNANÇA")
    st.write("**Legenda:** E (Executor), R (Responsável), C (Consultado), I (Informado).")
    st.info("Regra inegociável: cada atividade tem UM único R.")
    
    st.subheader("9️⃣ Alertas de Burla")
    st.warning("* 'Só dessa vez libera'\n* 'Depois a gente formaliza'\n* 'É urgente'\n* 'Sempre foi assim'")
    st.error("👉 Qualquer exceção mata o ERCI.")
    
    st.subheader("1️⃣0️⃣ Recomendações Práticas")
    st.write("* O ERCI deve virar documento oficial assinado.")
    st.write("* Gate sem R definido = pedido devolvido.")
    st.write("* Primeiro mês vai gerar atrito → isso é sinal de sucesso.")
    st.write("* Quem reclamar está perdendo poder informal.")

elif secao == "14. Checklists Detalhados":
    st.header("CHECKLISTS OPERACIONAIS POR GATE")
    
    with st.expander("📝 GATE 1 — ACEITE TÉCNICO"):
        st.write("**Responsável:** Dono do Pedido | **Executor:** PCP")
        st.markdown("""
        * **Inf. Comerciais:** Pedido no sistema, Cliente id, Tipo de obra, Responsável id.
        * **Escopo Técnico:** Projeto mínimo, Ambientes, Materiais principais, Itens fora do padrão.
        * **Prazo:** Solicitado registrado, Avaliado tecnicamente, Risco identificado.
        * **Governança:** Dono definido, PCP validou, Aprovado formalmente.
        """)
        st.error("Critérios de Bloqueio: Projeto incompleto, Dono indefinido, Prazo inviável.")

    with st.expander("📝 GATE 2 — LIBERAÇÃO DE PRODUÇÃO"):
        st.write("**Responsável:** PCP | **Executor:** Produção")
        st.markdown("""
        * **Planejamento:** Sequenciado, Capacidade validada, Gargalo id e protegido.
        * **Projeto:** Técnico liberado, Medidas conferidas, Versão registrada.
        * **Comunicação:** Produção ciente, Prazo interno, Alterações registradas.
        """)
        st.error("Critérios de Bloqueio: Fora da sequência, Gargalo saturado, Sem liberação formal.")

    with st.expander("📝 GATE 3 — MATERIAL GARANTIDO"):
        st.write("**Responsável:** Financeiro | **Executor:** Compras")
        st.markdown("""
        * **Materiais:** Lista validada, Quantidades conferidas, Especiais id.
        * **Compras:** Fornecedores id, Lead times confirmados, Datas registradas.
        * **Financeiro:** Impacto no caixa, Compra autorizada, Pagamento definido.
        """)
        st.error("Critérios de Bloqueio: Material crítico não comprado, Financeiro não aprovou, Lead time incompatível.")

    with st.expander("📝 GATE 4 — LIBERAÇÃO DE ENTREGA"):
        st.write("**Responsável:** Dono do Pedido | **Executor:** Logística")
        st.markdown("""
        * **Produto:** Produção concluída, Qualidade conferida, Itens separados.
        * **Logística:** Checklist de carga, Frota definida, Rota planejada.
        * **Prazo:** Data validada c/ logística, Cliente informado, Equipe alinhada.
        """)
        st.error("Critérios de Bloqueio: Produto incompleto, Falta de frota, Prazo não validado.")

elif secao == "15. Rotina Semanal de Governança":
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

# Rodapé lateral
st.sidebar.markdown("---")
st.sidebar.caption("Status Marcenaria - Visão Sistêmica 2026")
