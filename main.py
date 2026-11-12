from fastapi import FastAPI

app = FastAPI(
    title="Gestion Academica API",
    version="1.0.0",
    description="API desarrollada bajo arquitectura de capas"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development"
    }
