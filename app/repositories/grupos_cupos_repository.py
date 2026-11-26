from typing import Optional

class GruposCuposRepository:
    def __init__(self):
        self._db_grupos = {
            "PRG201": {
                "codigo_curso": "PRG201",
                "nombre_curso": "Programación Web Avanzada",
                "grupos": [
                    {"grupo_id": 1, "docente": "Ing. Carlos Mendoza", "horario": "Lun-Mie 08:00-10:00", "cupos_totales": 30, "cupos_disponibles": 5, "estado": "ABIERTO"},
                    {"grupo_id": 2, "docente": "Ing. Maria Gomez", "horario": "Mar-Jue 14:00-16:00", "cupos_totales": 25, "cupos_disponibles": 0, "estado": "CERRADO"}
                ]
            },
            "RED201": {
                "codigo_curso": "RED201",
                "nombre_curso": "Redes y Servicios Web",
                "grupos": [
                    {"grupo_id": 1, "docente": "Ing. Johan Romero", "horario": "Vie 07:00-11:00", "cupos_totales": 20, "cupos_disponibles": 3, "estado": "ABIERTO"}
                ]
            }
        }

    def obtener_grupos_por_curso(self, codigo_curso: str) -> Optional[dict]:
        return self._db_grupos.get(codigo_curso.upper())