# Relatório Final - Caracterizando a Atividade de Code Review no GitHub

**Disciplina:** Laboratório de Experimentação de Software
**Professor:** João Paulo Carneiro Aramuni
**Grupo:** [Nome do Grupo]
**Data de Entrega:** [Data]

---

## 1. Introdução

Este relatório apresenta uma análise da atividade de code review em repositórios populares do GitHub, focando em Pull Requests (PRs) que foram submetidos a revisão. O objetivo é identificar variáveis que influenciam no merge de um PR, como tamanho, tempo de análise, descrição e interações.

**Hipóteses Informais:**

- PRs menores têm maior probabilidade de serem aprovados.
- PRs com descrições mais detalhadas recebem feedback mais rápido.
- PRs com mais interações (comentários) tendem a demorar mais para serem mergeados.

---

## 2. Metodologia

### 2.1. Criação do Dataset

Foram selecionados os **200 repositórios mais populares** do GitHub, com pelo menos **100 PRs** (MERGED ou CLOSED). Os PRs analisados atenderam aos seguintes critérios:

- Status: MERGED ou CLOSED.
- Pelo menos uma revisão.
- Tempo de análise superior a uma hora (para evitar revisões automáticas).

### 2.2. Coleta de Dados

As métricas coletadas para cada PR incluem:

- **Tamanho:** Número de arquivos, linhas adicionadas e removidas.
- **Tempo de Análise:** Intervalo entre criação e fechamento/merge.
- **Descrição:** Número de caracteres na descrição do PR.
- **Interações:** Número de participantes e comentários.

### 2.3. Questões de Pesquisa

As análises foram divididas em duas dimensões:

#### A. Feedback Final das Revisões (Status do PR)

- **RQ 01:** Relação entre tamanho do PR e feedback final.
- **RQ 02:** Relação entre tempo de análise e feedback final.
- **RQ 03:** Relação entre descrição do PR e feedback final.
- **RQ 04:** Relação entre interações e feedback final.

#### B. Número de Revisões

- **RQ 05:** Relação entre tamanho do PR e número de revisões.
- **RQ 06:** Relação entre tempo de análise e número de revisões.
- **RQ 07:** Relação entre descrição do PR e número de revisões.
- **RQ 08:** Relação entre interações e número de revisões.

### 2.4. Análise Estatística

Foi utilizado o **teste de correlação de Spearman** para avaliar as relações entre as variáveis, devido à natureza não paramétrica dos dados.

---

## 3. Resultados

### 3.1. Sumarização dos Dados

| Métrica                  | Mediana (PRs MERGED) | Mediana (PRs CLOSED) |
| ------------------------ | -------------------- | -------------------- |
| Tamanho (arquivos)       | X                    | Y                    |
| Tempo de Análise (h)     | X                    | Y                    |
| Descrição (caracteres)   | X                    | Y                    |
| Interações (comentários) | X                    | Y                    |

### 3.2. Correlações Principais

- **RQ 01:** Correlação entre tamanho do PR e status: [valor de correlação].
- **RQ 02:** Correlação entre tempo de análise e status: [valor de correlação].
- **RQ 05:** Correlação entre tamanho do PR e número de revisões: [valor de correlação].

*(Incluir gráficos ou tabelas adicionais conforme necessário.)*

---

## 4. Discussão

### 4.1. Comparação com as Hipóteses

- **Hipótese 1 (PRs menores são aprovados mais rápido):** [Confirmada/Refutada] com base nos dados.
- **Hipótese 2 (Descrições detalhadas aceleram o feedback):** [Confirmada/Refutada].
- **Hipótese 3 (Mais interações aumentam o tempo de análise):** [Confirmada/Refutada].

### 4.2. Limitações

- Os dados estão limitados a repositórios populares, o que pode não representar projetos menores.
- PRs com revisões automáticas foram filtrados, mas alguns falsos positivos podem permanecer.

---

## 5. Conclusão

Este estudo destacou que [principais achados]. As correlações encontradas sugerem que [insights relevantes]. Para trabalhos futuros, seria interessante [sugestões].

---

## Apêndices

### Código Utilizado

- Scripts de coleta: `repo_collector.py`, `pr_collector.py`, `main.py`, `processData.py`, `visualize.py`.
- Bibliotecas: `pandas`, `seaborn`, `matplotlib`, `python`.

### Dataset

- Arquivo final: `pullRequestsFinal.csv`.
