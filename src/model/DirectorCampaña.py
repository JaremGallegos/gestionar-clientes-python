from __future__ import annotations
from src.model.Empleado import Empleado
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import Optional

class DirectorCampaña(Empleado):
    def __init__(self, nombre: str, email: str, categoria: Optional[CategoriaLaboral] = None) -> None:
        super().__init__(nombre, email, "Director de Campaña", categoria)