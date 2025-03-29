from customtkinter import CTk

class UtilVentana:
    @staticmethod
    def centrar_ventana(ventana: CTk, app_ancho, app_largo):
        screen_ancho = ventana.winfo_screenwidth()
        screen_largo = ventana.winfo_screenheight()
        x = int((screen_ancho / 2) - (app_ancho / 2))
        y = int((screen_largo / 2) - (app_largo / 2))
        return ventana.geometry(f"{app_ancho}x{app_largo}+{x}+{y}")
        