import os, json
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import List, Any, Dict
from datetime import date

class CategoriaController:
    def __init__(self, json_file: str = "./data/categorias.json") -> None:
        self.json_file = json_file
        self.categorias: List[CategoriaLaboral] = self._cargar_categorias()
    
    def _cargar_categorias(self) -> List[CategoriaLaboral]:
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, "r") as f:
            data = json.load(f)
            return [CategoriaLaboral.from_dict(item) for item in data]
    
    def _guardar_categorias(self) -> None:
        with open(self.json_file, "w") as f:
            json.dump([cat.to_dict() for cat in self.categorias], f, indent = 4)
    
    def _crear_categoria(self, categoria: CategoriaLaboral) -> None:
        """
        UC15: Crear nueva Categoría Laboral.
        Flujo Principal: Ingresar nombre y sueldo base.
        """
        pass
    
    def _modificar_categoria(self, id_categoria: Any, nuevos_datos: Dict[str, Any]) -> None:
        """
        UC15: Modificar Categoría Laboral.
        Flujo Principal: Actualizar los datos de la categoría (nombre, sueldo base).
        """
        pass
    
    def _eliminar_categoria(self, id_categoria: Any) -> None:
        """
        UC15: Eliminar Categoría Laboral.
        Flujo Principal: Eliminar la categoría seleccionada.
        """
        pass 