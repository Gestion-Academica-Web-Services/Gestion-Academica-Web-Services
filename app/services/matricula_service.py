from app.repositories.matricula_repository import MatriculaRepository

class MatriculaService:
    def __init__(self, repository: MatriculaRepository):
        self.repository = repository

    def verificar_cupo(self, grupo_id: int) -> dict:
        grupo = self.repository.obtener_grupo(grupo_id)
        if not grupo:
            raise KeyError("El grupo académico especificado no se encuentra registrado en el sistema.")

        cupos_restantes = grupo["capacidad_maxima"] - grupo["cupos_ocupados"]
        cupo_disponible = cupos_restantes > 0
        estado_grupo = "ABIERTO" if cupo_disponible else "CERRADO"

        return {
            "grupo_id": grupo["grupo_id"],
            "cupo_disponible": cupo_disponible,
            "cupos_restantes": max(0, cupos_restantes),
            "cupos_ocupados": grupo["cupos_ocupados"],
            "capacidad_maxima": grupo["capacidad_maxima"],
            "estado_grupo": estado_grupo
        }