from app.repositories.usuario_repository import UsuarioRepository
from app.domain.usuario import ValidarIdentificacionRequest, ValidarCorreoRequest, RegistrarUsuarioRequest

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def validar_identificacion(self, data: ValidarIdentificacionRequest) -> dict:
        if self.repository.existe_por_identificacion(data.tipo_documento, data.numero_documento):
            return {"valido": False, "mensaje": "El tipo y número de documento ya se encuentran registrados."}
        return {"valido": True, "mensaje": "Identificación disponible."}

    def validar_correo(self, data: ValidarCorreoRequest) -> dict:
        if self.repository.existe_por_correo(data.correo):
            return {"valido": False, "mensaje": "El correo electrónico ya se encuentra registrado."}
        return {"valido": True, "mensaje": "Correo disponible."}

    def registrar_usuario(self, data: RegistrarUsuarioRequest) -> dict:
        if self.repository.existe_por_identificacion(data.tipo_documento, data.numero_documento):
            raise ValueError("El documento de identidad ya se encuentra registrado.")
        if self.repository.existe_por_correo(data.correo):
            raise ValueError("El correo electrónico ya se encuentra registrado.")
        
        return self.repository.guardar(data.model_dump())