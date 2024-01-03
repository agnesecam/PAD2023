from archivio import *
import tkinter as tk
from tkinter import messagebox

class myApp:
    def __init__(self, root):
        self.root = root
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.root)
        contenitore1.pack()

        self.archivio = Archivio()
        # Creo alcuni studenti di esempio
        stud1 = Studente("Rossi", "Carlo", 345655, [('544MM', 30), ('564GG', 22)])
        stud2 = Studente("Bianchi", "Luigi", 123456, [])
        stud3 = Studente("Verdi", "Giulia", 987654, [('564GG', 18), ('241SS', 30), ('544MM', 26)])
        stud4 = Studente("Neri", "Giorgio", 789101, [('671IF', 25), ('410SS', 18), ('388LL', 29)])
        stud5 = Studente("Gialli", "Giorgio", 549245)
        # Popolo l'archivio
        self.archivio.inserisci(stud1, "nota1")
        self.archivio.inserisci(stud2, "nota2")
        self.archivio.inserisci(stud3, "nota3")
        self.archivio.inserisci(stud4, "nota4")
        self.archivio.inserisci(stud5, "nota5")

        # Creo i bottoni
        # Visualizza archivio
        self.pulsante_visualizzaArchivio = tk.Button(contenitore1, text="Visualizza archivio")
        self.pulsante_visualizzaArchivio.pack()
        self.pulsante_visualizzaArchivio.bind("<Button-1>", self.finestra_visualizza_archivio)
        # Inserisci studente
        self.pulsante_inserisciStudente = tk.Button(contenitore1, text="Inserisci studente")
        self.pulsante_inserisciStudente.pack()
        self.pulsante_inserisciStudente.bind("<Button-1>", self.finestra_inserisci_studente)

    ######### HANDLER ##########
    def finestra_visualizza_archivio(self, event):
        # Creo una nuova finestra per la visualizzazione dell'archivio
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Visualizza archivio")

        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)  
        contenitore1.pack()
        # Creo la textbox
        self.box_visualizzaArchivio = tk.Text(contenitore1, width=90, height=10)
        self.box_visualizzaArchivio.pack()
        self.box_visualizzaArchivio.delete("1.0", tk.END)
        self.box_visualizzaArchivio.insert(tk.END, str(self.archivio)) # Uso il metodo __str__ della classe Archivio in archivio.py

    def finestra_inserisci_studente(self, event):
        # Creo una nuova finestra per gestire l'inserimento di un nuovo studente
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Inserisci studente")
        self.dialog.geometry("400x300")
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)
        contenitore1.pack()
        # Creo le etichette per i campi di input
        label_cognome = tk.Label(contenitore1, text="Cognome")
        label_cognome.grid(row=0, column=0)
        label_nome = tk.Label(contenitore1, text="Nome")
        label_nome.grid(row=1, column=0)
        label_matricola = tk.Label(contenitore1, text="Matricola")
        label_matricola.grid(row=2, column=0)
        label_esami = tk.Label(contenitore1, text="Esami")
        label_esami.grid(row=3, column=0)
        label_note = tk.Label(contenitore1, text="Note")
        label_note.grid(row=4, column=0)
        # Creo i campi di input
        entry_cognome = tk.Entry(contenitore1, width=30)
        entry_cognome.grid(row=0, column=1)
        entry_nome = tk.Entry(contenitore1, width=30)
        entry_nome.grid(row=1, column=1)
        entry_matricola = tk.Entry(contenitore1, width=30)
        entry_matricola.grid(row=2, column=1)
        entry_esami = tk.Entry(contenitore1, width=30)
        entry_esami.grid(row=3, column=1)
        entry_note = tk.Entry(contenitore1, width=30)
        entry_note.grid(row=4, column=1)        
        # Creo il pulsante per l'inserimento
        pulsante_inserisci = tk.Button(contenitore1, text="Inserisci")
        pulsante_inserisci.grid(row=5, column=1)
        pulsante_inserisci.bind("<Button-1>", self.inserimento_studente)

    def inserimento_studente(self, event):
        # Prendo i dati in input
        cognome = self.entry_cognome.get()
        nome = self.entry_nome.get()
        matricola = self.entry_matricola.get()
        lista_esami = self.entry_esami.get()
        note = self.entry_note.get()
        # Creo un nuovo studente
        nuovo_studente = Studente(nome, cognome, matricola, lista_esami)
        self.archivio.inserisci(nuovo_studente, note)
        

root = tk.Tk()
app = myApp(root)
root.mainloop()
