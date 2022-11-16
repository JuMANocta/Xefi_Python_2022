from tkinter import *
from Controller import nbcars_nbplacesvides

class Gui_probleme:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("200x200")
        self.frame = Frame(parent)
        self.interfaceGUI()
        self.packGUI()

    def interfaceGUI(self):
        self.labNbEleves = Label(self.frame, text="Nombre d'élèves")
        self.enNbEleves = Entry(self.frame)
        self.labNbAdultes = Label(self.frame, text="Nombre d'adultes")
        self.enNbAdultes = Entry(self.frame)
        self.labNbPlacesCars = Label(self.frame, text="Nombre de places par cars")
        self.enNbPlacesCars = Entry(self.frame)
        self.retourBtn = Button(self.frame, text="Calcul", command=self.calcul)
        self.labNbCars = Label(self.frame, text="Nombre de cars")

    def packGUI(self):
        self.frame.pack()
        self.labNbEleves.pack()
        self.enNbEleves.pack()
        self.labNbAdultes.pack()
        self.enNbAdultes.pack()
        self.labNbPlacesCars.pack()
        self.enNbPlacesCars.pack()
        self.retourBtn.pack()
        self.labNbCars.pack()

    def calcul(self):
        try:
            nb_eleves = int(self.enNbEleves.get())
            nb_adultes = int(self.enNbAdultes.get())
            nb_places = int(self.enNbPlacesCars.get())
            self.labNbCars.config(text=nbcars_nbplacesvides.NbCars_nbPlacesVides(nb_eleves,nb_adultes,nb_places), fg="green")
        except:
            self.labNbCars.config(text="Erreur de saisie", fg="red")
