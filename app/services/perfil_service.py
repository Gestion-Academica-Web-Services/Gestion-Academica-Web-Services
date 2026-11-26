from app.repositories.perfil_repository import PerfilRepository

class PerfilService:
    def __init__(self, repository: PerfilRepository):
        self.repository = repository

    def actualizar_perfil(self, usuario_id: int, datos: dict) -> dict:
        usuario = self.repository.obtener_por_id(usuario_id)
        if not usuario:
            raise KeyError("El usuario especificado no existe en el sistema.")

        usuario_actualizado = self.repository.actualizar_perfil(usuario_id, datos)

        return {
            "mensaje": "Perfil actualizado exitosamente",
            "data": {
                "usuario_id": usuario_actualizado["id"],
                "nombre": usuario_actualizado["nombre"],
                "email": usuario_actualizado["email"],
                "telefono": usuario_actualizado["telefono"]
            },
            "success": True
        }