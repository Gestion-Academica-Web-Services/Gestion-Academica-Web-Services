from fastapi import FastAPI
from app.api.usuario_router import router as usuario_router

app = FastAPI(
    title="API Gestión Académica",
    description="Backend con Arquitectura de Capas",
    version="1.0.0"
)

# Conectamos las rutas de usuarios a la aplicación principal
app.include_router(usuario_router)

@app.get("/", tags=["Root"])
def root():
    return {"mensaje": "API de Gestión Académica funcionando correctamente"}