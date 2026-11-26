from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.requisitos_programa import ConsultarRequisitosResponse
from app.services.requisitos_programa_service import RequisitosProgramaService
from app.repositories.requisitos_programa_repository import RequisitosProgramaRepository

router = APIRouter(prefix="/api/v1/programas", tags=["Gestión de Programas Académicos"])

repo = RequisitosProgramaRepository()
service = RequisitosProgramaService(repo)

@router.get("/{programaId}/requisitos", response_model=ConsultarRequisitosResponse, status_code=status.HTTP_200_OK)
def consultar_requisitos(programaId: int):
    try:
        return service.consultar_requisitos(programaId)
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "mensaje": str(e).strip("'"),
                "data": None,
                "success": False
            }
        )