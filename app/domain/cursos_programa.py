from typing import List, Optional
from pydantic import BaseModel

class CursoItem(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    semestre: int

class ConsultarCursosProgramaResponse(BaseModel):
    mensaje: str
    data: Optional[dict] = None
    success: bool