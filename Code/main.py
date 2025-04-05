from repo_collector import get_top_repositories  # Nome corrigido aqui
from pr_collector import get_repository_prs
import csv
from config import CONFIG

def save_to_csv(data, filename):
    if not data:
        return False

    fieldnames = [
        "repo", "number", "state", "created_at", "merged_at", "closed_at",
        "additions", "deletions", "changed_files", "description_length",
        "comments", "reviews", "time_to_merge", "time_to_close"
    ]

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Erro ao salvar CSV: {str(e)}")
        return False

def main():
    print("Iniciando coleta de dados...")

    repositories = get_top_repositories()  # Agora com nome consistente
    if not repositories:
        print("Nenhum repositório encontrado")
        return

    all_prs = []

    for repo in repositories:
        owner, name = repo["nameWithOwner"].split('/')
        print(f"Coletando PRs de {owner}/{name}...")

        prs = get_repository_prs(owner, name)
        if prs:
            all_prs.extend(prs)
            print(f"Encontrados {len(prs)} PRs válidos")

    if save_to_csv(all_prs, "pull_requests.csv"):
        print(f"Coleta concluída. Total de PRs coletados: {len(all_prs)}")
    else:
        print("Erro ao salvar os dados")

if __name__ == "__main__":
    main()