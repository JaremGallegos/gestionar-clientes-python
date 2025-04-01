from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.Empleado import Empleado   
    from src.model.CategoriaLaboral import CategoriaLaboral

class PersonalContable(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Pesonal Contable", categoria)