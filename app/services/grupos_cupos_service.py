from app.repositories.grupos_cupos_repository import GruposCuposRepository

class GruposCuposService:
    def __init__(self, repository: GruposCuposRepository):
        self.repository = repository

    def consultar_grupos(self, codigo_curso: str) -> dict:
        datos = self.repository.obtener_grupos_por_curso(codigo_curso)
        if not datos:
            raise KeyError(f"El curso '{codigo_curso}' no existe o no tiene grupos asignados.")

        return {
            "mensaje": "Grupos y cupos del curso consultados correctamente",
            "data": datos,
            "success": True
        }