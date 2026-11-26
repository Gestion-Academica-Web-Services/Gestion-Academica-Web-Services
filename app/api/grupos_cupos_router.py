from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.grupos_cupos import ConsultarGruposCuposResponse
from app.services.grupos_cupos_service import GruposCuposService
from app.repositories.grupos_cupos_repository import GruposCuposRepository

router = APIRouter(prefix="/api/v1/cursos", tags=["Gestión de Cursos y Asignaturas"])

repo = GruposCuposRepository()
service = GruposCuposService(repo)

@router.get("/{codigoCurso}/grupos", response_model=ConsultarGruposCuposResponse, status_code=status.HTTP_200_OK)
def consultar_grupos_curso(codigoCurso: str):
    try:
        return service.consultar_grupos(codigoCurso)
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "mensaje": str(e).strip("'"),
                "data": None,
                "success": False
            }
        )