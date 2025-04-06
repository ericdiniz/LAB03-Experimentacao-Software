import requests
from datetime import datetime
from config import CONFIG

def get_repository_prs(owner, name):
    query = """
    query ($after: String) {
      repository(owner: "%s", name: "%s") {
        pullRequests(
          states: [CLOSED, MERGED]
          first: 100
          after: $after
        ) {
          nodes {
            number
            state
            createdAt
            mergedAt
            closedAt
            additions
            deletions
            changedFiles
            body
            comments { totalCount }
            reviews { totalCount }
          }
          pageInfo { hasNextPage endCursor }
        }
      }
    }
    """ % (owner, name)

    prs = []
    after = None
    has_next = True

    while has_next:
        try:
            response = requests.post(
                CONFIG["GITHUB_API_URL"],
                json={"query": query, "variables": {"after": after}},
                headers=CONFIG["HEADERS"],
                timeout=CONFIG["TIMEOUT"]
            )
            response.raise_for_status()
            data = response.json()
            pr_data = data["data"]["repository"]["pullRequests"]

            for pr in pr_data["nodes"]:
                try:
                    created = datetime.fromisoformat(pr["createdAt"].replace("Z", ""))
                    merged = datetime.fromisoformat(pr["mergedAt"].replace("Z", "")) if pr.get("mergedAt") else None
                    closed = datetime.fromisoformat(pr["closedAt"].replace("Z", "")) if pr.get("closedAt") else None
                    time_diff = ((merged or closed) - created).total_seconds()/3600

                    if pr["reviews"]["totalCount"] >= CONFIG["MIN_REVIEWS"] and time_diff >= CONFIG["MIN_HOURS"]:
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
                            "description_length": len(pr.get("body", "")) if pr.get("body") else 0,
                            "comments": pr["comments"]["totalCount"],
                            "reviews": pr["reviews"]["totalCount"],
                            "time_to_merge": time_diff if merged else None,
                            "time_to_close": time_diff if closed else None
                        })

                except Exception:
                    continue

            has_next = pr_data["pageInfo"]["hasNextPage"]
            after = pr_data["pageInfo"]["endCursor"]
            time.sleep(CONFIG["REQUEST_DELAY"])

        except Exception:
            break

    return prs