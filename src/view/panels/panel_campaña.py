from src.config import COLOR_CUERPO_PRINCIPAL
from src.controller.CampañaController import CampañaController
from src.model.Campaña import Campaña
from src.model.Pago import Pago
from src.model.Anuncio import Anuncio
from src.model.Gasto import Gasto
from datetime import datetime, date
import customtkinter as ctk
import tkinter.messagebox as messagebox

def str_to_date(fecha_str: str) -> date:
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        return None

class PanelCampañaDesign:
    def __init__(self, panel_principal):
        self.controller = CampañaController()
        self._barra_superior = ctk.CTkFrame(panel_principal)
        self._barra_superior.pack(side = ctk.TOP, fill = ctk.X, expand = False)
        self._barra_inferior = ctk.CTkFrame(panel_principal)
        self._barra_inferior.pack(side = ctk.BOTTOM, fill = 'both', expand = True)
        self._label_titulo = ctk.CTkLabel(self._barra_superior, text = "Página Campaña", height = 20)
        self._label_titulo.configure(fg_color = "#222d33", font = ('Roboto', 30), bg_color = COLOR_CUERPO_PRINCIPAL)
        self._label_titulo.pack(side = ctk.TOP, fill = 'both', expand = True, padx = 10, pady = 10)
        self._center_frame = ctk.CTkFrame(panel_principal)
        self._center_frame.pack(fill = ctk.BOTH, expand = True, padx = 10, pady = 10)
        self._campanas_text = ctk.CTkTextbox(self._center_frame, width = 600, height = 300)
        self._campanas_text.pack(side = ctk.TOP, pady = 5)
        self._buttons_frame = ctk.CTkFrame(self._center_frame)
        self._buttons_frame.pack(pady = 5)
        
        btn_conf = {"width": 180, "height": 30, "corner_radius": 8}
        self._btn_registrar = ctk.CTkButton(self._buttons_frame, text = "Registrar Campaña", command=self.popup_registrar_campaña, **btn_conf)
        self._btn_registrar.grid(row=0, column=0, padx=5, pady=5)
        self._btn_finalizar = ctk.CTkButton(self._buttons_frame, text="Finalizar Campaña", command=self.popup_finalizar_campaña, **btn_conf)
        self._btn_finalizar.grid(row=0, column=1, padx=5, pady=5)
        self._btn_registrar_pago = ctk.CTkButton(self._buttons_frame, text="Registrar Pago", command=self.popup_registrar_pago, **btn_conf)
        self._btn_registrar_pago.grid(row=1, column=0, padx=5, pady=5)
        self._btn_consultar_pagos = ctk.CTkButton(self._buttons_frame, text="Consultar Pagos", command=self.popup_consultar_pagos, **btn_conf)
        self._btn_consultar_pagos.grid(row=1, column=1, padx=5, pady=5)
        self._btn_asignar_empleados = ctk.CTkButton(self._buttons_frame, text="Asignar Empleados", command=self.popup_asignar_empleados, **btn_conf)
        self._btn_asignar_empleados.grid(row=2, column=0, padx=5, pady=5)
        self._btn_registrar_contacto = ctk.CTkButton(self._buttons_frame, text="Registrar Contacto", command=self.popup_registrar_contacto, **btn_conf)
        self._btn_registrar_contacto.grid(row=2, column=1, padx=5, pady=5)
        self._btn_registrar_anuncio = ctk.CTkButton(self._buttons_frame, text="Registrar Anuncio", command=self.popup_registrar_anuncio, **btn_conf)
        self._btn_registrar_anuncio.grid(row=3, column=0, padx=5, pady=5)
        self._btn_finalizar_anuncio = ctk.CTkButton(self._buttons_frame, text="Finalizar Anuncio", command=self.popup_finalizar_anuncio, **btn_conf)
        self._btn_finalizar_anuncio.grid(row=3, column=1, padx=5, pady=5)
        self._btn_registrar_gasto = ctk.CTkButton(self._buttons_frame, text="Registrar Gasto", command=self.popup_registrar_gasto, **btn_conf)
        self._btn_registrar_gasto.grid(row=4, column=0, padx=5, pady=5)
        self._btn_consultar_gastos = ctk.CTkButton(self._buttons_frame, text="Consultar Gastos", command=self.popup_consultar_gastos, **btn_conf)
        self._btn_consultar_gastos.grid(row=4, column=1, padx=5, pady=5)
        self.actualizar_lista_campañas()
        
    def actualizar_lista_campañas(self):
        """Actualiza el área de texto con la lista de campañas registradas."""
        self._campanas_text.delete("1.0", ctk.END)
        for campaña in self.controller.campanas:
            # Se muestra id, título, estado y (si existe) empleado de contacto.
            contacto = getattr(campaña, "empleado_contacto", None)
            contacto_str = contacto.nombre if contacto is not None else "N/A"
            linea = f"ID: {campaña.id} | Título: {campaña.titulo} | Estado: {campaña.estado} | Contacto: {contacto_str}\n"
            self._campanas_text.insert(ctk.END, linea)