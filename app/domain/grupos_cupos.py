from typing import List, Optional
from pydantic import BaseModel

class GrupoCupoItem(BaseModel):
    grupo_id: int
    docente: str
    horario: str
    cupos_totales: int
    cupos_disponibles: int
    estado: str  # "ABIERTO" o "CERRADO"

class ConsultarGruposCuposResponse(BaseModel):
    mensaje: str
    data: Optional[dict] = None
    success: bool