import csv
from tkinter import messagebox
class Stagiaire :
    lt=[]
    def __init__(self,id,name,emai,groupe):
        self._id=id
        self._name = name
        self._emai = emai
        if groupe =="Selectionner" :
            self._groupe = "Groupe non séléctioné"
        else:
            self._groupe = groupe

    def setName(self,new):
        self._name = new

    def setEmail(self,new):
        self._emai = new

    def setGroupe(self,new):
        self._groupe = new

    def ajouter(self,obj):
        Stagiaire.lt.append(obj)
        Stagiaire.EnregistrerCSV()
        Stagiaire.lt.clear()

    @classmethod
    def afficher(cls, table):
        table.delete(*table.get_children())
        for i in Stagiaire.lt:
            table.insert('', "end", values=(i._id, i._name, i._emai, i._groupe))

    @classmethod
    def supprimer(cls, id):
        with open('stagiaire.csv', 'r+') as file:
            reader = csv.reader(file, delimiter=";")
            l = []
            for i in reader :
                l.append(i)
            for i in l :
                if i[0] == str(id):
                    l.remove(i)
        with open("stagiaire.csv", "w+", newline="") as f:
            file = csv.writer(f, delimiter=";")
            for i in l:
                file.writerow([i[0], i[1], i[2], i[3]])




    @classmethod
    def EnregistrerCSV(cls):
        with open("stagiaire.csv", "a+", newline="") as f:
            file = csv.writer(f, delimiter=";")
            for i in Stagiaire.lt:
                file.writerow([i._id, i._name, i._emai, i._groupe])

    @classmethod
    def rechercher(cls, table, id):
        table.delete(*table.get_children())
        found = False
        with open('stagiaire.csv', 'r+') as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader :
                if i[0] == id :
                    table.insert('', "end", values=(i[0], i[1], i[2], i[3]))
                    found = True

        if found :
            messagebox.showinfo("Succes", "Stagiaire trouvé")
        else:
            messagebox.showwarning("Avertissement", "Aucun stagiaire trouvé.")

    @classmethod
    def modofier(cls,l, id,name,emai,groupe):
        for i in l:
            if i[0] == id:
                i[1] = name
                i[2] = emai
                i[3] = groupe

        with open("stagiaire.csv", "w+", newline="") as f:
            file = csv.writer(f, delimiter=";")
            for i in l:
                file.writerow([i[0], i[1], i[2], i[3]])


    @classmethod
    def modifierCSV(cls,id,name,emai,groupe):
        with open('stagiaire.csv', 'r+') as file:
            reader = csv.reader(file, delimiter=";")
            l = []
            for i in reader :
                l.append(i)
            Stagiaire.modofier(l,id,name,emai,groupe)

    @classmethod
    def Supprimer(cls,table):
        it = table.item(table.selection())
        value=it['values'][0]
        Stagiaire.supprimer(int(value))
        if table.selection():
            for item in table.selection():
                table.delete(item)

        else:
            messagebox.showwarning("Avertissement", "Aucune ligne sélectionnée.")

    @classmethod
    def afficherCSV(cls, table):
        table.delete(*table.get_children())
        with open('stagiaire.csv', 'r') as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                table.insert('', "end", values=(i[0], i[1], i[2], i[3]))

