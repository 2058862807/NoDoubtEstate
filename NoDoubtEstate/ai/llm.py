import os
import requests
from dotenv import load_dotenv

load_dotenv()

def llm_complete(provider="openai", model="gpt-4o-mini", prompt=""):
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "OpenAI API key not found in .env"
        
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1000
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"OpenAI API error: {response.status_code}"
                
        except Exception as e:
            return f"OpenAI error: {str(e)}"
    
    elif provider == "deepseek":
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            return "DeepSeek API key not found"
        
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1000
            }
            
            response = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"DeepSeek API error: {response.status_code}"
                
        except Exception as e:
            return f"DeepSeek error: {str(e)}"
    
    return f"Provider {provider} not supported. Use 'openai' or 'deepseek'"