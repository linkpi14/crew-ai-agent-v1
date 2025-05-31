# Meu Primeiro CrewAI

Este repositório contém o código completo para um projeto CrewAI simples. Após subir no GitHub, você pode direcionar esse repositório para o painel do CrewAI e rodar seu "crew" (conjunto de agentes) sem precisar instalar nada localmente.

## Arquivos

- `agents.yaml`: define os agentes e suas configurações (role, objetivo, LLM, memória etc).
- `crew.py`: script principal que carrega os agentes e dispara as tasks.
- `tools/example_tool.py`: um exemplo de ferramenta customizada que agentes podem usar.
- `requirements.txt`: dependências necessárias.
- `README.md`: este arquivo.

## Como usar

1. Faça o push deste repositório para o seu GitHub.
2. No painel do CrewAI (UI Studio ou CLI), aponte para este repositório. O CrewAI vai detectar `agents.yaml`, baixar as dependências de `requirements.txt` e rodar `crew.py`.
3. Configure suas credenciais de API do LLM (ex: `OPENAI_API_KEY`) no ambiente do CrewAI (Settings → Environment Variables).
4. No painel, clique em "Run Crew" ou equivalente para iniciar a execução. Os agentes irão executar as tarefas definidas em `crew.py`.

## Configurar credenciais

Este projeto espera que você defina, no ambiente de execução, a variável de ambiente:
- `OPENAI_API_KEY`: chave de API da OpenAI (ou outra variável equivalente, dependendo do provedor LLM que você usar).

### Exemplos de comandos usando CLI do CrewAI (opcional)

Caso você use CLI do CrewAI, dentro do painel do CrewAI poderá rodar:
```
# Se quiser testar localmente, mas na nuvem do CrewAI você não precisa:
pip install -r requirements.txt
python crew.py
```

## Descrição básica

Este "crew" tem dois agentes:
1. **pesquisador**: busca dados sobre um tópico usando uma ferramenta customizada (exemplo: busca simulada ou chamada de API).
2. **redator**: pega as informações coletadas pelo pesquisador e gera um relatório final de texto.

O arquivo `tools/example_tool.py` contém uma função fictícia `buscar_no_falso_api` que simula uma busca. Você pode substituir por integrações reais conforme a necessidade.

---

## Licença

Este projeto é de exemplo e está livre para uso. Faça alterações à vontade.
