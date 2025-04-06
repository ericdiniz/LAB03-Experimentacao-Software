import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "GITHUB_API_URL": "https://api.github.com/graphql",
    "HEADERS": {
        "Authorization": f"bearer {os.getenv('GITHUB_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    },
    "REQUEST_DELAY": 3,
    "MAX_REPOS": 200,
    "MIN_PRS": 100,
    "MIN_REVIEWS": 1,
    "MIN_HOURS": 1,
    "TIMEOUT": 30,
    "MAX_RETRIES": 5,
    "RETRY_DELAY": 5
}