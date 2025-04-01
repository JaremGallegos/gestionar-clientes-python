import os, json, logging
from src.model.Campaña import Campaña
from src.model.Pago import Pago
from src.model.Empleado import Empleado
from src.model.PersonalContacto import PersonalContacto
from src.model.Anuncio import Anuncio
from src.model.Gasto import Gasto
from typing import List, Any, Optional
from datetime import date

logging.basicConfig(
    filename = "./logging/auditoria_campaña.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s %(message)s'
)

class CampañaController:
    def __init__(self, path_file: str = "./data/campañas.json") -> None:
        self.json_file = path_file
        self.campanas: List[Campaña] = self._cargar_campanas()
    
    def _cargar_campanas(self) -> List[Campaña]:
        """
        Cargar las campañas desde el archivo JSON. Retorna lista vacia si el archivo no existe
        o esta corrupto.
        """
        if not os.path.exists(self.json_file):
            return []
        
        try:
            with open(self.json_file, "r", encoding = "utf-8") as file:
                data = json.load(file)
                return [Campaña.from_dict(item) for item in data]
        except json.JSONDecodeError:
            logging.error("Error al codificar JSON en la carga de campañas.")
            return []
    
    def _guardar_campanas(self) -> None:
        """
        Guardar la lista de campañas de forma atomica utilizando un archivo temporal.
        """
        temp_file = self.json_file + ".tmp"
        with open(temp_file, "w", encoding = "utf-8") as file:
            data = [campana.to_dict() for campana in self.campanas]
            json.dump(data, file, indent = 4, default = str)
        os.replace(temp_file, self.json_file)
    
    def registrar_campana(self, campana: Campaña) -> bool:
        """
        UC2: Registrar Campaña Publicitaria.
        Flujo Principal: Ingresar datos (título, fechas, costes estimados, presupuesto) y asociarla a un cliente.
        """
        if any (c.id == campana.id for c in self.campanas):
            logging.warning(f"Campaña con id {campana.id} ya existe.")
            return False
        
        self.campanas.append(campana)
        self._guardar_campanas()
        logging.info(f"Campaña registrada: {campana.to_dict()}")
        return True
        
    def registrar_finalizacion_campana(self, campana_id: int, fecha_cierre: date) -> bool:
        """
        UC3: Registrar Finalización de Campaña.
        Flujo Principal: Seleccionar la campaña, confirmar finalización y actualizar su estado a 'Finalizada'.
        """
        campana = self._buscar
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
    
    def registrar_gasto(self, campana_id: int, gasto: Gasto) -> bool:
        """
        UC10: Registrar Gastos de Campaña.
        Flujo Principal: Ingresar datos del gasto (monto, descripción, fecha) y actualizar los costes reales.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para registrar gasto.")
            return False
        
        campana.agregar_gasto(gasto)
        campana.costes_reales += gasto.monto
        self._guardar_campanas()
        logging.info(f"Gasto registrado en campaña {campana_id}: monto {gasto.monto}, descripcion {gasto.descripcion}")
        return True
    
    def consultar_gastos(self, campana_id: int) -> List[Gasto]:
        """
        UC11: Consultar Gastos de Campaña.
        Flujo Principal: Recuperar el resumen de gastos (costes reales) de la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para consulta de gastos.")
            return []
        return campana.gastos
    
    # Metodo auxiliar para buscar una campaña por su id
    def _buscar_campana(self, campana_id: int) -> Optional[Campaña]:
        for campana in self.campanas:
            if campana.id == campana_id:
                return campana
        return None