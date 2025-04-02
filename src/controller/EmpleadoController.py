import os, json, logging
from src.model.Empleado import Empleado
from src.model.DirectorCampaña import DirectorCampaña
from typing import List, Any, Dict

logging.basicConfig(
    filename = './logging/auditoria_empleados.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class EmpleadoController:
    def __init__(self, file_path: str = "./data/empleados.json") -> None:
        self.json_file = file_path
        self.empleados: List[Empleado] = self._cargar_empleados()
    
    def _cargar_empleados(self) -> List[Empleado]:
        pass
    
    def _agregar_empleado(self, empleado: Empleado) -> None:
        """
        UC14: Agregar nuevo trabajador.
        Flujo Principal: Ingresar los datos personales y profesionales del empleado.
        """
        pass
    
    def _modificar_empleado(self, id_empleado: Any, nuevos_datos: Dict[str, Any]) -> None:
        """
        UC14: Modificar datos de un trabajador.
        Flujo Principal: Actualizar los datos del empleado.
        """
        pass
    
    def _eliminar_empleado(self, id_empleado: Any) -> None:
        """
        UC14: Eliminar un trabajador.
        Flujo Principal: Eliminar el registro del empleado.
        """
        pass