from pydantic import BaseModel, EmailStr
from typing import Optional

class ValidarIdentificacionRequest(BaseModel):
    tipo_documento: str
    numero_documento: str

class ValidarCorreoRequest(BaseModel):
    correo: EmailStr

class RegistrarUsuarioRequest(BaseModel):
    tipo_documento: str
    numero_documento: str
    nombres: str
    apellidos: str
    correo: EmailStr

class RespuestaBase(BaseModel):
    exito: bool
    mensaje: str
    datos: Optional[dict] = None