import os, json
from src.model.Empleado import Empleado
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