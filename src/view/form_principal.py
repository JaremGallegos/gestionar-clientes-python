from customtkinter import CTkFont
from src.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
from src.util.util_ventana import UtilVentana as util_ventana
from src.util.util_imagenes import UtilImagen as util_imagen
import customtkinter as ctk

ctk.set_appearance_mode("System")

class FormPrincipalDesign(ctk.CTk):    
    def __init__(self):
        super().__init__()
        self._logo = util_imagen.leer_imagen("./assets/logo.jpg", (560, 136))
        self._perfil = util_imagen.leer_imagen("./assets/perfil.png", (100, 100))
        self.config_window()
        self.form_paneles()
        self.form_controles_barra_superior()
        self.form_controles_barra_lateral()
        self.form_controles_cuerpo()
    
    def config_window(self):
        self.title("Dashboard")
        self.iconbitmap("./assets/logoing.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)
        
    def form_paneles(self):
        self._barra_superior = ctk.CTkFrame(self, bg_color = COLOR_BARRA_SUPERIOR, fg_color = COLOR_BARRA_SUPERIOR, height = 50)
        self._barra_superior.pack(side = ctk.TOP, fill = 'both')
        self._menu_lateral = ctk.CTkFrame(self, bg_color = COLOR_MENU_LATERAL, fg_color = COLOR_MENU_LATERAL, width = 150)
        self._menu_lateral.pack(side = ctk.LEFT, fill = 'both', expand = False)
        self._cuerpo_principal = ctk.CTkFrame(self, bg_color = COLOR_CUERPO_PRINCIPAL, fg_color = COLOR_CUERPO_PRINCIPAL, width = 150)
        self._cuerpo_principal.pack(side = ctk.RIGHT, fill = 'both', expand = True)
        
    def form_controles_barra_superior(self):
        font_awesome = CTkFont(family = 'FontAwesome', size = 12)
        self._button_menu_lateral = ctk.CTkButton(self._barra_superior, text = "\uf0c9", font = font_awesome, bg_color = COLOR_BARRA_SUPERIOR, 
                                                  command = self.panel_toggle, text_color = "#fff", fg_color = COLOR_BARRA_SUPERIOR, width = 10)
        self._button_menu_lateral.pack(side = ctk.LEFT)
        self._label_titulo = ctk.CTkLabel(self._barra_superior, text = "Autodidacta")
        self._label_titulo.configure(fg_color = COLOR_BARRA_SUPERIOR, font = ("Roboto", 15), bg_color = "#fff", pady = 10, padx = 2, width = 12)
        self._label_titulo.pack(side = ctk.LEFT)
        self._label_titulo = ctk.CTkLabel(self._barra_superior, text = "73142526@continental.edu.pe")
        self._label_titulo.configure(fg_color = COLOR_BARRA_SUPERIOR, font = ("Roboto", 10), bg_color = "#fff", padx = 10, width = 20)
        self._label_titulo.pack(side = ctk.RIGHT)
    
    def form_controles_barra_lateral(self):
        font_awesome = CTkFont(family = 'FontAwesome', size = 15)
        ancho, alto = 20, 2
        self._label_perfil = ctk.CTkLabel(self._menu_lateral, image = self._perfil, bg_color = COLOR_MENU_LATERAL, fg_color = COLOR_MENU_LATERAL, text = "")
        self._label_perfil.pack(side = ctk.TOP, pady = 10)
        self._button_dashboard = ctk.CTkButton(self._menu_lateral)
        self._button_profile = ctk.CTkButton(self._menu_lateral)
        self._button_picture = ctk.CTkButton(self._menu_lateral)
        self._button_info = ctk.CTkButton(self._menu_lateral)
        self._button_settings = ctk.CTkButton(self._menu_lateral)
        
        _buttons_info = [
            ("Dahsboard", "\uf109", self._button_dashboard),
            ("Profile", "\uf007", self._button_profile),
            ("Picture", "\uf03e", self._button_picture),
            ("Info", "\uf129", self._button_info),
            ("Settings", "\uf013", self._button_settings),
        ]
        
        for text, icon, button in _buttons_info:
            self.confi_button_menu(button, text, icon, font_awesome, ancho, alto)
    
    def form_controles_cuerpo(self):
        label = ctk.CTkLabel(self._cuerpo_principal, image = self._logo, bg_color = COLOR_CUERPO_PRINCIPAL)
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    def confi_button_menu(self, button: ctk.CTkButton, text, icon, font_awesome, ancho, alto):
        button.configure(text = f" {icon}  {text}",  anchor = "w", font = font_awesome,
                        bg_color = COLOR_MENU_LATERAL, fg_color = COLOR_MENU_LATERAL)
        button.pack(side = ctk.TOP)
        self.event_hover_bind(button)
    
    def event_hover_bind(self, button: ctk.CTkButton):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
        
    def on_enter(self, event, button: ctk.CTkButton):
        button.configure(bg_color = COLOR_MENU_CURSOR_ENCIMA, fg_color = COLOR_MENU_CURSOR_ENCIMA, text_color = "#fff", corner_radius = 0)
    
    def on_leave(self, event, button: ctk.CTkButton):
        button.configure(bg_color = COLOR_MENU_LATERAL, fg_color = COLOR_MENU_LATERAL, text_color = "#fff", corner_radius = 0)
        
    def panel_toggle(self):
        if self._menu_lateral.winfo_ismapped():
            self._menu_lateral.pack_forget()
        else:
            self._menu_lateral.pack(side = ctk.LEFT, fill = 'y')