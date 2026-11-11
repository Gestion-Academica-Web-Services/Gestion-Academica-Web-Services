from fastapi import APIRouter, status
from app.domain.usuario import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository

# Instanciamos las capas
repo = UsuarioRepository()
service = UsuarioService(repo)

# Creamos el router
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(data: UsuarioCreate):
    """Crea un nuevo usuario en el sistema"""
    return service.crear_usuario(data)