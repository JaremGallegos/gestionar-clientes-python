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
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para finalizar.")
            return False
        
        if campana.estado != "En ejecucion":
            logging.warning(f"Campaña con id {campana_id} no se encuentra en ejecución.")
            
        campana.estado = "Finalizado"
        setattr(campana, 'fecha_cierre', fecha_cierre)
        self._guardar_campanas()
        logging.info(f"Campaña finalizada: {campana.to_dict()} con fecha de cierre {fecha_cierre}")
        return True
        
    
    def registrar_pago(self, campana_id: int, pago: Pago) -> bool:
        """
        UC4: Registrar Pago de Campaña.
        Flujo Principal: Ingresar monto y fecha del pago, asociándolo a la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para registrar pago.")
            return False
        
        campana.agregar_pago(pago)
        self._guardar_campanas()
        logging.info(f"Pago registrado en campaña {campana_id}: monto {pago.monto}, fecha {pago.fecha_pago}")
        return True
    
    def consultar_pagos(self, campana_id: int) -> List[Pago]:
        """
        UC5: Consultar Pagos de Campaña.
        Flujo Principal: Recuperar la lista de pagos asociados a la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para consulta de pagos.")
            return[]
        return campana.pagos
    
    def asignar_empleados(self, campana_id: int, empleados: List[Empleado]) -> bool:
        """
        UC6: Asignar Empleados a Campaña.
        Flujo Principal: Seleccionar empleados disponibles y asignarlos a la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para asignar empleados.")
            return False

        for empleado in empleados:
            if empleado not in campana.empleados:
                campana.agregar_empleado(empleado)
        
        self._guardar_campanas()
        logging.info(f"Empleados asignados a campaña {campana_id}: {[emp.nombre for emp in empleados]}")
        return True
    
    def registrar_empleado_contacto(self, campana_id: int, empleado: Empleado) -> bool:
        """
        UC7: Registrar Empleado de Contacto para Campaña.
        Flujo Principal: Designar un empleado (PersonalContacto) como contacto principal para la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para asignar contacto.")
            return False

        # Asignar el empleado si no esta previamente asignado
        if empleado not in campana.empleados:
            campana.agregar_empleado(empleado)
            
        # Designar el empleado como contacto principal
        setattr(campana, 'empleado_contacto', empleado)
        self._guardar_campanas()
        logging.info(f"Empleado {empleado.nombre} designado como contacto en campaña {campana_id}")
        return True
    
    def registrar_anuncio(self, campana_id: int, anuncio: Anuncio) -> bool:
        """
        UC8: Registrar Anuncio de Campaña.
        Flujo Principal: Ingresar la descripción del anuncio y asociarlo a la campaña.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para registrar anuncio.")
            return False
        
        campana.agregar_anuncio(anuncio)
        self._guardar_campanas()
        logging.info(f"Anuncio registrado en campaña {campana_id}: {anuncio.descripcion}")
        return True
    
    def registrar_finalizacion_anuncio(self, campana_id: int, anuncio_index: int) -> bool:
        """
        UC9: Registrar Finalización de Anuncio.
        Flujo Principal: Actualizar el estado del anuncio a 'Finalizado' y registrar la fecha.
        """
        campana = self._buscar_campana(campana_id)
        if campana is None:
            logging.warning(f"Campaña con id {campana_id} no encontrada para finalizar anuncio.")
            return False
        
        if anuncio_index < 0 or anuncio_index >= len(campana.anuncios):
            logging.warning(f"Indice de anuncio inválido para la campaña {campana_id}.")
            return False
        
        anuncio = campana.anuncios[anuncio_index]
        # anuncio.estado = "Finalizado"
        self._guardar_campanas()
        logging.info(f"Anuncio finalizado en campaña {campana_id}: {anuncio.descripcion}")
        return True
    
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