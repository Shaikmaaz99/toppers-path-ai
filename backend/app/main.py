from fastapi import FastAPI

app = FastAPI(
    title="Toppers Path AI",
    description="AI-powered student assistant for Toppers Path Academy",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Toppers Path AI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Toppers Path AI"
    }
