from fastapi import FastAPI
from app.api.usuario_router import router as usuario_router

app = FastAPI(
    title="Gestion Academica API",
    version="1.0.0",
    description="API desarrollada bajo arquitectura de capas"
)

app.include_router(usuario_router)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development"
    }