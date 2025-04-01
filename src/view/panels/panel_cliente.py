from src.config import COLOR_CUERPO_PRINCIPAL
from src.controller.ClienteController import ClienteController
from src.model.Cliente import Cliente
import customtkinter as ctk

class PanelClienteDesign:
    def __init__(self, panel_principal):
        self.controller = ClienteController()
        self._barra_superior = ctk.CTkFrame(panel_principal)
        self._barra_superior.pack(side = ctk.TOP, fill = ctk.X, expand = False)
        self._barra_inferior = ctk.CTkFrame(panel_principal)
        self._barra_inferior.pack(side = ctk.BOTTOM, fill = 'both', expand = True)
        self._label_titulo = ctk.CTkLabel(self._barra_superior, text = "Página Cliente", height = 20)
        self._label_titulo.configure(fg_color = "#222d33", font = ('Roboto', 30), bg_color = COLOR_CUERPO_PRINCIPAL)
        self._label_titulo.pack(side = ctk.TOP, fill = 'both', expand = True)
        self._crear_interfaz()
        
    def _crear_interfaz(self):
        self._entry_nombre = ctk.CTkEntry(self._barra_inferior, placeholder_text = "Nombre del Cliente")
        self._entry_nombre.pack(pady = 5)
        self._entry_direccion = ctk.CTkEntry(self._barra_inferior, placeholder_text = "Dirección")
        self._entry_direccion.pack(pady = 5)
        self._entry_contacto = ctk.CTkEntry(self._barra_inferior, placeholder_text = "Contacto")
        self._entry_contacto.pack(pady = 5)
        self._boton_agregar = ctk.CTkButton(self._barra_inferior, text = "Agregar Cliente", command = self._agregar_cliente)
        self._boton_agregar.pack(pady = 5)
        self._lista_clientes = ctk.CTkTextbox(self._barra_inferior, height = 150)
        self._lista_clientes.pack(pady = 5)
        self._actualizar_lista()
        
    def _agregar_cliente(self):
        nombre = self._entry_nombre.get()
        direccion = self._entry_direccion.get()
        contacto = self._entry_contacto.get()
        
        if nombre and direccion and contacto:
            nuevo_cliente = Cliente(id = len(self.controller.clientes) + 1, nombre = nombre, direccion = direccion, detalle_contacto = contacto)
            if self.controller.agregar_cliente("Director de Campaña", nuevo_cliente):
                self._actualizar_lista()
    
    def _actualizar_lista(self):
        self._lista_clientes.delete("1.0", ctk.END)
        for cliente in self.controller.obtener_clientes():
            self._lista_clientes.insert(ctk.END, f"{cliente.id} - {cliente.nombre}\n")
    