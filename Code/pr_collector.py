import csv
import time
from datetime import datetime
import requests # type: ignore
from config import CONFIG

def fetch_prs(repo_full_name):
    prs = []
    page = 1

    while True:
        url = f"{CONFIG['GITHUB_API_URL']}/repos/{repo_full_name}/pulls"
        params = {"state": "all", "per_page": 100, "page": page}
        response = requests.get(url, params=params, headers=CONFIG["HEADERS"])
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        prs.extend(data)
        page += 1
        time.sleep(CONFIG["REQUEST_DELAY"])

    return prs

def save_prs(prs, repo_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"prs_{repo_name.replace('/', '_')}_{timestamp}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "number", "state", "title", "created_at", "merged_at", "comments"])
        for pr in prs:
            writer.writerow([
                pr["id"],
                pr["number"],
                pr["state"],
                pr["title"],
                pr["created_at"],
                pr.get("merged_at", ""),
                pr["comments"]
            ])

    return filename

if __name__ == "__main__":
    repo_name = input("Repo name (owner/repo): ")
    prs = fetch_prs(repo_name)
    output_file = save_prs(prs, repo_name)
    print(f"Saved: {output_file}")