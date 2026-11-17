from fastapi import FastAPI
from app.api.usuario_router import router as usuario_router
from app.api.programa_academico_router import router as programa_router
from app.api.autenticacion_router import router as autenticacion_router
from app.api.rol_router import router as rol_router

app = FastAPI(
    title="Gestion Academica API",
    version="1.0.0",
    description="API desarrollada bajo arquitectura de capas"
)

app.include_router(usuario_router)
app.include_router(programa_router)
app.include_router(autenticacion_router)
app.include_router(rol_router)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development"
    }