
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file located in ../../
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

username = "KR3915"
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {token}"}
url = f"https://api.github.com/users/{username}/repos?per_page=100"
repos = requests.get(url, headers=headers).json()

total_stars = sum(repo["stargazers_count"]for repo in repos)
print("Total stars:", total_stars)
