from crewai import Crew, Task
from crew import load_agents

def main():
    # Carrega os agentes definidos em agents.yaml
    agentes = load_agents()

    # 1) Task: Copywriter gera todo o texto (copy)
    tarefa_copy = Task(
        description=(
            "1. Receba os parâmetros 'produto' e 'produto_descricao'.\n"
            "2. Crie o texto completo para a landing page, incluindo:\n"
            "   - Título principal (hero headline)\n"
            "   - Subtítulo (subheading)\n"
            "   - Proposta de valor clara\n"
            "   - Lista de pelo menos quatro benefícios em bullet points\n"
            "   - Seção de prova social (dois ou três testemunhos ou estatísticas)\n"
            "   - Chamada para ação (CTA) clara, orientando o visitante a comprar ou entrar em contato\n"
            "   - Sugestões de elementos de layout (em texto), como onde colocar imagens, cores e seções principais.\n"
            "3. Retorne somente o copy completo em texto."
        ),
        expected_output="Copy de landing page para '{produto}' com base em {produto_descricao}.",
        agent="criador_landing"
    )

    # 2) Task: Designer de Layout cria wireframe textual baseado no copy
    tarefa_design = Task(
        description=(
            "1. Receba o texto gerado pelo agente 'criador_landing'.\n"
            "2. Crie um wireframe textual detalhado, definindo a estrutura de seções da página:\n"
            "   - Hero section (posicionamento de título, subtítulo e imagem de fundo)\n"
            "   - Seção de benefícios (como dispor bullets, ícones e cores)\n"
            "   - Seção de prova social (onde posicionar depoimentos ou estatísticas)\n"
            "   - Seção de FAQ (opcional), explicando dúvidas comuns\n"
            "   - Seção de rodapé (footer) com links e informações de contato\n"
            "3. Sugira hierarquia visual (tamanho de fonte relativo, cores primárias/secundárias) e espaçamentos.\n"
            "4. Retorne apenas o wireframe textual, sem gerar código HTML/CSS ainda."
        ),
        expected_output="Wireframe textual para a landing page de '{produto}'.",
        agent="visual_designer"
    )

    # 3) Task: Web Designer gera HTML e CSS baseados no wireframe e no copy
    tarefa_web = Task(
        description=(
            "1. Receba o copy completo do 'criador_landing' e o wireframe textual do 'visual_designer'.\n"
            "2. Construa o código HTML5 semântico e CSS3 para tornar a landing page responsiva:\n"
            "   - Use tags corretas: <header>, <nav> (se houver), <section>, <article>, <footer>.\n"
            "   - Utilize Flexbox e/ou Grid para estruturar colunas e centralizar conteúdo.\n"
            "   - Defina classes CSS semânticas (ex: .hero, .beneficios, .teste-monial, .cta).\n"
            "   - Inclua comentários no HTML/CSS explicando cada seção.\n"
            "   - Garanta que funcione bem em tela desktop e mobile (uso de media queries básicas).\n"
            "3. Não utilize bibliotecas externas (Bootstrap, Tailwind etc.).\n"
            "4. Retorne dois blocos: (a) arquivo 'index.html' completo, (b) arquivo 'styles.css'."
        ),
        expected_output="Código HTML e CSS completo para a landing page de '{produto}'.",
        agent="web_designer"
    )

    # 4) Task: QA Expert revisa e unifica resultados finais
    tarefa_qa = Task(
        description=(
            "1. Receba o copy (texto), o wireframe textual e o código HTML/CSS produzidos pelos agentes anteriores.\n"
            "2. Revise gramática, ortografia e consistência do copy.\n"
            "3. Verifique a semântica HTML e potenciais erros no CSS (classes duplicadas, hierarquia incorreta, faltam alt em imagens etc.).\n"
            "4. Sugira correções pontuais em texto e no código (se houver) mantendo o estilo original.\n"
            "5. Retorne uma versão final consolidada com:\n"
            "   - Copy corrigido (se necessário)\n"
            "   - Wireframe textual resumido com eventuais ajustes\n"
            "   - HTML final corrigido (se houve correções)\n"
            "   - CSS final corrigido"
        ),
        expected_output="Artefato final revisado e pronto para publicação.",
        agent="qa_expert"
    )

    # Monta o crew com a sequência de tarefas
    crew = Crew(
        agents=agentes,
        tasks=[tarefa_copy, tarefa_design, tarefa_web, tarefa_qa]
    )

    # Define parâmetros iniciais (nome e descrição do produto)
    parametros = {
        "produto": "SuperBlend Suplemento",
        "produto_descricao": (
            "Fórmula vegana com 20 g de proteína isolada, sem lactose, sabor natural de baunilha. "
            "Voltado para atletas veganos que buscam recuperação muscular rápida e energia limpa."
        )
    }

    # Executa o crew (cada agente recebe seu input e passa output ao próximo)
    resultados = crew.kickoff(parameters=parametros)

    # Exibe, em sequência, o output de cada agente
    print("\n===== COPYWRITER GEROU =====\n")
    print(resultados["criador_landing"])
    print("\n===== WIRE_FRAME GERADO =====\n")
    print(resultados["visual_designer"])
    print("\n===== HTML E CSS GERADOS =====\n")
    # Para facilitar, exibiremos HTML e CSS separados conforme o retorno do agente web_designer
    bloco_web = resultados["web_designer"]
    # Supondo que o agente devolveu algo como: "=== index.html ===\n<...>\n=== styles.css ===\n<...>"
    print(bloco_web)
    print("\n===== QA FINAL =====\n")
    print(resultados["qa_expert"])

if __name__ == "__main__":
    main()
