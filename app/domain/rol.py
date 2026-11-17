from pydantic import BaseModel

class AsignarRolRequest(BaseModel):
    usuario_id: int
    rol: str

class AsignarRolResponse(BaseModel):
    mensaje: str
    usuario_id: int
    nuevo_rol: str