from typing import Optional

class RolRepository:
    def __init__(self):
        self._roles_validos = ["admin", "estudiante", "docente", "coordinador"]
        self._db_usuarios = [
            {"id": 1, "nombre": "Johan Romero", "rol": "estudiante", "activo": True},
            {"id": 2, "nombre": "Carlos Perez", "rol": "docente", "activo": True},
            {"id": 3, "nombre": "Admin Sistema", "rol": "admin", "activo": True}
        ]

    def usuario_existe(self, usuario_id: int) -> bool:
        return any(u["id"] == usuario_id for u in self._db_usuarios)

    def es_rol_valido(self, rol: str) -> bool:
        return rol.lower() in self._roles_validos

    def actualizar_rol(self, usuario_id: int, nuevo_rol: str) -> bool:
        for u in self._db_usuarios:
            if u["id"] == usuario_id:
                u["rol"] = nuevo_rol.lower()
                return True
        return False