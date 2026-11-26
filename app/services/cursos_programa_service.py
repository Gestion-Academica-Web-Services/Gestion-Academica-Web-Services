from app.repositories.cursos_programa_repository import CursosProgramaRepository

class CursosProgramaService:
    def __init__(self, repository: CursosProgramaRepository):
        self.repository = repository

    def consultar_cursos(self, programa_id: int) -> dict:
        datos = self.repository.obtener_cursos_por_programa(programa_id)
        if not datos:
            raise KeyError("El programa académico especificado no existe o no tiene cursos asignados.")

        return {
            "mensaje": "Cursos del programa académico consultados correctamente",
            "data": datos,
            "success": True
        }