from customtkinter import CTkFont
from src.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
from src.util.util_ventana import UtilVentana as util_ventana
from src.util.util_imagenes import UtilImagen as util_imagen
import customtkinter as ctk

class FormPrincipalDesign(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._logo = util_imagen.leer_imagen("./assets/logo.jpg", (560, 136))
        self._perfil = util_imagen.leer_imagen("./assets/perfil.png", (100, 100))
        self._set_appearance_mode("System")
        self.config_window()
    
    def config_window(self):
        self.title("Prototipo")
        self.iconbitmap("./assets/logoing.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)