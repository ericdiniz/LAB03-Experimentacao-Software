import requests
import time
from config import CONFIG

def get_repositories():
    query = """
    query ($cursor: String) {
      search(
        query: "sort:stars-desc",
        type: REPOSITORY,
        first: 50,
        after: $cursor
      ) {
        nodes {
          ... on Repository {
            nameWithOwner
            pullRequests(states: [CLOSED, MERGED]) { totalCount }
          }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
    """

    repos = []
    cursor = None

    while len(repos) < CONFIG["MAX_REPOS"]:
        try:
            response = requests.post(
                CONFIG["GITHUB_API_URL"],
                json={"query": query, "variables": {"cursor": cursor}},
                headers=CONFIG["HEADERS"],
                timeout=CONFIG["TIMEOUT"]
            )
            data = response.json()

            for repo in data["data"]["search"]["nodes"]:
                if repo["pullRequests"]["totalCount"] >= CONFIG["MIN_PRS"]:
                    repos.append(repo)
                    if len(repos) >= CONFIG["MAX_REPOS"]:
                        break

            if not data["data"]["search"]["pageInfo"]["hasNextPage"]:
                break

            cursor = data["data"]["search"]["pageInfo"]["endCursor"]
            time.sleep(CONFIG["REQUEST_DELAY"])

        except Exception:
            break

    return repos