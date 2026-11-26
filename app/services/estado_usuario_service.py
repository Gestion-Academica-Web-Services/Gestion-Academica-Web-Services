from app.repositories.estado_usuario_repository import EstadoUsuarioRepository

class EstadoUsuarioService:
    def __init__(self, repository: EstadoUsuarioRepository):
        self.repository = repository

    def cambiar_estado(self, usuario_id: int, nuevo_estado: str, rol_solicitante: str) -> dict:
        # 1. Control de acceso: requiere rol 'admin'
        if rol_solicitante.lower() != "admin":
            raise PermissionError("Acceso denegado. Se requiere autenticación con rol de 'admin'.")

        # 2. Validar existencia del usuario
        if not self.repository.usuario_existe(usuario_id):
            raise KeyError("El usuario especificado no existe.")

        # 3. Validar que el estado ingresado sea uno de los permitidos
        if not self.repository.es_estado_valido(nuevo_estado):
            raise ValueError(f"El estado '{nuevo_estado}' no es válido. Los estados permitidos son: activo, inactivo, suspendido.")

        # 4. Actualizar en base de datos
        self.repository.actualizar_estado(usuario_id, nuevo_estado)

        return {
            "mensaje": "Estado de la cuenta actualizado correctamente",
            "data": {
                "usuario_id": usuario_id,
                "nuevo_estado": nuevo_estado.lower()
            },
            "success": True
        }