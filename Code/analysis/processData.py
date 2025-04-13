import pandas as pd
import os
from pathlib import Path

current_dir = Path(__file__).parent
input_csv = current_dir.parent / "results" / "pullRequestsFinal.csv"
output_csv = current_dir.parent / "results" / "datasetProcessado.csv"
plots_dir = current_dir.parent / "plots"

os.makedirs(output_csv.parent, exist_ok=True)
os.makedirs(plots_dir, exist_ok=True)

try:
    df = pd.read_csv(input_csv)
    print(f"✅ Dataset carregado: {len(df)} PRs")
except FileNotFoundError:
    print(f"❌ Arquivo {input_csv} não encontrado. Execute main.py primeiro.")
    exit()

df = df[
    (df['reviews'] >= 1) &
    ((df['time_to_merge'] >= 1) | (df['time_to_close'] >= 1))
].copy()

df['total_lines'] = df['additions'] + df['deletions']
df['has_description'] = df['description_length'] > 0
df['interactions'] = df['comments'] + df['reviews']
df['review_density'] = df['reviews'] / df['time_to_merge']

required_columns = ['state', 'changed_files', 'time_to_merge', 'description_length',
                   'comments', 'reviews', 'total_lines', 'has_description',
                   'interactions', 'review_density']

for col in required_columns:
    if col not in df.columns:
        df[col] = 0

df.to_csv(output_csv, index=False)
print(f"🚀 Dataset processado salvo em {output_csv} (Lab03S02 concluído).")