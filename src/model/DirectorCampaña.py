from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.Empleado import Empleado
    from src.model.CategoriaLaboral import CategoriaLaboral

class DirectorCampaña(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Director de Campaña", categoria)