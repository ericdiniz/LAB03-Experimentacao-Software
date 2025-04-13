import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import os
from pathlib import Path

# Configurações iniciais
current_dir = Path(__file__).parent
input_csv = current_dir.parent / "results" / "datasetProcessado.csv"
plots_dir = current_dir.parent / "plots"
os.makedirs(plots_dir, exist_ok=True)

# Paleta de cores
CORES = {
    'aprovado': '#4CAF50',  # Verde
    'rejeitado': '#F44336', # Vermelho
    'destaque': '#2196F3'   # Azul
}

# Carrega os dados
df = pd.read_csv(input_csv)

# Configuração geral dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12

# --- Dimensão A: Feedback Final (Status do PR) ---

# RQ01: Tamanho vs Status
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=df,
    x='state',
    y='changed_files',
    estimator='median',
    hue='state',
    palette=[CORES['aprovado'], CORES['rejeitado']],
    errorbar=None,
    legend=False
)
plt.title("RQ01: Tamanho Médio de PRs por Status de Aprovação", pad=15)
plt.xlabel("Status do Pull Request", labelpad=10)
plt.ylabel("Número Médio de Arquivos Alterados", labelpad=10)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Aprovados (MERGED)", "Rejeitados (CLOSED)"])

# Adiciona valores nas barras
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1f}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10),
                textcoords='offset points', fontsize=11)
plt.savefig(plots_dir / "RQ01_tamanho_status.png", bbox_inches='tight')
plt.close()

# RQ02: Tempo vs Status
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    data=df,
    x='state',
    y='time_to_merge',
    showfliers=False,
    hue='state',
    palette=[CORES['aprovado'], CORES['rejeitado']],
    width=0.5,
    legend=False
)
plt.title("RQ02: Tempo de Análise por Status de Aprovação", pad=15)
plt.xlabel("Status do Pull Request", labelpad=10)
plt.ylabel("Tempo de Análise (horas)", labelpad=10)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Aprovados (MERGED)", "Rejeitados (CLOSED)"])
plt.savefig(plots_dir / "RQ02_tempo_status.png", bbox_inches='tight')
plt.close()

# RQ03: Descrição vs Status
plt.figure(figsize=(10, 6))
ax = sns.violinplot(
    data=df,
    x='state',
    y='description_length',
    hue='state',
    palette=[CORES['aprovado'], CORES['rejeitado']],
    cut=0,
    legend=False
)
plt.title("RQ03: Tamanho da Descrição por Status de Aprovação", pad=15)
plt.xlabel("Status do Pull Request", labelpad=10)
plt.ylabel("Número de Caracteres na Descrição", labelpad=10)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Aprovados (MERGED)", "Rejeitados (CLOSED)"])
plt.savefig(plots_dir / "RQ03_descricao_status.png", bbox_inches='tight')
plt.close()

# RQ04: Interações vs Status
plt.figure(figsize=(12, 6))
df['interactions_binned'] = pd.cut(df['interactions'], bins=range(0, 20, 2))
ax = sns.countplot(
    data=df,
    x='interactions_binned',
    hue='state',
    palette=[CORES['aprovado'], CORES['rejeitado']]
)
plt.title("RQ04: Número de Interações por Status de Aprovação", pad=15)
plt.xlabel("Número Total de Interações (comentários + revisões)", labelpad=10)
plt.ylabel("Contagem de PRs", labelpad=10)
plt.legend(title="Status", labels=["Aprovados", "Rejeitados"])
plt.xticks(rotation=45)
plt.savefig(plots_dir / "RQ04_interacoes_status.png", bbox_inches='tight')
plt.close()

# --- Dimensão B: Número de Revisões ---

# RQ05: Tamanho vs Revisões
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='changed_files', y='reviews',
           scatter_kws={'alpha':0.3, 'color': CORES['destaque']},
           line_kws={'color': 'red'})
plt.title("RQ05: Relação entre Tamanho do PR e Número de Revisões", pad=15)
plt.xlabel("Número de Arquivos Alterados", labelpad=10)
plt.ylabel("Número de Revisões", labelpad=10)
plt.savefig(plots_dir / "RQ05_tamanho_revisoes.png", bbox_inches='tight')
plt.close()

# RQ06: Tempo vs Revisões
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='time_to_merge', y='reviews',
           scatter_kws={'alpha':0.3, 'color': CORES['destaque']},
           line_kws={'color': 'red'})
plt.title("RQ06: Relação entre Tempo de Análise e Número de Revisões", pad=15)
plt.xlabel("Tempo de Análise (horas)", labelpad=10)
plt.ylabel("Número de Revisões", labelpad=10)
plt.savefig(plots_dir / "RQ06_tempo_revisoes.png", bbox_inches='tight')
plt.close()

# RQ07: Descrição vs Revisões
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='description_length', y='reviews',
           scatter_kws={'alpha':0.3, 'color': CORES['destaque']},
           line_kws={'color': 'red'})
plt.title("RQ07: Relação entre Descrição e Número de Revisões", pad=15)
plt.xlabel("Tamanho da Descrição (caracteres)", labelpad=10)
plt.ylabel("Número de Revisões", labelpad=10)
plt.savefig(plots_dir / "RQ07_descricao_revisoes.png", bbox_inches='tight')
plt.close()

# RQ08: Interações vs Revisões
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='comments', y='reviews',
           scatter_kws={'alpha':0.3, 'color': CORES['destaque']},
           line_kws={'color': 'red'})
plt.title("RQ08: Relação entre Comentários e Número de Revisões", pad=15)
plt.xlabel("Número de Comentários", labelpad=10)
plt.ylabel("Número de Revisões", labelpad=10)
plt.savefig(plots_dir / "RQ08_comentarios_revisoes.png", bbox_inches='tight')
plt.close()

print("✅ Todos os gráficos foram gerados com sucesso!")