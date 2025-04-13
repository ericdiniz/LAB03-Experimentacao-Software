import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import os

# Configuração
INPUT_CSV = "../data/dataset_processado.csv"
PLOTS_DIR = "../plots"

# Carrega os dados processados
try:
    df = pd.read_csv(INPUT_CSV)
except FileNotFoundError:
    print(f"❌ Execute process_data.py primeiro para gerar {INPUT_CSV}")
    exit()

# Cria pasta para gráficos
os.makedirs(PLOTS_DIR, exist_ok=True)

# ---- Análises ----
# RQ01: Tamanho vs. Status
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='state', y='changed_files', showfliers=False)
plt.title("RQ01: Arquivos Alterados por Status do PR")
plt.savefig(f"{PLOTS_DIR}/rq01_boxplot.png", bbox_inches='tight', dpi=300)

# RQ05: Correlação Tamanho x Revisões
corr, p = spearmanr(df['total_lines'], df['reviews'])
print(f"📊 RQ05: Correlação Spearman (Tamanho x Revisões): {corr:.2f} (p-value: {p:.4f})")

# RQ02: Tempo de Merge com/sem Descrição
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='has_description', y='time_to_merge', hue='state', ci=None)
plt.title("RQ02: Tempo de Merge por Presença de Descrição")
plt.savefig(f"{PLOTS_DIR}/rq02_barplot.png", bbox_inches='tight', dpi=300)

print(f"📈 Gráficos salvos em {PLOTS_DIR} (Lab03S03 concluído).")