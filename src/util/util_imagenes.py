from PIL import  ImageTk, Image

class UtilImagen:
    def leer_imagen(path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))
