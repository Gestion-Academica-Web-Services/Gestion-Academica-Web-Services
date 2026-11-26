from typing import Optional
from pydantic import BaseModel

class AsignarRolRequest(BaseModel):
    usuario_id: int
    rol: str

class DetalleRolData(BaseModel):
    usuario_id: int
    rol: str

class AsignarRolResponse(BaseModel):
    mensaje: str
    data: Optional[DetalleRolData] = None
    success: bool