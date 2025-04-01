from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.NotaConceptual import NotaConceptual 
    from src.model.Empleado import Empleado

class Idea(NotaConceptual):
    def __init__(self, descripcion: str, fecha, date, autor: Empleado) -> None:
        super().__init__(descripcion, fecha, date, autor)