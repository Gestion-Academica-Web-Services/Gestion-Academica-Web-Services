from typing import Optional

class RequisitosProgramaRepository:
    def __init__(self):
        self._db_requisitos = {
            1: {
                "programa_id": 1,
                "nombre_programa": "Ingeniería de Sistemas / Computación",
                "requisitos": [
                    {"codigo_asignatura": "MAT101", "nombre_asignatura": "Cálculo I", "tipo_requisito": "Prerrequisito", "creditos": 4},
                    {"codigo_asignatura": "PRG101", "nombre_asignatura": "Programación Orientada a Objetos", "tipo_requisito": "Prerrequisito", "creditos": 3}
                ]
            },
            2: {
                "programa_id": 2,
                "nombre_programa": "Redes y Servicios Web",
                "requisitos": [
                    {"codigo_asignatura": "RED101", "nombre_asignatura": "Fundamentos de Redes IPv4/IPv6", "tipo_requisito": "Prerrequisito", "creditos": 3},
                    {"codigo_asignatura": "WEB101", "nombre_asignatura": "Servicios Web y Arquitectura REST", "tipo_requisito": "Corequisito", "creditos": 3}
                ]
            }
        }

    def obtener_requisitos(self, programa_id: int) -> Optional[dict]:
        return self._db_requisitos.get(programa_id)