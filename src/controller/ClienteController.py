import os, json, logging
from src.model.Cliente import Cliente
from typing import List, Dict, Any, Optional

logging.basicConfig(
    filename = './logging/auditoria_clientes.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s %(message)s'
)

class ClienteController:
    def __init__(self, file_path: str = "./data/clientes.json") -> None:
        self.json_file = file_path
        self.clientes: List[Cliente] = self._cargar_clientes()
        
    def _cargar_clientes(self) -> List[Cliente]:
        """
        Cargar los clientes desde el archivo JSON. Si no existe, retorna
        lista vacia.
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, "r", encoding = "utf-8") as file:
            try:
                data = json.load(file)
                return [Cliente.from_dict(item) for item in data]
            except json.JSONDecodeError:
                logging.error("Error al decodificar JSON en la carga de clientes.")
    
    def _guardar_clientes(self) -> None:
        """
        Guardar la lista de clientes en el archivo JSON de manera atomica.
        """
        temp_file = self.json_file + ".tmp"
        with open(temp_file, "w", encoding = "utf-8") as file:
            data = [cliente.to_dict() for cliente in self.clientes]
            json.dump(data, file, indent = 4)
        os.replace(temp_file, self.json_file)     
     
    def _verificar_autenticacion(self, usuario) -> bool:
        """
        Verificacion que el usuario este autenticado y tenga el rol 
        'Director de Campaña'. Se espera que el objeto usuario tenga
        atributos 'username' y 'role'
        """
        if usuario and getattr(usuario, "role", None) == "Director de Campaña":
            return True
        return False
     
    def agregar_cliente(self, usuario, cliente: Cliente) -> bool:
        """
        UC1: Agrega un nuevo cliente.
        Precondición: Director de Campaña autenticado.
        Flujo Principal: Ingresar datos del cliente (nombre, dirección, detalle de contacto)
        y confirmar la acción. La transacción es atómica y se registra para auditoría.
        """
        # Verificacion si el usuario que está agregando un cliente esta autenticado.
        if not self._verificar_autenticacion(usuario):
            logging.warning("Intento de agregar cliente sin autenticacion adecuada.")
            return False
        
        # Verificar que no exista un cliente con el mismo id.
        if any(c.id == cliente.id for c in self.clientes):
            logging.warning(f"El cliente con id {cliente.id} ya existe.")
            return False

        self.clientes.append(cliente)
        self._guardar_clientes()
        logging.info(f"Cliente agregado: {cliente.to_dict()}")
        return True
        
    def modificar_cliente(self, usuario, cliente_modificado: Cliente) -> bool:
        """
        UC1: Modificar datos de un cliente existente.
        Flujo Principal: Buscar el cliente por su identificador y actualizar sus datos.
        Precondiciones: El usuario debe estar autenticado y tener un rol 'Director de Campaña'.
        """
        if not self._verificar_autenticacion(usuario):
            logging.warning("Intento de modificar cliente sin autenticacion adecuada.")
            return False
                
        for index, cliente in enumerate(self.clientes):
            if cliente.id == cliente_modificado.id:
                self.clientes[index] = cliente_modificado
                self._guardar_clientes()
                logging.info(f"Cliente modificado: {cliente_modificado.to_dict()}")
                return True
        
        logging.warning(f"No encontro cliente con id {cliente_modificado.id} para modificar.")
        return False
        
    def elimina_cliente(self, usuario, cliente_id: int) -> bool:
        """
        UC1: Eliminar un cliente.
        Flujo Principal: Buscar y eliminar el cliente; la transacción es atómica.
        Precondicion: El usuario debe estar autenticado y tener el rol 'Director de Campaña'.
        """
        if not self._verificar_autenticacion(usuario):
            logging.warning("Intento de eliminar cliente sin autenticacion adecuada.")
            return False
        
        cliente_encontrado: Optional[Cliente] = None
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            self._guardar_clientes()        
            logging.info(f"Cliente eliminado: {cliente_encontrado.to_dict()}")
            return True
        else:
            logging.warning(f"No se encontro cliente con id {cliente_id} para eliminar.")
            return False
    
    def obtener_clientes(self) -> List[Cliente]:
        """
        Retorna la lista de clientes registrados.
        """
        return self.clientes