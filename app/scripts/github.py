
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file located in ../../
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

username = "KR3915"
token = os.getenv("GITHUB_TOKEN")

def get_stars():
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    repos = requests.get(url, headers=headers).json()
    total_stars = sum(repo["stargazers_count"]for repo in repos)
    return total_stars

def get_github_followers():
    url = f"https://api.github.com/users/{username}" 
    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)

    # Pokud API vrátí chybu → vyhoď výjimku
    response.raise_for_status()

    data = response.json()
    return data.get("followers", 0)