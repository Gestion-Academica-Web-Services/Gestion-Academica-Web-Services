from pydantic import BaseModel

# Datos base que siempre tendrá un usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: str
    rol: str

# Datos requeridos para CREAR el usuario (incluye contraseña)
class UsuarioCreate(UsuarioBase):
    password: str

# Datos que la API RESPONDE (excluye contraseña por seguridad)
class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True