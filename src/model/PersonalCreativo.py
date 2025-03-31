from src.model import Empleado, CategoriaLaboral
from typing import Optional

class PersonalCreativo(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Personal Creativo", categoria)
        