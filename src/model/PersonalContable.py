from src.model import Empleado, CategoriaLaboral
from typing import Optional

class PersonalContable(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Pesonal Contable", categoria)