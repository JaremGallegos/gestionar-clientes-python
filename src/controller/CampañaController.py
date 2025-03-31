import os, json
from src.model.Campaña import Campaña
from src.model.Pago import Pago
from src.model.Empleado import Empleado
from src.model.PersonalContacto import PersonalContacto
from src.model.Anuncio import Anuncio
from src.model.Gasto import Gasto
from typing import List, Any
from datetime import date

class CampañaController:
    def __init__(self, json_file: str = "./data/campañas.json") -> None:
        self.json_file = json_file
        self.campanas: List[Campaña] = self._cargar_campanas()
    
    def _cargar_campanas(self) -> List[Campaña]:
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, "r") as f:
            data = json.load(f)
            return [Campaña.from_dict(item) for item in data]
    
    def _guardar_campanas(self) -> None:
        with open(self.json_file, "w") as f:
            json.dump([campana.to_dict() for campana in self.campanas], f, indent = 4)
    
    def registrar_campana(self, campana: Campaña) -> None:
        """
        UC2: Registrar Campaña Publicitaria.
        Flujo Principal: Ingresar datos (título, fechas, costes estimados, presupuesto) y asociarla a un cliente.
        """
        if not campana.titulo or campana.presupuesto <= 0:
            raise ValueError("Datos de campaña inválidos.")
        self.campanas.append(campana)
        self._guardar_campanas()
        
    def finalizar_campana(self, id_campana: Any, fecha_finalizacion: date) -> None:
        """
        UC3: Registrar Finalización de Campaña.
        Flujo Principal: Seleccionar la campaña, confirmar finalización y actualizar su estado a 'Finalizada'.
        """
        for campana in self.campanas:
            if campana.estado != "En ejecución":
                raise ValueError("La campaña no se encuentra en ejecución.")
            campana.estado = "Finalizada"
            campana.fecha_fin_prevista = fecha_finalizacion
            self._guardar_campanas()
            return
        raise LookupError("Campaña no encontrada.")
    
    def registrar_pago(self, id_campana: Any, pago: Pago) -> None:
        """
        UC4: Registrar Pago de Campaña.
        Flujo Principal: Ingresar monto y fecha del pago, asociándolo a la campaña.
        """
        for campana in self.campanas:
            if campana.id == id_campana:
                if pago.monto <= 0:
                    raise ValueError("Monto de pago inválido.")
                campana.agregar_pago(pago)
                self._guardar_campanas()
                return
        raise LookupError("Campaña no encontrada.")
    
    def consultar_pagos(self, id_campana: Any) -> List[Pago]:
        """
        UC5: Consultar Pagos de Campaña.
        Flujo Principal: Recuperar la lista de pagos asociados a la campaña.
        """
        for campana in self.campanas:
            if campana.id == id_campana:
                return campana.pagos
        raise LookupError("Campaña no encontrada.")
    
    def asignar_empleados(self, id_campana: Any, empleados: List[Empleado]) -> None:
        """
        UC6: Asignar Empleados a Campaña.
        Flujo Principal: Seleccionar empleados disponibles y asignarlos a la campaña.
        """
        for campana in self.campanas:
            if campana.id == id_campana:
                for emp in empleados:
                    if emp not in campana.empleados:
                        campana.agregar_empleado(emp)
                self._guardar_campanas()
                return
        raise LookupError("Campaña no encontrada.")
    
    def registrar_empleado_contacto(self, id_campana: Any, empleado_contacto: PersonalContacto) -> None:
        """
        UC7: Registrar Empleado de Contacto para Campaña.
        Flujo Principal: Designar un empleado (PersonalContacto) como contacto principal para la campaña.
        """
        pass
    
    def registrar_anuncio(self, id_campana: Any, anuncio: Anuncio) -> None:
        """
        UC8: Registrar Anuncio de Campaña.
        Flujo Principal: Ingresar la descripción del anuncio y asociarlo a la campaña.
        """
        pass
    
    def finalizar_anuncio(self, id_campana: Any, id_anuncio: Any, fecha_finalizacion: date) -> None:
        """
        UC9: Registrar Finalización de Anuncio.
        Flujo Principal: Actualizar el estado del anuncio a 'Finalizado' y registrar la fecha.
        """
        pass
    
    def registrar_gasto(self, id_campana: Any, gasto: Gasto) -> None:
        """
        UC10: Registrar Gastos de Campaña.
        Flujo Principal: Ingresar datos del gasto (monto, descripción, fecha) y actualizar los costes reales.
        """
        pass
    
    def consultar_gastos(self, id_campana: Any) -> List[Gasto]:
        """
        UC11: Consultar Gastos de Campaña.
        Flujo Principal: Recuperar el resumen de gastos (costes reales) de la campaña.
        """
        pass