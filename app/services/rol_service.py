from app.repositories.rol_repository import RolRepository

class RolService:
    def __init__(self, repository: RolRepository):
        self.repository = repository

    def asignar_rol(self, usuario_id: int, nuevo_rol: str, rol_solicitante: str) -> dict:
        # 1. Control de acceso: Verificar que el solicitante tenga rol 'admin'
        if rol_solicitante.lower() != "admin":
            raise PermissionError("Acceso denegado. Solo los usuarios con rol 'admin' pueden asignar roles.")

        # 2. Validar existencia del usuario a modificar
        if not self.repository.usuario_existe(usuario_id):
            raise KeyError("El usuario especificado no se encuentra registrado en el sistema.")

        # 3. Validar que el rol asignado sea válido en el catálogo
        if not self.repository.es_rol_valido(nuevo_rol):
            raise ValueError(f"El rol '{nuevo_rol}' no es un rol permitido en la plataforma.")

        # 4. Guardar cambio en la base de datos
        self.repository.actualizar_rol(usuario_id, nuevo_rol)

        return {
            "mensaje": "Rol asignado exitosamente al usuario.",
            "usuario_id": usuario_id,
            "nuevo_rol": nuevo_rol.lower()
        }