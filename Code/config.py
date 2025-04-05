import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

CONFIG = {
    "GITHUB_API_URL": "https://api.github.com/graphql",
    "HEADERS": {
        "Authorization": f"bearer {os.getenv('GITHUB_TOKEN')}",
        "Content-Type": "application/json"
    },
    "REQUEST_DELAY": 2,
    "MAX_REPOS": 200,
    "MIN_PRS": 100,
    "MIN_REVIEWS": 1,
    "MIN_HOURS": 1,
    "TIMEOUT": 30
}