#libs
from population import *
from functions import *
from laberintos import *
from tkinter import *
from PIL import Image, ImageTk



# Funciones


#VENTANA
gui = Tk()

laberinto = 0
cantNext = 1

# geometria
gui.geometry("960x640")
gui.config(background="#8C919A")
gui.resizable(False,False)

# aspecto

#Encabezado
gui.title("Analísis de Algoritmos - Caro y Nikko")
gui.config(background="#17253f")
titulo = Label(text = "Proyecto de Laberintos", bg = "#17253f", fg = "white", font = "Verdana 25")
titulo.pack(pady = 20)

#Cuerpo
canvas = Canvas(bg='#8C919A')
canvas.pack(expand=YES, fill=BOTH)


w = 300
h = 300

#Canvas laberinto inicial
canvas.create_text(60, 20, fill="black", font="Verdana 15", text="Inicial")
can_inicial = Canvas(gui, bg='#c4c4fc', width = w, height = h)
can_inicial.place(x = 10, y = 125)

'''
txt_inicial = Text(gui, height= 15,width= 50)
txt_inicial.pack()
txt_inicial.place(x = 20, y = 550)
'''



#Canvas laberinto pasado
canvas.create_text(400, 20, fill="black", font="Verdana 15", text="Anterior")
can_anterior = Canvas(gui, bg='#678dce', width = w, height = h)
can_anterior.place(x = 330, y = 125)

'''
txt_anterior = Text(gui, height= 15,width= 50)
txt_anterior.pack()
txt_anterior.place(x = 450, y = 550)
'''



#Canvas laberinto actual
canvas.create_text(700, 20, fill="black", font="Verdana 15", text="Actual")
can_actual = Canvas(gui, bg='#9bccfc', width = w, height = h)
can_actual.place(x = 650, y = 125)

'''
txt_actual = Text(gui, height= 15,width= 50)
txt_actual.pack()
txt_actual.place(x = 880, y = 550)
'''





#Footer
nombre = IntVar()
nombre_img = Entry(gui, textvariable = nombre, width = "12", font = ("Arial", "12"), bg= "white")
nombre_img.place(x = 170, y = 450)
nombre_lbl = Label (gui, text="Dificultad de Laberinto",font = ("Arial", "10"))
nombre_lbl.place(x = 10, y = 450)

cant_gene = IntVar()
cant_gene_img = Entry(gui, textvariable = cant_gene, width = "12", font = ("Arial", "12"), bg= "white")
cant_gene_img.place(x = 170, y = 475)
cant_gene_lbl = Label (gui, text="Cantidad de generaciones",font = ("Arial", "10"))
cant_gene_lbl.place(x = 10, y = 475)

cant_indivi = IntVar()
cant_indivi_img  = Entry(gui, textvariable = cant_indivi, width = "12", font = ("Arial", "12"), bg= "white")
cant_indivi_img.place(x = 170, y = 500)
cant_indivie_lbl = Label (gui, text="Cantidad de individuos",font = ("Arial", "10"))
cant_indivie_lbl.place(x = 10, y = 500)


def loadLab():
    LabImg= (Image.open("IMGs\\"+str(nombre.get())+".png"))

    #Resize the Image using resize method
    resized_image= LabImg.resize((w,h), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    can_inicial.create_image(0,0, anchor=NW, image=new_image)
    can_inicial.new_image = new_image

    btn_next.place_forget()

def exe_code():
    # Get laberintos de prueba
    lab = nombre.get()
    cantGene = cant_gene.get()
    cantIndi = cant_indivi.get()
    laberinto = laberintos("IMGs",lab,cantIndi)
    
    for i in range(cantGene):
        laberinto.evolve(i+1)

    btn_next.place(x = 650, y = 550 )

def nextImg():
    global cantNext
    LabImg= (Image.open("Results\\Imagen"+str(cantNext)+".png"))

    #Resize the Image using resize method
    resized_image= LabImg.resize((w,h), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    can_actual.create_image(0,0, anchor=NW, image=new_image)
    can_actual.new_image = new_image

    if cantNext >= 1:
        LabImg2= (Image.open("Results\\Imagen"+str(cantNext-1)+".png"))

        #Resize the Image using resize method
        resized_image= LabImg2.resize((w,h), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)

        #Add image to the Canvas Items
        can_anterior.create_image(0,0, anchor=NW, image=new_image)
        can_anterior.new_image = new_image

    if cantNext == cant_gene.get():
        btn_next.place_forget()
    else:
        cantNext = cantNext + 1

#BOTONES
btn_load = Button(gui, text="Load", command = loadLab, width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_load.place(x = 150, y = 550 )


btn_exe = Button(gui, text="Execute", command = exe_code, width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_exe.place(x = 400, y = 550 )

btn_next = Button(gui, text="Next Img", command = nextImg, width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_next.place(x = 650, y = 550 )





#Llamada al GUI
gui.mainloop()