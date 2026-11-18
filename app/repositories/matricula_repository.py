from typing import Optional

class MatriculaRepository:
    def __init__(self):
        # Base de datos simulada de grupos académicos
        self._db_grupos = [
            {"grupo_id": 101, "capacidad_maxima": 30, "cupos_ocupados": 25, "activo": True}, # ABIERTO (5 disponibles)
            {"grupo_id": 102, "capacidad_maxima": 20, "cupos_ocupados": 20, "activo": True}, # CERRADO (0 disponibles)
            {"grupo_id": 103, "capacidad_maxima": 15, "cupos_ocupados": 10, "activo": True}  # ABIERTO (5 disponibles)
        ]

    def obtener_grupo(self, grupo_id: int) -> Optional[dict]:
        for grupo in self._db_grupos:
            if grupo["grupo_id"] == grupo_id:
                return grupo
        return None