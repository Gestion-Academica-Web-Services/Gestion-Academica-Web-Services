from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.perfil import ActualizarPerfilRequest, ActualizarPerfilResponse
from app.services.perfil_service import PerfilService
from app.repositories.perfil_repository import PerfilRepository

router = APIRouter(prefix="/api/v1/usuarios", tags=["Gestión de Usuarios y Roles"])

repo = PerfilRepository()
service = PerfilService(repo)

@router.put("/perfil", response_model=ActualizarPerfilResponse, status_code=status.HTTP_200_OK)
def actualizar_perfil(datos: ActualizarPerfilRequest):
    try:
        resultado = service.actualizar_perfil(
            usuario_id=datos.usuario_id,
            datos=datos.model_dump(exclude_unset=True)
        )
        return resultado
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "mensaje": str(e).strip("'"),
                "data": None,
                "success": False
            }
        )