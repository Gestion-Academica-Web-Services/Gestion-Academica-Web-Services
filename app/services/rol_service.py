from app.repositories.rol_repository import RolRepository

class RolService:
    def __init__(self, repository: RolRepository):
        self.repository = repository

    def asignar_rol(self, usuario_id: int, nuevo_rol: str, rol_solicitante: str) -> dict:
        # 1. Control de acceso por rol admin
        if rol_solicitante.lower() != "admin":
            raise PermissionError("Acceso denegado. Solo los usuarios con rol 'admin' pueden asignar roles.")

        # 2. Validar existencia del usuario
        if not self.repository.usuario_existe(usuario_id):
            raise KeyError("El usuario especificado no existe")

        # 3. Validar si el rol existe en el catálogo
        if not self.repository.es_rol_valido(nuevo_rol):
            raise ValueError("El rol especificado no existe")

        # 4. Actualizar rol en repositorio
        self.repository.actualizar_rol(usuario_id, nuevo_rol)

        return {
            "mensaje": "Rol asignado correctamente",
            "data": {
                "usuario_id": usuario_id,
                "rol": nuevo_rol.lower()
            },
            "success": True
        }