from repo_collector import fetch_repositories, save_repositories
from pr_collector import fetch_prs, save_prs
import csv

def main():
    print("Starting data collection...")

    repos = fetch_repositories()
    repos_file = save_repositories(repos)
    print(f"Repositories saved to {repos_file}")

    with open(repos_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for repo in reader:
            prs = fetch_prs(repo['full_name'])
            prs_file = save_prs(prs, repo['full_name'].replace('/', '_'))
            print(f"PRs for {repo['full_name']} saved to {prs_file}")

if __name__ == "__main__":
    main()