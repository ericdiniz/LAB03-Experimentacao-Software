import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import os
from pathlib import Path

current_dir = Path(__file__).parent
input_csv = current_dir.parent / "results" / "datasetProcessado.csv"
plots_dir = current_dir.parent / "plots"

try:
    df = pd.read_csv(input_csv)
except FileNotFoundError:
    print(f"❌ Execute processData.py primeiro para gerar {input_csv}")
    exit()

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='state', y='changed_files', showfliers=False)
plt.title("RQ01: Arquivos Alterados por Status do PR")
plt.savefig(plots_dir / "rq01Boxplot.png", bbox_inches='tight')
plt.close()

corr, p = spearmanr(df['total_lines'], df['reviews'])
print(f"📊 RQ05: Correlação Spearman (Tamanho x Revisões): {corr:.2f} (p-value: {p:.4f})")

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='has_description', y='time_to_merge', hue='state', errorbar=None)
plt.title("RQ02: Tempo de Merge por Presença de Descrição")
plt.savefig(plots_dir / "rq02Barplot.png", bbox_inches='tight')
plt.close()

print(f"📈 Gráficos salvos em {plots_dir} (Lab03S03 concluído).")