from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.matricula import VerificarCupoResponse
from app.services.matricula_service import MatriculaService
from app.repositories.matricula_repository import MatriculaRepository

router = APIRouter(prefix="/api/matriculas", tags=["Gestión de Matrículas"])

repo = MatriculaRepository()
service = MatriculaService(repo)

@router.get("/verificar-cupo/{grupoId}", response_model=VerificarCupoResponse, status_code=status.HTTP_200_OK)
def verificar_cupo(grupoId: int):
    try:
        return service.verificar_cupo(grupoId)
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"mensaje": str(e).strip("'")}
        )