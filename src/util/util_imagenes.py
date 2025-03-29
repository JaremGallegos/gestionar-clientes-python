from PIL import  ImageTk, Image

class UtilImagen:
    @staticmethod
    def leer_imagen(path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS))
