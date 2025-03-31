from __future__ import annotations
from src.model import Campaña
from typing import Optional, List

class Cliente:
    def __init__(self, nombre: str, direccion: str, detalle_contacto: str) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__detalle_contacto = detalle_contacto
        
        # Asociaciones:
        self.__campanas: List[Campaña] = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    
    @property 
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direccion: str) -> None:
        self.__direccion = direccion
        
    @property
    def detalle_contacto(self) -> str:
        return self.__detalle_contacto
    
    @detalle_contacto.setter
    def detalle_contacto(self, detalle_contacto: str) -> None:
        self.__detalle_contacto = detalle_contacto
        
    @property
    def campanas(self) -> List[Campaña]:
        return self.__campanas
    
    def registrar_campana(self, campana: Campaña) -> None:
        self.__campanas.append(campana)