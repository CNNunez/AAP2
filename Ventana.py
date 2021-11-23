#libs
from population import *
from functions import *
from laberintos import *
from tkinter import *



# Funciones

#uploads laberinto
def load_img():
    # Get laberintos de prueba
    l = laberintos("IMGs",2)
    for i in range(10):
        l.evolve()


    #print results
    for i in range(l.length()):
        l.print(i)
        input()






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
can_inicial.place(x = 20, y = 125)

txt_inicial = Text(gui, height= 15,width= 50)
txt_inicial.pack()
txt_inicial.place(x = 20, y = 550)




#Canvas laberinto pasado
canvas.create_text(500, 20, fill="black", font="Verdana 15", text="Anterior")
can_anterior = Canvas(gui, bg='#678dce', width = w, height = h)
can_anterior.place(x = 450, y = 125)

txt_anterior = Text(gui, height= 15,width= 50)
txt_anterior.pack()
txt_anterior.place(x = 450, y = 550)




#Canvas laberinto actual
canvas.create_text(930, 20, fill="black", font="Verdana 15", text="Actual")
can_actual = Canvas(gui, bg='#9bccfc', width = w, height = h)
can_actual.place(x = 880, y = 125)

txt_actual = Text(gui, height= 15,width= 50)
txt_actual.pack()
txt_actual.place(x = 880, y = 550)






#Footer
nombre = IntVar()
nombre_img = Entry(gui, textvariable = nombre, width = "12", font = ("Arial", "12"), bg= "white")
nombre_img.place(x = 20, y = 25)

btn_load = Button(gui, text="Load", command = load_img(), width= "10", height= "1", bg= "#c0d6e4", font = "Arial 10", fg = "black")
btn_load.place(x = 150, y = 25 )


btn_load = Button(gui, text="STEP", command = None, width= "30", height= "2", bg= "#ffa6bb", font = "Arial 20", fg = "white")
btn_load.place(x = 400, y = 850 )



#Llamada al GUI
gui.mainloop()




































