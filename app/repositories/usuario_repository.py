from app.domain.usuario import UsuarioCreate, UsuarioResponse

class UsuarioRepository:
    def __init__(self):
        # Base de datos simulada en memoria
        self._db: dict[int, dict] = {}
        self._next_id: int = 1

    def crear(self, data: UsuarioCreate) -> UsuarioResponse:
        # Convertimos el modelo Pydantic a diccionario
        nuevo_usuario = data.model_dump()
        nuevo_usuario["id"] = self._next_id
        
        # Guardamos en nuestra "base de datos"
        self._db[self._next_id] = nuevo_usuario
        self._next_id += 1
        
        return UsuarioResponse(**nuevo_usuario)