from __future__ import annotations
from src.model.Empleado import Empleado
from datetime import date

class NotaConceptual:
    def __init__(self, descripcion: str, fecha: date, autor: Empleado) -> None:
        self.__descripcion = descripcion
        self.__fecha = fecha
        self.__autor = autor
    
    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        self.__descripcion = descripcion
        
    @property
    def fecha(self) -> date:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha: date) -> None:
        self.__fecha = fecha
        
    @property
    def autor(self) -> Empleado:
        return self.__autor
    
    @autor.setter
    def autor(self, autor: Empleado) -> None:
        self.__autor = autor