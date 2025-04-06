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
    os.makedirs('resultados', exist_ok=True)
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
    except Exception as e:
        print(f"Erro ao salvar CSV: {str(e)}")
        return False

def main():
    start_time = time.time()
    print(f"\n=== INÍCIO DA COLETA {time.strftime('%d/%m %H:%M')} ===")

    try:
        print("Testando conexão com a API...")
        repositories = get_repositories()

        if not repositories:
            print("\nFalha crítica: Não foi possível obter repositórios")
            print("Soluções possíveis:")
            print("1. Verifique seu token no arquivo .env")
            print("2. Teste manualmente com:")
            print(f"   curl -H \"Authorization: bearer {CONFIG['HEADERS']['Authorization'][7:]}\" https://api.github.com/user")
            print("3. Espere 1 hora se excedeu o rate limit")
            return

        print(f"\nRepositórios encontrados: {len(repositories)}")
        print("Iniciando coleta de PRs...")

        all_prs = []
        for i, repo in enumerate(repositories, 1):
            owner, name = repo["nameWithOwner"].split('/')
            print(f"\n[{i}/{len(repositories)}] Coletando {owner}/{name}")

            prs = get_repository_prs(owner, name)
            if prs:
                all_prs.extend(prs)
                print(f"PRs válidos coletados: {len(prs)}")
            else:
                print("Nenhum PR válido encontrado")

        if save_to_csv(all_prs, "pull_requests.csv"):
            total_time = time.time() - start_time
            print(f"\n=== COLETA CONCLUÍDA ===")
            print(f"Horário de término: {time.strftime('%d/%m %H:%M')}")
            print(f"Tempo total: {format_time(total_time)}")
            print(f"Repositórios processados: {len(repositories)}")
            print(f"Total de PRs coletados: {len(all_prs)}")
            print(f"Arquivo gerado: resultados/pull_requests.csv")
        else:
            print("\nErro ao salvar os dados coletados")

    except KeyboardInterrupt:
        print("\nColeta interrompida pelo usuário!")
        if len(all_prs) > 0:
            if save_to_csv(all_prs, "partial_pull_requests.csv"):
                print("Dados parciais salvos em resultados/partial_pull_requests.csv")
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")

if __name__ == "__main__":
    main()