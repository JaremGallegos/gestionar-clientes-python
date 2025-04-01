from src.model.Empleado import Empleado
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.CategoriaLaboral import CategoriaLaboral

class PersonalContacto(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Personal de Contacto", categoria)