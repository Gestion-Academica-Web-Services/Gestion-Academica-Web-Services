from typing import List, Optional
from pydantic import BaseModel

class RequisitoItem(BaseModel):
    codigo_asignatura: str
    nombre_asignatura: str
    tipo_requisito: str  # "Prerrequisito" o "Corequisito"
    creditos: int

class ConsultarRequisitosResponse(BaseModel):
    mensaje: str
    data: Optional[dict] = None
    success: bool