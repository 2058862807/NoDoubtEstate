import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="DREAM 2.0 Assistant", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "status": "ok", 
        "system": "DREAM 2.0",
        "message": "Recursive AGI is online!"
    }

@app.get("/")
def root():
    return {"message": "NoDoubtEstate DREAM 2.0 Backend - AGI Powered"}

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=PORT)
