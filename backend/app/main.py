from fastapi import FastAPI

from backend.app.api.tutor import router as tutor_router

app = FastAPI(
    title="Toppers Path AI",
    description="AI-powered student assistant for Toppers Path Academy",
    version="0.1.0"
)

app.include_router(tutor_router)


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
