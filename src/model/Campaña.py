from datetime import date
from src.model import Cliente, Pago, Anuncio, Gasto, NotaConceptual, Empleado
from typing import Optional, List

class Campaña:
    def __init__(self, 
                 titulo: str, 
                 fecha_inicio: date, 
                 fecha_fin_prevista: date,
                 costes_estimados: float,
                 presupuesto: float,
                 cliente: Cliente) -> None:
        self.__titulo = titulo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin_prevista = fecha_fin_prevista
        self.__costes_estimados = costes_estimados
        self.__presupuesto = presupuesto
        self.__cliente = cliente
        self.__costes_reales = 0.0
        self.__estado = "En ejecución"

        # Asociaciones:
        self.__pagos: List[Pago] = []
        self.__anuncios: List[Anuncio] = []
        self.__gastos: List[Gasto] = [] 
        self.__notas_conceptuales: List[NotaConceptual] = []
        self.__empleados: List[Empleado] = []
        
        # Registrar esta campaña en el cliente
        cliente.registrar_campana(self)
        
    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo
        
    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: date) -> None:
        self.__fecha_inicio = fecha_inicio
        
    @property
    def fecha_fin_prevista(self) -> date:
        return self.__fecha_fin_prevista
    
    @fecha_fin_prevista.setter
    def fecha_fin_prevista(self, fecha_fin_prevista: date) -> None:
        self.__fecha_fin_prevista = fecha_fin_prevista
        
    @property
    def costes_estimados(self) -> float:
        return self.__costes_estimados
    
    @costes_estimados.setter
    def costes_estimados(self, costes_estimados: float) -> None:
        self.__costes_estimados = costes_estimados
    
    @property
    def presupuesto(self) -> float:
        return self.__presupuesto
    
    @presupuesto.setter
    def presupuesto(self, presupuesto: float) -> None:
        self.__presupuesto = presupuesto
        
    @property
    def costes_reales(self) -> float:
        return self.__costes_reales
    
    @costes_reales.setter
    def costes_reales(self, costes_reales: float) -> None:
        self.__costes_reales = costes_reales
        
    @property
    def estado(self) -> str:
        return self.__estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self.__estado = estado
        
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
    
    @property
    def pagos(self) -> List[Pago]:
        return self.__pagos
    
    def agregar_pago(self, pago: Pago) -> None:
        self.__pagos.append(pago)
        
    @property
    def anuncios(self) ->  List[Gasto]:
        return self.__anuncios
    
    def agregar_anuncio(self, anuncio: Anuncio) -> None:
        self.__anuncios.append(anuncio)
        
    @property
    def gastos(self) -> List[Gasto]:
        return self.__gastos
    
    def agregar_gasto(self, gasto: Gasto) -> None:
        self.__gastos.append(gasto)

    @property
    def notas_conceptuales(self) -> List[NotaConceptual]:
        return self.__notas_conceptuales
    
    def agregar_nota(self, nota: NotaConceptual) -> None:
        self.__notas_conceptuales.append(nota)
    
    @property
    def empleados(self) -> List[Empleado]:
        return self.__empleados
    
    def agregar_empleado(self, empleado: Empleado) -> None:
        self.__empleados.append(empleado) 