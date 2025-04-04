import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

CONFIG = {
    "GITHUB_API_URL": "https://api.github.com",
    "HEADERS": {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    },
    "REQUEST_DELAY": int(os.getenv('REQUEST_DELAY', 1)),
    "MAX_REPOS": int(os.getenv('MAX_REPOS', 200)),
    "MIN_PRS": int(os.getenv('MIN_PRS', 100)),
    "MIN_REVIEWS": int(os.getenv('MIN_REVIEWS', 1)),
    "MIN_HOURS": int(os.getenv('MIN_HOURS', 1))
}