import requests # type: ignore
import time
from config import CONFIG

def get_repositories():
    query = """
    query ($cursor: String) {
      search(
        query: "stars:>100 sort:stars-desc",
        type: REPOSITORY,
        first: 10,
        after: $cursor
      ) {
        repositoryCount
        edges {
          node {
            ... on Repository {
              nameWithOwner
              pullRequests(states: [CLOSED, MERGED]) {
                totalCount
              }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
    """

    repositories = []
    cursor = None
    attempts = 0

    while len(repositories) < 200 and attempts < 30:
        try:
            response = requests.post(
                CONFIG["GITHUB_API_URL"],
                json={"query": query, "variables": {"cursor": cursor}},
                headers=CONFIG["HEADERS"],
                timeout=240
            )

            if response.status_code != 200:
                print(f"Erro {response.status_code}. Tentativa {attempts + 1}/10")
                attempts += 1
                time.sleep(60)
                continue

            data = response.json()

            if "errors" in data:
                print("Erro na query:", data["errors"][0]["message"])
                break

            new_repos = [
                edge["node"] for edge in data["data"]["search"]["edges"]
                if edge["node"]["pullRequests"]["totalCount"] >= 100
            ]

            repositories.extend(new_repos)
            print(f"✅ Progresso: {len(repositories)}/200 repositórios")

            if not data["data"]["search"]["pageInfo"]["hasNextPage"] or len(repositories) >= 200:
                break

            cursor = data["data"]["search"]["pageInfo"]["endCursor"]
            time.sleep(30)  # Delay maior para evitar rate limit

        except Exception as e:
            print(f"Erro: {str(e)}")
            attempts += 1
            time.sleep(120)

    return repositories[:200]