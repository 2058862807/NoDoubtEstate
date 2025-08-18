import os
import requests
from dotenv import load_dotenv

load_dotenv()

def vercel_deploy(project_dir, prod=True):
    token = os.getenv("VERCEL_TOKEN")
    if not token:
        return False, "Vercel token not found in .env"
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://api.vercel.com/v2/user", headers=headers)
        
        if response.status_code == 200:
            deployment_type = "production" if prod else "preview"
            return True, f"Vercel ready for {deployment_type} deployment of {project_dir}"
        else:
            return False, f"Vercel API error: {response.status_code}"
    except Exception as e:
        return False, f"Vercel error: {str(e)}"