# LABORATÓRIO 03 - Caracterizando a atividade de code review no GitHub

## Informações sobre a Avaliação

| Item      | Detalhes                   |
| --------- | -------------------------- |
| Código    | LAB03                      |
| Atividade | Laboratório 03 - 20 pontos |

### Informações Docente

| Curso                  | Disciplina                                | Turno | Período/Sala |
| ---------------------- | ----------------------------------------- | ----- | ------------ |
| Engenharia de Software | Laboratório de Experimentação de Software | NOITE | 6º           |

**Professor(a):** João Paulo Carneiro Aramuni

## Introdução

A prática de code review tornou-se fundamental nos processos ágeis de desenvolvimento. Consiste na inspeção do código por desenvolvedores antes da integração à base principal, garantindo qualidade e evitando defeitos. No GitHub, isso ocorre através de Pull Requests (PRs) que são avaliados e discutidos pelos colaboradores do projeto.

**Objetivo:** Analisar PRs em repositórios populares do GitHub para identificar variáveis que influenciam no merge de um PR.

## Metodologia

### 1. Criação do Dataset

**Critérios de seleção:**
- Repositórios entre os 200 mais populares do GitHub
- Com pelo menos 100 PRs (MERGED + CLOSED)
- PRs com status MERGED ou CLOSED
- Com pelo menos uma revisão (total count do campo review)
- Tempo de revisão > 1 hora (diferença entre criação e merge/close)

### 2. Questões de Pesquisa

#### A: Feedback Final das Revisões (Status do PR)

| Código | Questão de Pesquisa                               |
| ------ | ------------------------------------------------- |
| RQ 01  | Relação entre tamanho dos PRs e feedback final    |
| RQ 02  | Relação entre tempo de análise e feedback final   |
| RQ 03  | Relação entre descrição dos PRs e feedback final  |
| RQ 04  | Relação entre interações nos PRs e feedback final |

#### B: Número de Revisões

| Código | Questão de Pesquisa                                   |
| ------ | ----------------------------------------------------- |
| RQ 05  | Relação entre tamanho dos PRs e número de revisões    |
| RQ 06  | Relação entre tempo de análise e número de revisões   |
| RQ 07  | Relação entre descrição dos PRs e número de revisões  |
| RQ 08  | Relação entre interações nos PRs e número de revisões |

### 3. Definição de Métricas

| Métrica          | Detalhes                                                  |
| ---------------- | --------------------------------------------------------- |
| Tamanho          | Número de arquivos; total de linhas adicionadas/removidas |
| Tempo de Análise | Intervalo entre criação do PR e última atividade          |
| Descrição        | Número de caracteres do corpo do PR (markdown)            |
| Interações       | Número de participantes; número de comentários            |

## Relatório Final

**Estrutura:**
1. Introdução com hipóteses informais
2. Metodologia utilizada
3. Resultados por questão de pesquisa
4. Discussão comparando hipóteses x resultados

**Requisitos:**
- Utilizar teste estatístico (Spearman ou Pearson) para correlações
- Justificar escolha do teste
- Apresentar valores medianos dos dados

## Processo de Desenvolvimento

| Etapa    | Descrição                                  | Pontos | Prazo (Grupo 1) | Prazo (Grupo 2) |
| -------- | ------------------------------------------ | ------ | --------------- | --------------- |
| Lab03S01 | Seleção de repositórios + script de coleta | 5      | 05/05           | 01/05           |
| Lab03S02 | Dataset completo + relatório preliminar    | 5      | -               | -               |
| Lab03S03 | Análise e relatório final                  | 10     | 06/05           | 02/05           |

**Valor total:** 20 pontos

## Integrantes

- Eric Rodrigues Diniz
- Pablo Guilherme
- Ian

## Licença
[MIT License](LICENSE)