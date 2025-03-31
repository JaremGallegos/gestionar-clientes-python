from __future__ import annotations
from datetime import date

class Pago:
    def __init__(self, monto: float, fecha_pago: date) -> None:
        self.__monto = monto
        self.__fecha_pago = fecha_pago
        
    @property
    def monto(self) -> float:
        return self.__monto
    
    @monto.setter
    def monto(self, monto: float) -> None:
        self.__monto = monto
        
    @property
    def fecha_pago(self) -> date:
        return self.__fecha_pago
    
    @fecha_pago.setter
    def fecha_pago(self, fecha_pago: date) -> None:
        self.__fecha_pago = fecha_pago