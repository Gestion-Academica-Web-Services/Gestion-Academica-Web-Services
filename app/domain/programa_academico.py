from pydantic import BaseModel

class ProgramaAcademicoResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    nivel_formacion: str
    titulo_otorgado: str
    total_creditos: int
    duracion_semestres: int
    vigencia: str
    activo: bool