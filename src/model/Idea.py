from __future__ import annotations
from src.model import NotaConceptual, Empleado
from datetime import date

class Idea(NotaConceptual):
    def __init__(self, descripcion: str, fecha, date, autor: Empleado) -> None:
        super().__init__(descripcion, fecha, date, autor)