from typing import Optional

class EstadoUsuarioRepository:
    def __init__(self):
        # Estados permitidos según criterios de aceptación
        self._estados_permitidos = ["activo", "inactivo", "suspendido"]
        self._db_usuarios = [
            {"id": 1, "nombre": "Johan Romero", "estado": "activo"},
            {"id": 2, "nombre": "Carlos Perez", "estado": "activo"},
            {"id": 3, "nombre": "Usuario Inactivo", "estado": "inactivo"}
        ]

    def usuario_existe(self, usuario_id: int) -> bool:
        return any(u["id"] == usuario_id for u in self._db_usuarios)

    def es_estado_valido(self, estado: str) -> bool:
        return estado.lower() in self._estados_permitidos

    def actualizar_estado(self, usuario_id: int, nuevo_estado: str) -> bool:
        for u in self._db_usuarios:
            if u["id"] == usuario_id:
                u["estado"] = nuevo_estado.lower()
                return True
        return False