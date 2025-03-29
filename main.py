from src.view.form_principal import FormPrincipalDesign
from src.view.form_login import FormLoginDesign
try:
    from urllib.request import urlopen, urlretrieve
    from PIL import Image, ImageTk
    import customtkinter as ctk
    import os
    import io
    import json
    import webbrowser
    import sys
    import pkg_resources
    import threading
except Exception as e:
    import os 
    os.system("pip install -r requirements.txt")

login = FormLoginDesign()
login.mainloop()    