
from tkinter import *
from tkinter import ttk
import atributosGUI

def app():
    global root
    ##progressbar.stop()
    ##splash.destroy()
    root = Tk()
    #global user_sigint
    #global password_sigint
    #user_sigint=StringVar()
    #password_sigint=StringVar()
    #global entrada_user
    #global entrada_pass
    #global cur
    ###titulo de ventana
    root.title('RAPTOR V 1.0') 
    ####definiendo ventana
    screenWidth = root.winfo_screenwidth()  
    # Obtenga el alto del área de visualización
    screenHeight = root.winfo_screenheight()
    #tamaño automatico
    width = atributosGUI.ANCHO
    height = atributosGUI.ALTO
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2

    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
    root.configure(background=atributosGUI.COLOR)
    
    root.mainloop()
    

app()