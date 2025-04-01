from tkinter import messagebox
from customtkinter import CTkFont
from src.config import COLOR_NEUTRO_NEGRO, COLOR_CUERPO_ALTERNATICA
from src.util.util_ventana import UtilVentana as util_ventana
from src.util.util_imagenes import UtilImagen as util_imagen
import customtkinter as ctk

ctk.set_appearance_mode("System")

class FormSignupDesign(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self._logo = util_imagen.leer_imagen("./assets/logo.jpg", (200, 200))
        self.config_window()
        self.body_frame()
        
    def config_window(self):
        self.title("Registrar")
        self.iconbitmap("./assets/logoing.ico")
        w, h = 400, 100
        util_ventana.centrar_ventana(self, w, h)
    
    def body_frame(self):
        self._label_version = ctk.CTkLabel(self, text = "Version: ")