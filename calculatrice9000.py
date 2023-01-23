from tkinter import *


caractère = ""

def touch(calculate):
    if touch == "=":
        calculate()
        return

    global caractère
    caractère += str(calculate)
    equation.set(caractère)


def calculate():
    try:
        global caractère
        total = str(eval(caractère))

        equation.set(total)
        caractère = total
    except:
        equation.set("error")
        caractère = ""


def delete():
    global caractère
    caractère = ""
    equation.set("")



if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="#101419")

    # the name of the application
    gui.title("Calculatrice")

    # the size of the window
    gui.geometry("270x392")

    # Variable for store the contents
    equation = StringVar()

    resultat = Label(gui, fg="#000000", textvariable=equation, height=2, width=38)
    resultat.grid(columnspan=7)

    bouton1=Button(gui,text="1",command=lambda :touch(1),font=('Arial',15),height=2,width=4)
    bouton1.grid(column=0 , row=5 )

    bouton2 = Button(gui, text="2", command=lambda :touch(2),font=('Arial',15),height=2,width=4)
    bouton2.grid(column=1 , row=5)

    bouton3 = Button(gui, text="3", command=lambda :touch(3),font=('Arial',15),height=2,width=4)
    bouton3.grid(column=2 , row=5)

    bouton4 = Button(gui, text="4", command=lambda :touch(4),font=('Arial',15),height=2,width=4)
    bouton4.grid(column=0 , row=3)

    bouton5 = Button(gui, text="5", command=lambda :touch(5),font=('Arial',15),height=2,width=4)
    bouton5.grid(column=1, row=3)

    bouton6 = Button(gui, text="6", command=lambda :touch(6),font=('Arial',15),height=2,width=4)
    bouton6.grid(column=2 , row=3)

    bouton7 = Button(gui, text="7", command=lambda :touch(7),font=('Arial',15),height=2,width=4)
    bouton7.grid(column=0, row=2)

    bouton8 = Button(gui, text="8", command=lambda :touch(8),font=('Arial',15),height=2,width=4)
    bouton8.grid(column=1 , row=2)

    bouton9 = Button(gui, text="9", command=lambda :touch(9),font=('Arial',15),height=2,width=4)
    bouton9.grid(column=2,row=2)

    bouton0 = Button(gui, text="0", command=lambda :touch(0),font=('Arial',15),height=2,width=4)
    bouton0.grid(column=1, row=6)

    boutonaddition = Button(gui, text="+", command=lambda :touch('+'),font=('Arial',15),height=2,width=4)
    boutonaddition.grid(column=3, row=5)

    boutonsoustraction= Button(gui, text="-", command=lambda :touch('-'),font=('Arial',15),height=2,width=4)
    boutonsoustraction.grid(column=3 , row=3)

    boutonmultiplication = Button(gui, text="x", command=lambda :touch('*'),font=('Arial',15),height=2,width=4)
    boutonmultiplication.grid(column=3 , row=2)

    boutondivision = Button(gui, text="/", command=lambda :touch('/'),font=('Arial',15),height=2,width=4)
    boutondivision.grid(column=4 , row=2)

    boutonracine = Button(gui, text="√", command=lambda :touch('**0.5'),font=('Arial',15),height=2,width=4)
    boutonracine.grid(column=4 , row=3)

    boutonp2 = Button(gui, text="²", command=lambda :touch('**2'),font=('Arial',15),height=2,width=4)
    boutonp2.grid(column=4 , row=5)

    boutonpoint = Button(gui, text=".", command=lambda :touch('.'), font=('Arial', 15), height=2, width=4)
    boutonpoint.grid(column=0, row=6)

    boutonégale = Button(gui, text="=", command=lambda :calculate(), font=('Arial', 15), height=2, width=4)
    boutonégale.grid(column=3 , row=6)

    boutonvide1 = Button(gui, text="", command='', font=('Arial', 15), height=2, width=4)
    boutonvide1.grid(column=4, row=6)

    boutonvide2 = Button(gui, text="", command='', font=('Arial', 15), height=2, width=4)
    boutonvide2.grid(column=2, row=6)

    boutondelete = Button(gui, text="delete", command=lambda :delete(), font=('Arial'), height=5, width=29)
    boutondelete.grid(columnspan=7)

    mainloop()