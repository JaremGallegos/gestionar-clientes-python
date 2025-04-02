from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.NotaConceptual import NotaConceptual 
    from src.model.Empleado import Empleado

class Idea(NotaConceptual):
    def __init__(self, id: int, descripcion: str, autor: Empleado, fecha: date) -> None:
        super().__init__(descripcion, fecha, date, autor)
        self.id = id
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "autor": self.autor,
            "fecha": self.fecha.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> Idea:
        return cls(
            id = data["id"],
            descripcion = data["descripcion"],
            autor = data["autor"],
            fecha = date.fromisoformat(data["fecha"])
        )