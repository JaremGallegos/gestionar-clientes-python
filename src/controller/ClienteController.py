import os, json
from src.model.Cliente import Cliente
from typing import List, Dict, Any

class ClienteController:
    def __init__(self, json_file: str = "./data/clientes.json") -> None:
        self.json_file = json_file
        self.clientes: List[Cliente] = self._cargar_clientes()
        
    def _cargar_clientes(self) -> List[Cliente]:
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, "r") as f:
            data = json.load(f)
            return [Cliente.from_dict(item) for item in data]
    
    def _guardar_clientes(self) -> None:
        with open(self.json_file, "w") as f:
            json.dump([cliente.to_dict() for cliente in self.clientes], f, indent = 4)     
     
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        UC1: Agrega un nuevo cliente.
        Precondición: Director de Campaña autenticado.
        Flujo Principal: Ingresar datos del cliente (nombre, dirección, detalle de contacto)
        y confirmar la acción. La transacción es atómica y se registra para auditoría.
        """
        if not cliente.nombre or not cliente.direccion or not cliente.detalle_contacto:
            raise ValueError("Datos incompletos para el cliente.")
        self.clientes.append(cliente)
        self._guardar_clientes()
        
    def modificar_cliente(self, id_cliente: Any, nuevos_datos: Dict[str, Any]) -> None:
        """
        UC1: Modificar datos de un cliente existente.
        Flujo Principal: Buscar el cliente por su identificador y actualizar sus datos.
        """
        encontrado = False
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                if "nombre" in nuevos_datos:
                    cliente.nombre = nuevos_datos["nombre"]
                if "direccion" in nuevos_datos:
                    cliente.direccion = nuevos_datos["direccion"]
                if "detalle_contacto" in nuevos_datos:
                    cliente.detalle_contacto = nuevos_datos["detalle_contacto"]
                self._guardar_clientes()
                encontrado = True
                break
        if not encontrado:
            raise LookupError("Cliente no encontrado.")
        
    def elimina_cliente(self, id_cliente: Any) -> None:
        """
        UC1: Eliminar un cliente.
        Flujo Principal: Buscar y eliminar el cliente; la transacción es atómica.
        """
        self.clientes = [cliente for cliente in self.clientes if cliente.id != id_cliente]
        self._guardar_clientes()