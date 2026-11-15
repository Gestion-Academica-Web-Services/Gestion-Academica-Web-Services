from fastapi import APIRouter, HTTPException, status
from app.domain.usuario import ValidarIdentificacionRequest, ValidarCorreoRequest, RegistrarUsuarioRequest, RespuestaBase
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository

router = APIRouter(prefix="/api/usuarios", tags=["Gestión de Usuarios"])

repo = UsuarioRepository()
service = UsuarioService(repo)

@router.post("/validar-identificacion", response_model=RespuestaBase)
def validar_identificacion(data: ValidarIdentificacionRequest):
    resultado = service.validar_identificacion(data)
    return RespuestaBase(
        exito=resultado["valido"],
        mensaje=resultado["mensaje"]
    )

@router.post("/validar-correo", response_model=RespuestaBase)
def validar_correo(data: ValidarCorreoRequest):
    resultado = service.validar_correo(data)
    return RespuestaBase(
        exito=resultado["valido"],
        mensaje=resultado["mensaje"]
    )

@router.post("/registrar", status_code=status.HTTP_201_CREATED, response_model=RespuestaBase)
def registrar_usuario(data: RegistrarUsuarioRequest):
    try:
        usuario_creado = service.registrar_usuario(data)
        return RespuestaBase(
            exito=True,
            mensaje="Usuario registrado exitosamente.",
            datos=usuario_creado
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )