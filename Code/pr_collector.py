import requests
import time
from datetime import datetime
from config import CONFIG

def get_repository_prs(owner, name):
    query_template = f"""
    query ($after: String) {{
      repository(owner: "{owner}", name: "{name}") {{
        pullRequests(
          states: [CLOSED, MERGED]
          first: 50
          after: $after
          orderBy: {{field: CREATED_AT, direction: DESC}}
        ) {{
          nodes {{
            number
            state
            createdAt
            mergedAt
            closedAt
            additions
            deletions
            changedFiles
            body
            comments {{ totalCount }}
            reviews {{ totalCount }}
          }}
          pageInfo {{ hasNextPage endCursor }}
        }}
      }}
      rateLimit {{ remaining resetAt }}
    }}
    """

    prs = []
    cursor = None
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            rate_check = requests.get(
                "https://api.github.com/rate_limit",
                headers=CONFIG["HEADERS"]
            ).json()

            remaining = rate_check["resources"]["graphql"]["remaining"]
            if remaining < 50:
                reset_time = rate_check["resources"]["graphql"]["reset"]
                wait_seconds = max(5, reset_time - time.time() + 10)
                print(f"⏳ Rate limit baixo ({remaining}). Esperando {wait_seconds:.0f}s...")
                time.sleep(wait_seconds)
                continue

            variables = {"after": cursor} if cursor else {}
            response = requests.post(
                CONFIG["GITHUB_API_URL"],
                json={"query": query_template, "variables": variables},
                headers=CONFIG["HEADERS"],
                timeout=60
            )

            if response.status_code == 502:
                attempts += 1
                wait_time = min(300, 10 * attempts)
                print(f"🔁 Bad Gateway (502). Tentativa {attempts}. Esperando {wait_time}s...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            data = response.json()

            if "errors" in data:
                error_msg = data["errors"][0]["message"]
                if "API rate limit" in error_msg:
                    reset_time = datetime.strptime(
                        data["data"]["rateLimit"]["resetAt"],
                        "%Y-%m-%dT%H:%M:%SZ"
                    ).timestamp()
                    wait_seconds = max(5, reset_time - time.time() + 10)
                    print(f"⏳ Rate limit excedido. Esperando {wait_seconds:.0f}s...")
                    time.sleep(wait_seconds)
                    continue
                raise ValueError(f"Erro GraphQL: {error_msg}")

            if not data.get("data"):
                raise ValueError("Resposta sem campo 'data'")

            pr_nodes = data["data"]["repository"]["pullRequests"]["nodes"]
            for pr in pr_nodes:
                try:
                    created = datetime.strptime(pr["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
                    merged = datetime.strptime(pr["mergedAt"], "%Y-%m-%dT%H:%M:%SZ") if pr.get("mergedAt") else None
                    closed = datetime.strptime(pr["closedAt"], "%Y-%m-%dT%H:%M:%SZ") if pr.get("closedAt") else None
                    time_diff = ((merged or closed) - created).total_seconds() / 3600

                    if (pr["reviews"]["totalCount"] >= CONFIG["MIN_REVIEWS"] and
                        time_diff >= CONFIG["MIN_HOURS"]):

                        prs.append({
                            "repo": f"{owner}/{name}",
                            "number": pr["number"],
                            "state": pr["state"],
                            "created_at": pr["createdAt"],
                            "merged_at": pr.get("mergedAt", ""),
                            "closed_at": pr.get("closedAt", ""),
                            "additions": pr["additions"],
                            "deletions": pr["deletions"],
                            "changed_files": pr["changedFiles"],
                            "description_length": len(pr.get("body", "") or ""),
                            "comments": pr["comments"]["totalCount"],
                            "reviews": pr["reviews"]["totalCount"],
                            "time_to_merge": time_diff if merged else None,
                            "time_to_close": time_diff if closed else None
                        })
                except Exception as e:
                    print(f"⚠️ PR {pr.get('number')} ignorado: {str(e)}")
                    continue

            page_info = data["data"]["repository"]["pullRequests"]["pageInfo"]
            if not page_info["hasNextPage"]:
                break

            cursor = page_info["endCursor"]
            attempts = 0
            time.sleep(1)

        except Exception as e:
            attempts += 1
            print(f"❌ Erro (tentativa {attempts}/{max_attempts}): {str(e)}")
            time.sleep(min(300, 10 * attempts))

    return prs