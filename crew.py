from crewai import Crew, Task
from crew import load_agents  # Função gerada automaticamente pelo CrewAI CLI para carregar agents.yaml

def main():
    # Carrega todos os agentes definidos em agents.yaml
    agentes = load_agents()

    # Task 1: agente 'pesquisador' deverá usar a ferramenta para buscar dados
    tarefa_pesquisa = Task(
        description=(
            "1. Use a tool 'buscar_no_falso_api' para pesquisar sobre '{tópico}'.\n"
            "2. Organize os resultados em tópicos claros.\n"
            "3. Retorne a lista de tópicos e citações obtidas."
        ),
        expected_output="Lista de tópicos e referências sobre '{tópico}'.",
        agent="pesquisador"
    )

    # Task 2: agente 'redator' recebe a saída do pesquisador e gera texto final
    tarefa_redacao = Task(
        description=(
            "1. Receba os tópicos e referências entregues pelo pesquisador.\n"
            "2. Crie um relatório coeso, com introdução, desenvolvimento e conclusão.\n"
            "3. Apresente o relatório completo em formato de texto."
        ),
        expected_output="Relatório final sobre '{tópico}'.",
        agent="redator"
    )

    # Cria o crew passando a lista de agentes e a sequência de tarefas
    crew = Crew(
        agents=agentes,
        tasks=[tarefa_pesquisa, tarefa_redacao]
    )

    # Executa o crew com o parâmetro 'tópico'
    resultados = crew.kickoff(parameters={"tópico": "Inteligência Artificial em Marketing"})

    # Exibe os resultados no terminal
    print("\n===== Resultados Obtidos =====\n")
    for nome_agente, output in resultados.items():
        print(f"Agente '{nome_agente}' produziu:\n{output}\n")

if __name__ == "__main__":
    main()
