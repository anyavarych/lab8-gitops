from fastapi import FastAPI

app = FastAPI(title="Courses API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Courses API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/instance")
def instance():
    return {"service": "courses-api", "version": "1.0.0"}