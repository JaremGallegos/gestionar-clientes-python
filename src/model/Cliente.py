from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.Campaña import Campaña

class Cliente:
    def __init__(self, id: int, nombre: str, direccion: str, detalle_contacto: str) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__detalle_contacto = detalle_contacto
        
        # Asociaciones:
        self.__campanas: List[Campaña] = []
    
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id
    
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
    
    @classmethod
    def from_dict(cls, data: dict) -> Cliente:
        """
        Crea una instancia de Cliente a partir de un diccionario.
        Se espera que 'data' contenga las claves: id, nombre, direccion, detalle_contacto.
        """
        return cls(
            id = data["id"],
            nombre = data["nombre"],
            direccion = data["direccion"],
            detalle_contacto = data["detalle_contacto"]
        )
    
    def to_dict(self):
        """
        Retorna un diccionario con la información del cliente.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
            "detalle_contacto": self.__detalle_contacto,
            "campaña": []
        }   