from app.repositories.programa_academico_repository import ProgramaAcademicoRepository

class ProgramaAcademicoService:
    def __init__(self, repository: ProgramaAcademicoRepository):
        self.repository = repository

    def consultar_programa(self, programa_id: int) -> dict:
        programa = self.repository.obtener_por_id(programa_id)
        if not programa:
            raise KeyError("El programa académico solicitado no se encuentra registrado en el sistema.")
        if not programa.get("activo", True):
            raise ValueError("El programa académico seleccionado no se encuentra activo en el catálogo.")
        return programa