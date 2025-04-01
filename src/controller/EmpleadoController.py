import os, json
from src.model.Empleado import Empleado
from src.model.DirectorCampaña import DirectorCampaña
from typing import List, Any

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