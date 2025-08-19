from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "DREAM 1.0 is alive!"}

@app.get("/health") 
def health():
    return {"status": "ok", "system": "DREAM"}
