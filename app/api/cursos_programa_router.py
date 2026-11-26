from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.cursos_programa import ConsultarCursosProgramaResponse
from app.services.cursos_programa_service import CursosProgramaService
from app.repositories.cursos_programa_repository import CursosProgramaRepository

router = APIRouter(prefix="/api/v1/programas", tags=["Gestión de Cursos y Asignaturas"])

repo = CursosProgramaRepository()
service = CursosProgramaService(repo)

@router.get("/{programaId}/cursos", response_model=ConsultarCursosProgramaResponse, status_code=status.HTTP_200_OK)
def consultar_cursos_programa(programaId: int):
    try:
        return service.consultar_cursos(programaId)
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "mensaje": str(e).strip("'"),
                "data": None,
                "success": False
            }
        )