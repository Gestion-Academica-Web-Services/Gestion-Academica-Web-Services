from app.repositories.requisitos_programa_repository import RequisitosProgramaRepository

class RequisitosProgramaService:
    def __init__(self, repository: RequisitosProgramaRepository):
        self.repository = repository

    def consultar_requisitos(self, programa_id: int) -> dict:
        info = self.repository.obtener_requisitos(programa_id)
        if not info:
            raise KeyError("El programa académico especificado no existe o no tiene requisitos registrados.")

        return {
            "mensaje": "Requisitos del programa académico consultados correctamente",
            "data": info,
            "success": True
        }