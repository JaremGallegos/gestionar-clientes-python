import os, json
from src.model.Empleado import Empleado
from src.model.DirectorCampaña import DirectorCampaña
from typing import List, Any, Dict

class EmpleadoController:
    def __init__(self, json_file: str = "./data/empleados.json") -> None:
        self.json_file = json_file
        self.empleados: List[Empleado] = self._cargar_empleados()
    
    def _cargar_empleados(self) -> List[Empleado]:
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, "r") as f:
            data = json.load(f)
            # Se debe implementar la logica de deserializacion segun el rol
            # Aqui se asume que cada empleado tiene un campo 'rol'
            empleados = []
            for item in data:
                rol = item.get("rol", "")
                if rol == "Director de Campaña":
                    empleados.append(DirectorCampaña.fro)
    
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