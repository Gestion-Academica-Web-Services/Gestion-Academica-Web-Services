from app.domain.usuario import UsuarioCreate, UsuarioResponse
from app.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    # Inyección de dependencias: el servicio recibe el repositorio
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def crear_usuario(self, data: UsuarioCreate) -> UsuarioResponse:
        # Aquí irían las reglas de negocio (ej. validar si el email ya existe)
        return self.repo.crear(data)