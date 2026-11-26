from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.domain.autenticacion import LoginRequest, TokenResponse
from app.services.autenticacion_service import AutenticacionService
from app.repositories.autenticacion_repository import AutenticacionRepository

router = APIRouter(prefix="/api/autenticacion", tags=["Gestión de Autenticación"])

repo = AutenticacionRepository()
service = AutenticacionService(repo)

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(credenciales: LoginRequest):
    try:
        resultado = service.autenticar_usuario(credenciales.correo, credenciales.password)
        return resultado
    except KeyError as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"mensaje": str(e).strip("'")}
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"mensaje": str(e)}
        )