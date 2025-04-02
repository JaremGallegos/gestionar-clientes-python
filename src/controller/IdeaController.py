import os, json, logging
from src.model.Empleado import Empleado
from src.model.Idea import Idea
from typing import List, Any, Dict
from datetime import date

logging.basicConfig(
    filename = './logging/auditoria_ideas.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class IdeaController:
    def __init__(self, file_path: str = "/data/ideas.json") -> None:
        self.json_file = file_path
        self.ideas: List[Idea] = self._cargar_ideas()
    
    def _cargar_ideas(self) -> List[Idea]:
        """
        Carga las ideas desde el archivo JSON. Retorna una lista vacia si el
        archivo no existe o hay error.
        """
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, "r", encoding = "utf-8") as file:
                data = json.load(file)
                return [Idea.from_dict(item) for item in data]
        except json.JSONDecodeError:
            logging.error("Error al decodificar JSON en la carga de ideas.")
            return []
        
    def _guardar_ideas(self) -> None:
        """
        Guarda la lista de ideas en el archivo JSON de forma atomica.
        """
        temp_file = self.json_file + ".tmp"
        with open(temp_file, "w", encoding = "utf-8") as file:
            data = [idea.to_dict() for idea in self.ideas]
            json.dump(data, file, indent = 4)
        os.replace(temp_file, self.json_file)
    
    def registrar_idea(self, idea: Idea) -> bool:
        """
        UC12: Registrar Ideas de Anuncios
        Flujo Principal: Permite al Personal Creativo ingresar ideas o notas conceptuales para los anuncios.
        Requerimientos: Debe permitirse la edición o eliminación posterior.
        Precondicion: Usuario autenticado con permisos de Personal Creativo.
        """
        # Verificar que no exista ya una idea con el mismo id (por seguridad)
        if any(i.id == idea.id for i in self.ideas):
            logging.warning(f"Idea con id {idea.id} ya existe.")
            return False
        
        self.ideas.append(idea)
        self._guardar_ideas()
        logging.info(f"Idea registrada: {idea.to_dict()}")
        return True
    
    def consultar_ideas(self) -> List[Idea]:
        """
        UC13: Consultar Ideas de Anuncios
        Flujo Principal: Permite visualizar las ideas y notas conceptuales registradas.
        Requerimientos: La consulta debe permitir filtrar o buscar.
        Precondicion: Debe existir al menos una idea registrada.
        """
        return self.ideas