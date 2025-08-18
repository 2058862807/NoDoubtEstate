import os
import requests
from dotenv import load_dotenv

load_dotenv()

def github_commit_push(repo_path, message, remote="origin", branch="main"):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return False, "GitHub token not found in .env"
    
    try:
        headers = {"Authorization": f"token {token}"}
        response = requests.get("https://api.github.com/user", headers=headers)
        
        if response.status_code == 200:
            user = response.json()
            return True, f"GitHub connected as {user.get('login')} - Ready to push: {message}"
        else:
            return False, f"GitHub API error: {response.status_code}"
    except Exception as e:
        return False, f"GitHub error: {str(e)}"