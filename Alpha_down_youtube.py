from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox, ttk

print(os.getcwd())

def accion():
    enlace = videos.get()
    if enlace == "":
        MessageBox.showinfo("Falta Link","Debe ingresar el link del video para descargar;\nComo pretendes descargar sin poner el link????")
    else:
        video = YouTube(enlace)
        selection = combo.get()
        if selection=="Resolución ALTA":
            descarga = video.streams.get_highest_resolution()
        if selection=="Resolución BAJA":
            descarga = video.streams.get_lowest_resolution()
        if selection=="Solo AUDIO":
            descarga = video.streams.get_audio_only()
        descarga.download()
#        boton["state"] = DISABLED
        
def popup():
    MessageBox.showinfo("Sobre mi","Enlace a mi perfil de Linkedin;\nhttps://www.linkedin.com/in/adriánalbertoauvieux/")
    
root = Tk()
root.config(bd=15)
root.geometry("590x310")
root.configure(bg="red")
root.title("Descarga tu video favorito")
root.iconbitmap('./issets/youtube.ico')

bg = PhotoImage(file = "./issets/fondo1.png")
foto = Label( root, image = bg,)
foto.place(x = 0, y = 0)

#imagen = PhotoImage(file="./issets/fondo.png")
#foto = Label(root, image=imagen, bd=0)
#foto.grid(row=0, column=0)

root.wm_attributes('-transparentcolor', '#ab23ff')

#Create a Label
Label(root, text= "Ingresa el link del video", fg='white',font= ('Helvetica 10'), bg= 'red3').place(x=230,y=77)
#'#ab23ff'

#text = StringVar()
#text.set("Test")
#down_text = Label(root, text="T", fg='white',font= ('Helvetica 20'), bg= 'red3').place(x=300,y=190)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label="Para mas información", menu=helpmenu)
helpmenu.add_cascade(label="Información del autor", command=popup)

menubar.add_command(label="Salir", command=root.destroy)

#instrucciones = Label(root, text="Programa para descargar tus videos favoritos\n")
#instrucciones.grid(row=0,column=1)

videos = Entry(root,width=50)
videos.place(x=230,y=100)

combo = ttk.Combobox(state="readonly",values=["Resolución ALTA", "Resolución BAJA", "Solo AUDIO"])
combo.current(0)
combo.place(x=230, y=130)

boton = Button(root, text="Descargar", command=accion)
boton.place(x=350,y=160)

root.mainloop()

