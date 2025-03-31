from __future__ import annotations

class Anuncio:
    def __init__(self, descripcion: str, estado: str = "En preparación") -> None:
        self.__descripcion = descripcion
        self.__estado = estado
        
    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        self.__descripcion = descripcion
        
    @property
    def estado(self) -> str:
        return self.__estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self.__estado = estado