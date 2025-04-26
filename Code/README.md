COMO USAR O COLETOR DE PRs DO GITHUB

1. INSTALAÇÃO:
   - Tenha Python 3.8+ instalado
   - Execute no terminal:
     git clone [URL_DO_REPOSITORIO]
     cd [NOME_DO_REPOSITORIO]
     python -m venv venv
     venv\Scripts\activate (Windows) OU source venv/bin/activate (Linux/Mac)
     pip install -r requirements.txt

2. CONFIGURAR TOKEN:
   - Crie um arquivo .env na pasta do projeto com:
     GITHUB_TOKEN=seu_token_do_github
   - Obtenha o token em: https://github.com/settings/tokens
   - Marque as permissões: repo e read:user

3. EXECUTAR:
   python main.py

O que o programa faz:
- Busca os 200 repositórios mais populares
- Filtra apenas os com +100 PRs
- Coleta PRs que:
  * São MERGED ou CLOSED
  * Tem pelo menos 1 review
  * Levaram mais de 1 hora para ser analisados

Arquivos importantes:
- repo_collector.py -> Busca repositórios
- pr_collector.py -> Coleta dados dos PRs
- main.py -> Execução principal
- config.py -> Configurações (não altere)

Saída:
- results/pullRequestsFinal.csv -> Dados completos
- results/partial_*.csv -> Dados parciais

Dicas:
- Pode levar várias horas para completar
- Use Ctrl+C para pausar (salva automaticamente)
- Para testes, altere em main.py: len(repositories) para um número menor
