class UsuarioRepository:
    def __init__(self):
        self._db_usuarios = []
        self._id_counter = 1

    def existe_por_identificacion(self, tipo_doc: str, num_doc: str) -> bool:
        return any(
            u["tipo_documento"] == tipo_doc and u["numero_documento"] == num_doc
            for u in self._db_usuarios
        )

    def existe_por_correo(self, correo: str) -> bool:
        return any(u["correo"].lower() == correo.lower() for u in self._db_usuarios)

    def guardar(self, datos_usuario: dict) -> dict:
        datos_usuario["id"] = self._id_counter
        self._id_counter += 1
        self._db_usuarios.append(datos_usuario)
        return datos_usuario