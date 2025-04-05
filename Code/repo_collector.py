import requests
from config import CONFIG

def get_top_repositories():  # Nome alterado para match com a importação
    query = """
    {
      search(query: "stars:>5000", type: REPOSITORY, first: 10) {
        edges {
          node {
            ... on Repository {
              nameWithOwner
              stargazerCount
              pullRequests(states: [CLOSED, MERGED]) {
                totalCount
              }
            }
          }
        }
      }
    }
    """

    try:
        response = requests.post(
            CONFIG["GITHUB_API_URL"],
            json={"query": query},
            headers=CONFIG["HEADERS"],
            timeout=CONFIG["TIMEOUT"]
        )
        response.raise_for_status()

        repos = [
            edge["node"] for edge in
            response.json()["data"]["search"]["edges"]
            if edge["node"]["pullRequests"]["totalCount"] >= CONFIG["MIN_PRS"]
        ]

        return repos[:CONFIG["MAX_REPOS"]]

    except Exception as e:
        print(f"Erro ao buscar repositórios: {str(e)}")
        return []