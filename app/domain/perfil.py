from typing import Optional
from pydantic import BaseModel, EmailStr

class ActualizarPerfilRequest(BaseModel):
    usuario_id: int
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None

class DetallePerfilData(BaseModel):
    usuario_id: int
    nombre: str
    email: str
    telefono: str

class ActualizarPerfilResponse(BaseModel):
    mensaje: str
    data: Optional[DetallePerfilData] = None
    success: bool