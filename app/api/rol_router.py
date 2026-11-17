from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
from app.domain.rol import AsignarRolRequest, AsignarRolResponse
from app.services.rol_service import RolService
from app.repositories.rol_repository import RolRepository

router = APIRouter(prefix="/api/v1/usuarios", tags=["Gestión de Usuarios y Roles"])

repo = RolRepository()
service = RolService(repo)

@router.post("/roles", response_model=AsignarRolResponse, status_code=status.HTTP_200_OK)
def asignar_rol(
    datos: AsignarRolRequest,
    x_rol_solicitante: str = Header(default="admin", alias="X-Rol-Solicitante", description="Rol del usuario que realiza la petición (ej. admin)")
):
    try:
        resultado = service.asignar_rol(datos.usuario_id, datos.rol, x_rol_solicitante)
        return resultado
    except PermissionError as e:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"mensaje": str(e)}
        )
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"mensaje": str(e).strip("'")}
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"mensaje": str(e)}
        )