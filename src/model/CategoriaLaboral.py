from __future__ import annotations

class CategoriaLaboral:
    def __init__(self, nombre: str, sueldo_base: float) -> None:
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre
        
    @property
    def sueldo_base(self) -> float:
        return self.__sueldo_base
    
    @sueldo_base.setter
    def sueldo_base(self, sueldo_base: float) -> None:
        self.__sueldo_base = sueldo_base