from src.config import COLOR_CUERPO_PRINCIPAL
import customtkinter as ctk

class PanelClienteDesign:
    def __init__(self, panel_principal):
        self._barra_superior = ctk.CTkFrame(panel_principal)
        self._barra_superior.pack(side = ctk.TOP, fill = ctk.X, expand = False)
        self._barra_inferior = ctk.CTkFrame(panel_principal)
        self._barra_inferior.pack(side = ctk.BOTTOM, fill = 'both', expand = True)
        self._label_titulo = ctk.CTkLabel(self._barra_superior, text = "Página Cliente", height = 20)
        self._label_titulo.configure(fg_color = "#222d33", font = ('Roboto', 30), bg_color = COLOR_CUERPO_PRINCIPAL)
        self._label_titulo.pack(side = ctk.TOP, fill = 'both', expand = True)
