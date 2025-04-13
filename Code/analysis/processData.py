import pandas as pd
import os

# Configuração
INPUT_CSV = "../data/pull_requests_final.csv"
OUTPUT_CSV = "../data/dataset_processado.csv"

# Carrega os dados brutos
try:
    df = pd.read_csv(INPUT_CSV)
    print(f"✅ Dataset carregado: {len(df)} PRs")
except FileNotFoundError:
    print(f"❌ Arquivo {INPUT_CSV} não encontrado. Execute main.py primeiro.")
    exit()

# Filtros e métricas (exigidos no laboratório)
df = df[
    (df['reviews'] >= 1) &
    ((df['time_to_merge'] >= 1) | (df['time_to_close'] >= 1))
].copy()

df['total_lines'] = df['additions'] + df['deletions']
df['has_description'] = df['description_length'] > 0

# Salva o dataset processado
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
df.to_csv(OUTPUT_CSV, index=False)
print(f"🚀 Dataset processado salvo em {OUTPUT_CSV} (Lab03S02 concluído).")