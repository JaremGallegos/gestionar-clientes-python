from __future__ import annotations
from src.model.NotaConceptual import NotaConceptual 
from src.model.Empleado import Empleado
from datetime import date

class Idea(NotaConceptual):
    def __init__(self, descripcion: str, fecha, date, autor: Empleado) -> None:
        super().__init__(descripcion, fecha, date, autor)