from datetime import datetime, timedelta
from app.repositories.autenticacion_repository import AutenticacionRepository

class AutenticacionService:
    def __init__(self, repository: AutenticacionRepository):
        self.repository = repository

    def autenticar_usuario(self, correo: str, password_recibido: str) -> dict:
        usuario = self.repository.buscar_por_correo(correo)
        
        # 1. Validar si el usuario existe
        if not usuario:
            raise KeyError("Las credenciales ingresadas son incorrectas o el usuario no existe.")
        
        # 2. Validar si la cuenta está ACTIVA
        if not usuario.get("activo", False):
            raise ValueError("La cuenta de usuario se encuentra inactiva. Contacte al administrador.")
        
        # 3. Validar coincidencia de la contraseña
        if usuario["password_plano"] != password_recibido:
            raise KeyError("Las credenciales ingresadas son incorrectas.")
        
        # 4. Generar token estructurado con ID, Rol y Expiración (24 horas)
        fecha_expiracion = (datetime.now() + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        token_simulado = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.user_{usuario['id']}_{usuario['rol']}"
        
        return {
            "access_token": token_simulado,
            "token_type": "bearer",
            "usuario_id": usuario["id"],
            "rol": usuario["rol"],
            "expiracion": fecha_expiracion
        }