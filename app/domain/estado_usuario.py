from typing import Optional
from pydantic import BaseModel

class CambiarEstadoRequest(BaseModel):
    usuario_id: int
    estado: str

class DetalleEstadoData(BaseModel):
    usuario_id: int
    nuevo_estado: str

class CambiarEstadoResponse(BaseModel):
    mensaje: str
    data: Optional[DetalleEstadoData] = None
    success: bool