# Laboratório 03 - Análise de Code Review no GitHub

Repositório para o projeto de Experimentação em Software da PUC Minas, focado em estudar a atividade de code review em repositórios populares do GitHub.

## Integrantes

- Eric Rodrigues Diniz
- Pablo Guilherme
- Ian

## Objetivo

Analisar Pull Requests (PRs) em repositórios populares para entender como diferentes fatores influenciam:

- A decisão de merge/rejeição (status do PR)
- O número de revisões realizadas

## Métricas Analisadas

- **Tamanho do PR**: Número de arquivos e linhas modificadas
- **Tempo de análise**: Duração entre criação e fechamento do PR
- **Descrição**: Tamanho e qualidade da descrição
- **Interações**: Número de participantes e comentários

## Entregas do Projeto

1. **Dataset completo**:
   - Lista dos 200 repositórios mais populares analisados
   - Dados de PRs coletados com todas as métricas definidas

2. **Scripts de coleta**:
   - Código para extração automatizada de dados do GitHub API
   - Processamento dos dados brutos

3. **Análise estatística**:
   - Testes de correlação (Spearman/Pearson)
   - Visualizações dos resultados

4. **Relatório final**:
   - Hipóteses iniciais
   - Metodologia detalhada
   - Resultados e discussão
   - Conclusões sobre cada questão de pesquis
