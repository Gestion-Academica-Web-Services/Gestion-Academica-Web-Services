from typing import Optional

class PerfilRepository:
    def __init__(self):
        self._db_usuarios = [
            {"id": 1, "nombre": "Johan Romero", "email": "johan@ejemplo.com", "telefono": "3001234567"},
            {"id": 2, "nombre": "Carlos Perez", "email": "carlos@ejemplo.com", "telefono": "3109876543"}
        ]

    def obtener_por_id(self, usuario_id: int) -> Optional[dict]:
        for u in self._db_usuarios:
            if u["id"] == usuario_id:
                return u
        return None

    def actualizar_perfil(self, usuario_id: int, datos_nuevos: dict) -> Optional[dict]:
        for u in self._db_usuarios:
            if u["id"] == usuario_id:
                if datos_nuevos.get("nombre"):
                    u["nombre"] = datos_nuevos["nombre"]
                if datos_nuevos.get("email"):
                    u["email"] = datos_nuevos["email"]
                if datos_nuevos.get("telefono"):
                    u["telefono"] = datos_nuevos["telefono"]
                return u
        return None