from fastapi import FastAPI
from app.api.usuario_router import router as usuario_router
from app.api.programa_academico_router import router as programa_router
from app.api.autenticacion_router import router as autenticacion_router
from app.api.rol_router import router as rol_router
from app.api.matricula_router import router as matricula_router
from app.api.estado_usuario_router import router as estado_usuario_router
from app.api.perfil_router import router as perfil_router
from app.api.requisitos_programa_router import router as requisitos_programa_router
from app.api.cursos_programa_router import router as cursos_programa_router
from app.api.grupos_cupos_router import router as grupos_cupos_router

app = FastAPI(
    title="Gestion Academica API",
    version="1.0.0",
    description="API desarrollada bajo arquitectura de capas"
)

app.include_router(usuario_router)
app.include_router(programa_router)
app.include_router(autenticacion_router)
app.include_router(rol_router)
app.include_router(matricula_router)
app.include_router(estado_usuario_router)
app.include_router(perfil_router)
app.include_router(requisitos_programa_router)
app.include_router(cursos_programa_router)
app.include_router(grupos_cupos_router)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": "development"
    }