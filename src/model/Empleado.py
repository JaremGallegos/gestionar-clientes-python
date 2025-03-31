from __future__ import annotations
from src.model.CategoriaLaboral import CategoriaLaboral
from abc import ABC, abstractmethod
from typing import Optional

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