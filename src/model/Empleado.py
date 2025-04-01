from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.CategoriaLaboral import CategoriaLaboral    

class Empleado(ABC):
    def __init__(self, nombre: str, email: str, rol: str, categoria:Optional[CategoriaLaboral] = None) -> None:
        self._nombre = nombre
        self._email = email
        self._rol = rol
        self._categoria = categoria
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email
        
    @property
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, rol: str) -> None:
        self._rol = rol
        
    @property
    def categoria(self) -> Optional[CategoriaLaboral]:
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria: CategoriaLaboral) -> None:
        self._categoria = categoria
        
    @abstractmethod
    def from_dict(cls, data: dict) -> Empleado:
        """
        Crea una instancia de Cliente a partir de un diccionario.
        Se espera que 'data' contenga las claves: id, nombre, email, categoria y categoria_laboral.
        """
        return cls(
            id = data["id"],
            nombre = data["nombre"],
            direccion = data["email"],
            rol = data["categoria"],
            categoriaLaboral = data["categoria_laboral"]
        )
    
    @abstractmethod
    def to_dict(self):
        """
        Retorna un diccionario con la información del cliente.
        """
        pass