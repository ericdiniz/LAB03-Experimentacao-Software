from repo_collector import get_repositories
from pr_collector import get_repository_prs
import csv
import os
import time
from datetime import timedelta
from config import CONFIG

def format_time(seconds):
    return str(timedelta(seconds=seconds))

def main():
    start_time = time.time()
    print("=== INÍCIO DA COLETA ===")

    try:
        print("Buscando repositórios...")
        repos = get_repositories()

        if not repos:
            print("AVISO: Verifique seu token e conexão")
            return

        print(f"Repositórios encontrados: {len(repos)}")
        print("Coletando PRs...")

        all_prs = []
        for i, repo in enumerate(repos, 1):
            owner, name = repo["nameWithOwner"].split('/')
            prs = get_repository_prs(owner, name)
            if prs:
                all_prs.extend(prs)
                print(f"{i}/{len(repos)} | {owner}/{name} | PRs: {len(prs)}")

        if all_prs:
            os.makedirs('resultados', exist_ok=True)
            with open('resultados/pull_requests.csv', 'w') as f:
                writer = csv.DictWriter(f, fieldnames=prs[0].keys())
                writer.writeheader()
                writer.writerows(all_prs)

            print(f"\n=== FINALIZADO ===")
            print(f"Tempo total: {format_time(time.time() - start_time)}")
            print(f"PRs coletados: {len(all_prs)}")
        else:
            print("Nenhum PR válido encontrado")

    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()