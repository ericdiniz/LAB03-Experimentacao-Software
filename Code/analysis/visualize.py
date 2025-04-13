import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import os
from pathlib import Path

current_dir = Path(__file__).parent
input_csv = current_dir.parent / "results" / "datasetProcessado.csv"
plots_dir = current_dir.parent / "plots"

os.makedirs(plots_dir, exist_ok=True)

df = pd.read_csv(input_csv)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# A: Feedback Final (Status do PR)
# RQ01: Tamanho vs Status
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='state', y='changed_files', showfliers=False)
plt.title("RQ01: Arquivos Alterados por Status do PR")
plt.savefig(plots_dir / "RQ01_size_vs_status.png", bbox_inches='tight')
plt.close()

# RQ02: Tempo vs Status
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='state', y='time_to_merge', showfliers=False)
plt.title("RQ02: Tempo de Análise por Status do PR")
plt.savefig(plots_dir / "RQ02_time_vs_status.png", bbox_inches='tight')
plt.close()

# RQ03: Descrição vs Status
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='state', y='description_length', showfliers=False)
plt.title("RQ03: Tamanho da Descrição por Status do PR")
plt.savefig(plots_dir / "RQ03_desc_vs_status.png", bbox_inches='tight')
plt.close()

# RQ04: Interações vs Status
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='state', y='comments', showfliers=False)
plt.title("RQ04: Número de Comentários por Status do PR")
plt.savefig(plots_dir / "RQ04_comments_vs_status.png", bbox_inches='tight')
plt.close()

# B: Número de Revisões
# RQ05: Tamanho vs Revisões
plt.figure(figsize=(10,6))
sns.regplot(data=df, x='changed_files', y='reviews', scatter_kws={'alpha':0.3})
plt.title("RQ05: Arquivos Alterados vs Número de Revisões")
plt.savefig(plots_dir / "RQ05_size_vs_reviews.png", bbox_inches='tight')
plt.close()

# RQ06: Tempo vs Revisões
plt.figure(figsize=(10,6))
sns.regplot(data=df, x='time_to_merge', y='reviews', scatter_kws={'alpha':0.3})
plt.title("RQ06: Tempo de Análise vs Número de Revisões")
plt.savefig(plots_dir / "RQ06_time_vs_reviews.png", bbox_inches='tight')
plt.close()

# RQ07: Descrição vs Revisões
plt.figure(figsize=(10,6))
sns.regplot(data=df, x='description_length', y='reviews', scatter_kws={'alpha':0.3})
plt.title("RQ07: Tamanho da Descrição vs Número de Revisões")
plt.savefig(plots_dir / "RQ07_desc_vs_reviews.png", bbox_inches='tight')
plt.close()

# RQ08: Interações vs Revisões
plt.figure(figsize=(10,6))
sns.regplot(data=df, x='comments', y='reviews', scatter_kws={'alpha':0.3})
plt.title("RQ08: Número de Comentários vs Número de Revisões")
plt.savefig(plots_dir / "RQ08_comments_vs_reviews.png", bbox_inches='tight')
plt.close()

# Cálculo de correlações
print("\nCorrelações (Spearman):")
print("RQ05 - Tamanho vs Revisões:", spearmanr(df['changed_files'], df['reviews'])[0])
print("RQ06 - Tempo vs Revisões:", spearmanr(df['time_to_merge'], df['reviews'])[0])
print("RQ07 - Descrição vs Revisões:", spearmanr(df['description_length'], df['reviews'])[0])
print("RQ08 - Comentários vs Revisões:", spearmanr(df['comments'], df['reviews'])[0])

print(f"\n📈 Todos os gráficos salvos em {plots_dir}")