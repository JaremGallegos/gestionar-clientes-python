from src.model import Empleado, CategoriaLaboral
from typing import Optional

class PersonalContacto(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Personal de Contacto", categoria)