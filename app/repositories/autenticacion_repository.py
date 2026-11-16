from typing import Optional

class AutenticacionRepository:
    def __init__(self):
        # Base de datos simulada de usuarios registrados con hash de contraseña y estado
        self._db_usuarios = [
            {
                "id": 1,
                "correo": "johan@gmail.com",
                "password_hash": "pbkdf2_sha256_hash_123456",  # Simulacion hash contraseña: "123456"
                "password_plano": "123456",
                "rol": "Estudiante",
                "activo": True
            },
            {
                "id": 2,
                "correo": "docente@uts.edu.co",
                "password_hash": "pbkdf2_sha256_hash_docente", # Simulacion hash contraseña: "docente2026"
                "password_plano": "docente2026",
                "rol": "Docente",
                "activo": True
            },
            {
                "id": 3,
                "correo": "inactivo@uts.edu.co",
                "password_hash": "pbkdf2_sha256_hash_inactivo",
                "password_plano": "123456",
                "rol": "Estudiante",
                "activo": False
            }
        ]

    def buscar_por_correo(self, correo: str) -> Optional[dict]:
        for usuario in self._db_usuarios:
            if usuario["correo"] == correo:
                return usuario
        return None