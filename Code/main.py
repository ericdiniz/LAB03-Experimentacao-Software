from repo_collector import get_repositories
from pr_collector import get_repository_prs
import csv
import os
import time
from datetime import timedelta
from config import CONFIG

def format_time(seconds):
    return str(timedelta(seconds=seconds)).split('.')[0]

def save_to_csv(data, filename):
    os.makedirs('results', exist_ok=True)
    filepath = os.path.join('resultados', filename)

    fieldnames = [
        "repo", "number", "state", "created_at", "merged_at", "closed_at",
        "additions", "deletions", "changed_files", "description_length",
        "comments", "reviews", "time_to_merge", "time_to_close"
    ]

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception:
        return False

def main():
    start_time = time.time()
    print(f"\n=== INÍCIO DA COLETA {time.strftime('%d/%m %H:%M')} ===")

    try:
        print("\nFase 1: Buscando repositórios válidos...")
        repositories = get_repositories()

        if not repositories:
            print("\nFalha crítica: Não foi possível obter repositórios válidos")
            return

        print(f"\nFase 2: Coletando PRs dos {len(repositories)} repositórios...")
        all_prs = []

        for i, repo in enumerate(repositories, 1):
            owner, name = repo.split('/')
            print(f"\n[{i}/{len(repositories)}] Processando {owner}/{name}")

            prs = get_repository_prs(owner, name)
            if prs:
                all_prs.extend(prs)
                print(f"PRs válidos coletados: {len(prs)}")

            if i % 10 == 0:
                save_to_csv(all_prs, f"partial_{i}.csv")

        if save_to_csv(all_prs, "pullRequestsFinal.csv"):
            total_time = time.time() - start_time
            print(f"\n=== COLETA CONCLUÍDA ===")
            print(f"Horário de término: {time.strftime('%d/%m %H:%M')}")
            print(f"Tempo total: {format_time(total_time)}")
            print(f"Repositórios processados: {len(repositories)}")
            print(f"Total de PRs coletados: {len(all_prs)}")
            print(f"Arquivo gerado: resultados/pull_requests_final.csv")

    except KeyboardInterrupt:
        print("\nColeta interrompida pelo usuário!")
        if 'all_prs' in locals() and len(all_prs) > 0:
            save_to_csv(all_prs, "partial_interrupted.csv")
    except Exception:
        print("\nErro inesperado")

if __name__ == "__main__":
    main()