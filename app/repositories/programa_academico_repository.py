from typing import Optional

class ProgramaAcademicoRepository:
    def __init__(self):
        self._db_programas = [
            {
                "id": 1,
                "codigo": "PA-ITS-01",
                "nombre": "Tecnología en Desarrollo de Sistemas Informáticos",
                "nivel_formacion": "Tecnológico",
                "titulo_otorgado": "Tecnólogo en Desarrollo de Sistemas Informáticos",
                "total_creditos": 96,
                "duracion_semestres": 6,
                "vigencia": "Vigente",
                "activo": True
            },
            {
                "id": 2,
                "codigo": "PA-ING-02",
                "nombre": "Ingeniería de Software",
                "nivel_formacion": "Profesional",
                "titulo_otorgado": "Ingeniero de Software",
                "total_creditos": 160,
                "duracion_semestres": 10,
                "vigencia": "Vigente",
                "activo": True
            }
        ]

    def obtener_por_id(self, programa_id: int) -> Optional[dict]:
        for programa in self._db_programas:
            if programa["id"] == programa_id:
                return programa
        return None