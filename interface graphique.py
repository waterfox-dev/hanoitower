import tkinter
from tkinter.constants import BOTTOM, GROOVE, LEFT, RIGHT

def quitter():
    ma_fenetre.destroy()

def tracer_piquet():
    piquet_1 = canvas.create_rectangle(262, 256, 312, 511)
    piquet_2 = canvas.create_rectangle(536, 256, 586, 511)
    piquet_3 = canvas.create_rectangle(823, 256, 873, 511)

def tracer_disque(n):
    tracer_piquet()
    largeur_petit_disque = L = 75
    hauteur_petit_disque = H = 15
    if n > 10:
        label_1 = label_nbre_disques = tkinter.Label(Frame2, text = 'Le nombre doit être inférieur ou égal à 10')
        label_1.pack()
    else:
        for i in range(1, n + 1):
            Disque = canvas.create_rectangle(287+L/2, 511-(n-i)*H, 287-L/2, 511-(n-i+1)*H)
            L += L/(2*i)
#pour tracer : Ymin = 12 et Ymax = 511, Xmin = 12 et Xmax = 1111


ma_fenetre = tkinter.Tk()
ma_fenetre.title("Tour d'Hanoi")

#Frame
Frame1 = tkinter.Frame(ma_fenetre, borderwidth = 2, relief = GROOVE)
Frame1.pack(side=BOTTOM, padx=0, pady=10)

Frame2 = tkinter.Frame(ma_fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=RIGHT, padx=10, pady=0)

#Canevas
canvas = tkinter.Canvas(ma_fenetre, height=500, width=1100, bd=10, bg='ivory')
canvas.pack()

#Label
label_1 = label_nbre_disques = tkinter.Label(Frame2, text = 'saisir le nombre de disques')
label_1.pack()

#Entrée
value = tkinter.StringVar()
value.set("0")
saisie = tkinter.Entry(Frame2,textvariable=value, width=5, justify='center', bd=3)
saisie.pack()

#Boutons
bouton_1 = tkinter.Button(Frame1, text='Quitter', command=quitter)
bouton_1.pack(side=LEFT, padx=5, pady=5)

a = saisie.get()
bouton_2 = tkinter.Button(Frame1, text='Jouer', command=tracer_disque(int(a)))
bouton_2.pack(side=RIGHT, padx=5, pady=5)


ma_fenetre.mainloop()
