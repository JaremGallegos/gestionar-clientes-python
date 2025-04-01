from tkinter import messagebox
from customtkinter import CTkFont
from src.config import COLOR_NEUTRO_NEGRO, COLOR_CUERPO_ALTERNATICA, COLOR_PRIMITIVO_NEGRO, COLOR_LOGIN_MARCA, COLOR_CUERPO_PRINCIPAL
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
        w, h = 400, 410
        util_ventana.centrar_ventana(self, w, h)
    
    def body_frame(self):
        self._barra_cuerpo = ctk.CTkFrame(self, bg_color = COLOR_CUERPO_ALTERNATICA, fg_color = COLOR_CUERPO_ALTERNATICA, width = 600)
        self._barra_cuerpo.pack(side = ctk.RIGHT, expand = True, fill = ctk.BOTH)
        self._barra_top = ctk.CTkFrame(self._barra_cuerpo, height = 50, bg_color = COLOR_NEUTRO_NEGRO)
        self._barra_top.pack(side = ctk.TOP, fill = ctk.X)
        self._title_frame = ctk.CTkLabel(self._barra_top, text = "Registrar mi Usuario", font = ('Times', 30), fg_color = COLOR_PRIMITIVO_NEGRO,
                                         bg_color = COLOR_CUERPO_ALTERNATICA, pady = 50)
        self._title_frame.pack(expand = True, fill = ctk.BOTH)
        self._fill_frame = ctk.CTkFrame(self._barra_cuerpo, height = 50, bg_color = COLOR_CUERPO_ALTERNATICA, fg_color = COLOR_CUERPO_ALTERNATICA)
        self._fill_frame.pack(side = ctk.BOTTOM, expand = True, fill = ctk.BOTH)
        self._label_usuario = ctk.CTkLabel(self._fill_frame, text = "Usuario", font = ('Times', 14), fg_color = COLOR_PRIMITIVO_NEGRO,
                                           bg_color = COLOR_CUERPO_ALTERNATICA, anchor = "w")
        self._label_usuario.pack(fill = ctk.X, padx = 20, pady = 5)
        self._text_usuario = ctk.CTkEntry(self._fill_frame, font = ('Times', 14))
        self._text_usuario.pack(fill = ctk.X, padx = 20, pady = 10)
        self._label_clave = ctk.CTkLabel(self._fill_frame, text = "Contraseña", font = ('Times', 14), fg_color = COLOR_PRIMITIVO_NEGRO,
                                         bg_color = COLOR_CUERPO_ALTERNATICA, anchor = "w")
        self._label_clave.pack(fill = ctk.X, padx = 20, pady = 5)
        self._text_clave = ctk.CTkEntry(self._fill_frame, font = ('Times', 14))
        self._text_clave.pack(fill = ctk.X, padx = 20, pady = 10)
        self._text_clave.configure(show = "*")
        self._button_registrar = ctk.CTkButton(self._fill_frame, text = "Registrar", font = ('Times', 15), bg_color = COLOR_LOGIN_MARCA,
                                               fg_color = COLOR_CUERPO_PRINCIPAL)
        self._button_registrar.pack(fill = ctk.X, padx = 20, pady = 20)        