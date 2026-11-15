from fastapi import APIRouter, HTTPException, status
from app.domain.programa_academico import ProgramaAcademicoResponse
from app.services.programa_academico_service import ProgramaAcademicoService
from app.repositories.programa_academico_repository import ProgramaAcademicoRepository

router = APIRouter(prefix="/api/programas-academicos", tags=["Gestión Académica"])

repo = ProgramaAcademicoRepository()
service = ProgramaAcademicoService(repo)

@router.get("/{programaId}", response_model=ProgramaAcademicoResponse, status_code=status.HTTP_200_OK)
def consultar_programa(programaId: int):
    try:
        return service.consultar_programa(programaId)
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e).strip("'")
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )