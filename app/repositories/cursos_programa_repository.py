from typing import Optional

class CursosProgramaRepository:
    def __init__(self):
        self._db_cursos = {
            1: {
                "programa_id": 1,
                "nombre_programa": "Ingeniería de Sistemas / Computación",
                "cursos": [
                    {"codigo": "PRG201", "nombre": "Programación Web Avanzada", "creditos": 3, "semestre": 4},
                    {"codigo": "RED201", "nombre": "Redes y Servicios Web", "creditos": 4, "semestre": 4},
                    {"codigo": "BDD201", "nombre": "Motores de Bases de Datos", "creditos": 3, "semestre": 4}
                ]
            },
            2: {
                "programa_id": 2,
                "nombre_programa": "Redes de Computadores",
                "cursos": [
                    {"codigo": "RED101", "nombre": "Enrutamiento OSPF y VLANs", "creditos": 4, "semestre": 3},
                    {"codigo": "SEG101", "nombre": "Seguridad en Redes y ACLs", "creditos": 3, "semestre": 4}
                ]
            }
        }

    def obtener_cursos_por_programa(self, programa_id: int) -> Optional[dict]:
        return self._db_cursos.get(programa_id)