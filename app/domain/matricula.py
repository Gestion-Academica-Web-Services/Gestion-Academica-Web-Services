from pydantic import BaseModel

class VerificarCupoResponse(BaseModel):
    grupo_id: int
    cupo_disponible: bool
    cupos_restantes: int
    cupos_ocupados: int
    capacidad_maxima: int
    estado_grupo: str  # "ABIERTO" o "CERRADO"