import requests # type: ignore
import time
from config import CONFIG

def fetch_repos_page(page):
    try:
        response = requests.get(
            f"{CONFIG['REST_API_URL']}/search/repositories",
            params={
                "q": "stars:>1000",
                "sort": "stars",
                "order": "desc",
                "per_page": 100,
                "page": page
            },
            headers=CONFIG["HEADERS"],
            timeout=CONFIG["TIMEOUT"]
        )
        response.raise_for_status()
        return [repo["full_name"] for repo in response.json()["items"]]
    except Exception:
        return []

def check_repo_pr_count(repo_name):
    try:
        owner, name = repo_name.split('/')
        query = """
        query {
          repository(owner: "%s", name: "%s") {
            pullRequests(states: [CLOSED, MERGED]) {
              totalCount
            }
          }
        }
        """ % (owner, name)

        response = requests.post(
            CONFIG["GITHUB_API_URL"],
            json={"query": query},
            headers=CONFIG["HEADERS"],
            timeout=CONFIG["TIMEOUT"]
        )
        response.raise_for_status()
        data = response.json()
        return data["data"]["repository"]["pullRequests"]["totalCount"]
    except Exception:
        return 0

def get_repositories():
    valid_repos = []
    page = 1
    seen_repos = set()

    while len(valid_repos) < 200:
        new_repos = fetch_repos_page(page)
        if not new_repos:
            break

        for repo in new_repos:
            if repo in seen_repos:
                continue
            seen_repos.add(repo)

            pr_count = check_repo_pr_count(repo)
            if pr_count >= 100:
                valid_repos.append(repo)
                print(f"✅ [{len(valid_repos)}/200] {repo} - PRs: {pr_count}")
                if len(valid_repos) >= 200:
                    break

            time.sleep(1)

        page += 1
        if page > 10:
            break

    return valid_repos[:200]