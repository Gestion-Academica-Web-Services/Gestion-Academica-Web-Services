from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
from app.domain.estado_usuario import CambiarEstadoRequest, CambiarEstadoResponse
from app.services.estado_usuario_service import EstadoUsuarioService
from app.repositories.estado_usuario_repository import EstadoUsuarioRepository

router = APIRouter(prefix="/api/v1/usuarios", tags=["Gestión de Estado de Cuentas"])

repo = EstadoUsuarioRepository()
service = EstadoUsuarioService(repo)

@router.patch("/estado", response_model=CambiarEstadoResponse, status_code=status.HTTP_200_OK)
def cambiar_estado(
    datos: CambiarEstadoRequest,
    x_rol_solicitante: str = Header(default="admin", alias="X-Rol-Solicitante", description="Rol del usuario solicitante (ej. admin)")
):
    try:
        return service.cambiar_estado(datos.usuario_id, datos.estado, x_rol_solicitante)
    except PermissionError as e:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "mensaje": str(e),
                "data": None,
                "success": False
            }
        )
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "mensaje": str(e).strip("'"),
                "data": None,
                "success": False
            }
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "mensaje": str(e),
                "data": None,
                "success": False
            }
        )