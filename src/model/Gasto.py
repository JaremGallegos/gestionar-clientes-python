from __future__ import annotations
from datetime import date

class Gasto:
    def __init__(self, monto: float, descripcion: str, fecha: date) -> None:
        self.__monto = monto
        self.__descripcion = descripcion
        self.__fecha = fecha
        
    @property
    def monto(self) -> float:
        return self.__monto
    
    @monto.setter
    def monto(self, monto: float) -> None:
        self.__monto = monto

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