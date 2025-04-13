# Hipóteses Iniciais - Análise de Code Review no GitHub

## (i) Introdução

Este estudo investiga como características técnicas e sociais de Pull Requests (PRs) afetam seu processo de revisão em projetos open-source. Analisamos 525,234 PRs dos 200 repositórios mais populares do GitHub.

## (ii) Metodologia

- **Dataset**: PRs com pelo menos 1 revisão e tempo de análise >1h
- **Variáveis analisadas**:
  - Tamanho (arquivos/linhas alteradas)
  - Tempo de análise
  - Qualidade da descrição
  - Nível de interações
- **Técnicas**: Análise estatística descritiva e correlação de Spearman

## (iii) Hipóteses Informais

### DA: Feedback Final

**RQ01**: PRs menores têm maior taxa de aprovação
**RQ02**: PRs mais rápidos são mais aprovados
**RQ03**: Descrições detalhadas aumentam aprovação
**RQ04**: Muitas interações indicam PRs problemáticos

### B: Número de Revisões

**RQ05**: PRs grandes exigem mais revisões
**RQ06**: Revisões prolongadas geram mais ciclos
**RQ07**: Boas descrições reduzem revisões
**RQ08**: Discussões intensas levam a mais revisões
