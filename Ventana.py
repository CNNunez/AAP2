#libs
from population import *
from functions import *
from laberintos import *
from tkinter import *
from PIL import Image, ImageTk



# Funciones

#uploads laberinto
def load_img():
    # Get laberintos de prueba
    l = laberintos("IMGs",2)
    """
    for i in range(10):
        l.evolve()


    #print results
    for i in range(l.length()):
        l.print(i)
        input()
    """
        #path = os.path.dirname(os.path.realpath(__file__))+'\\Results\\Imagen' + str(100+position) + '.png'

def pruebaImg():
    LabImg= (PhotoImage(os.path.dirname(os.path.realpath(__file__))+'\\IMGs\\' + str(1) + '.png'))
    #imgLabP= (ImageTk.PhotoImage(file = "\\IMGs\\1.png"))

    #Resize the Image using resize method
#    resized_image= LabImg.resize((300,300), Image.ANTIALIAS)
 #   new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    can_inicial.create_image(50, 10, image=LabImg, anchor=NW)
    can_inicial.new_image = new_image

    #canvasLabFinP.create_image(0,0, anchor=NW, image = imgLabP)
    #canvasLabFinP.imgLabP = imgLabP



#VENTANA
gui = Tk()

# geometria
gui.geometry("1300x1000")
gui.resizable(False,False)

# aspecto

#Encabezado
gui.title("Analísis de Algoritmos - Caro y Nikko")
gui.config(background="#17253f")
titulo = Label(text = "Proyecto de Laberintos", bg = "#17253f", fg = "white", font = "Verdana 25")
titulo.pack(pady = 20)

#Cuerpo
canvas = Canvas(bg='#F2F1E7')
canvas.pack(expand=YES, fill=BOTH)


w = 400
h = 400

#Canvas laberinto inicial
canvas.create_text(60, 20, fill="black", font="Verdana 15", text="Inicial")
can_inicial = Canvas(gui, bg='#c4c4fc', width = w, height = h)
can_inicial.pack(expand=YES, fill=BOTH)
can_inicial.place(x = 20, y = 125)

'''
txt_inicial = Text(gui, height= 15,width= 50)
txt_inicial.pack()
txt_inicial.place(x = 20, y = 550)
'''



#Canvas laberinto pasado
canvas.create_text(500, 20, fill="black", font="Verdana 15", text="Anterior")
can_anterior = Canvas(gui, bg='#678dce', width = w, height = h)
can_anterior.place(x = 450, y = 125)

'''
txt_anterior = Text(gui, height= 15,width= 50)
txt_anterior.pack()
txt_anterior.place(x = 450, y = 550)
'''



#Canvas laberinto actual
canvas.create_text(930, 20, fill="black", font="Verdana 15", text="Actual")
can_actual = Canvas(gui, bg='#9bccfc', width = w, height = h)
can_actual.place(x = 880, y = 125)

'''
txt_actual = Text(gui, height= 15,width= 50)
txt_actual.pack()
txt_actual.place(x = 880, y = 550)
'''





#Footer
nombre = IntVar()
nombre_img = Entry(gui, textvariable = nombre, width = "12", font = ("Arial", "12"), bg= "white")
nombre_img.place(x = 200, y = 25)

btn_load = Button(gui, text="Load", command = pruebaImg(), width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_load.place(x = 150, y = 850 )


btn_exe = Button(gui, text="Execute", command = None, width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_exe.place(x = 400, y = 850 )

btn_next = Button(gui, text="Next Img", command = load_img(), width= "10", height= "2", bg= "#3B527E", font = "Arial 15", fg = "black")
btn_next.place(x = 650, y = 850 )




#Llamada al GUI
gui.mainloop()




































