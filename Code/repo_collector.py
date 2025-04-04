import csv
import time
from datetime import datetime
import requests # type: ignore
from config import CONFIG

def fetch_repositories():
    params = {"q": "stars:>1", "sort": "stars", "order": "desc", "per_page": 100}
    repos = []
    page = 1

    while len(repos) < CONFIG["MAX_REPOS"]:
        params["page"] = page
        response = requests.get(
            f"{CONFIG['GITHUB_API_URL']}/search/repositories",
            params=params,
            headers=CONFIG["HEADERS"]
        )
        response.raise_for_status()
        data = response.json()
        repos.extend(data["items"])
        if len(data["items"]) < 100:
            break
        page += 1
        time.sleep(CONFIG["REQUEST_DELAY"])

    return repos[:CONFIG["MAX_REPOS"]]

def save_repositories(repos):
    filename = f"repos.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "full_name", "stargazers_count", "html_url", "has_issues"])
        for repo in repos:
            writer.writerow([
                repo["id"],
                repo["full_name"],
                repo["stargazers_count"],
                repo["html_url"],
                repo["has_issues"]
            ])

    return filename

if __name__ == "__main__":
    repositories = fetch_repositories()
    output_file = save_repositories(repositories)
    print(f"Saved: {output_file}")