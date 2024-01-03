'''
[x] visualizzare il contenuto del archivio,
[  ] inserire un nuovo studente nell'archivio,
[  ] modificare i dati di uno studente,

[  ] cancellare uno studente dall'archivio,
[  ] calcolare la media dei voti di uno studente,
[  ] caricare l'archivio da file,
[  ] salvare l'archivio su file,
[  ] uscire dall'applicazione.
'''


from archivio import *
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import sys

# Dato che l'inserimento degli esami per la registrazione di un nuovo studente richiede che gli esami siano inseriti in un formato specifico, ho deciso di creare una casella di testo con un placeholder che mostra un esempio di come inserire gli esami.
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', placeholder_color='grey', width=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        if width is not None:
            self.config(width=width)

        self.put_placeholder()


    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color


    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color


    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()




class ConsoleRedirector:
    def __init__(self, textbox):
        self.textbox = textbox


    def write(self, text):
        self.textbox.insert(tk.END, text)
        self.textbox.see(tk.END)  # Scorrimento automatico alla fine del testo


    def flush(self):
        pass

class InserisciStudenteDialog:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.dialog = tk.Toplevel(root)
        self.dialog.title("Inserisci Studente")

        # Etichette
        tk.Label(self.dialog, text="Cognome:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(self.dialog, text="Nome:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(self.dialog, text="Matricola:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(self.dialog, text="Esami:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        # Campi di testo
        self.entry_cognome = tk.Entry(self.dialog, width=60)
        self.entry_cognome.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.dialog, width=60)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)
        self.entry_matricola = tk.Entry(self.dialog, width=60)
        self.entry_matricola.grid(row=2, column=1, padx=5, pady=5)
        self.entry_esami = EntryWithPlaceholder(self.dialog, placeholder="Scrivere gli esami nel formato 544MM-30, 564GG-22, 241SS-25...",  placeholder_color='grey', width=60)
        self.entry_esami.grid(row=3, column=1, padx=5, pady=5)
        # Pulsante per inserire lo studente
        tk.Button(self.dialog, text="Inserisci", command=self.inserisci_studente).grid(row=9, column=0, columnspan=2, pady=10)


    def inserisci_studente(self):
        cognome = self.entry_cognome.get()
        nome = self.entry_nome.get()
        matricola = self.entry_matricola.get()
        #Se la matricola non è un numero intero il sistema prova a convertirla in un numero intero e se non ci riesce solleva un'eccezione
        try:
            matricola = int(matricola)
        except ValueError: 
            messagebox.showerror("Errore", "La matricola deve essere un numero intero positivo.")
            return
        if matricola <= 0:
            messagebox.showerror("Errore", "La matricola deve essere un numero intero positivo.")
            return

        esami_input = self.entry_esami.get()
        esami = []
        #Se l'utente ha inserito deli esami
        if not (esami_input is None or esami_input == "" or esami_input == self.entry_esami.placeholder): #Dato che ho inserito i placeholder devo considerare che esami_input non sia proprio vuoto, ma che sia uguale al placeholder
            for esame in esami_input.split(','):
                esame = esame.strip().split('-')
                if esame and len(esame) == 2:
                    codice, voto = esame
                    voto = int(voto)
                    if not (18 <= voto <= 33):
                        messagebox.showerror("Errore", "Il voto deve essere un numero intero compreso tra 18 e 33.")
                        return
                    esami.append((codice, voto))
                else:
                    messagebox.showerror("Errore", "Formato esami non valido.")
                    return
            
        nuovo_studente = Studente(cognome, nome, matricola, esami)
        self.callback(nuovo_studente, esami_input)
        self.dialog.destroy()



class myApp:
    def __init__(self, root):
        self.root = root
        self.archivio = Archivio()

        # Creo alcuni studenti di esempio
        stud1 = Studente("Rossi", "Carlo", 345655, [('544MM', 30), ('564GG', 22)])
        stud2 = Studente("Bianchi", "Luigi", 123456, [])
        stud3 = Studente("Verdi", "Giulia", 987654, [('564GG', 18), ('241SS', 30), ('544MM', 26)])
        stud4 = Studente("Neri", "Giorgio", 789101, [('671IF', 25), ('410SS', 18), ('388LL', 29)])
        stud5 = Studente("Gialli", "Giorgio", 549245)

        self.archivio.inserisci(stud1, "nota1")
        self.archivio.inserisci(stud2, "nota2")
        self.archivio.inserisci(stud3, "nota3")
        self.archivio.inserisci(stud4, "nota4")
        self.archivio.inserisci(stud5, "nota5")

        # Creo il frame contenitore
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Creo i bottoni
        # Visualizza archivio
        self.button_visualizzaArchivio = tk.Button(self.frame, text="Visualizza archivio", command=self.handle_bottone_visualizzaArchivio)
        self.button_visualizzaArchivio.pack()

        # Inserisci studente
        self.button_inserisciStudente = tk.Button(self.frame, text="Inserisci studente", command=self.mostra_finestra_inserisci_studente)
        self.button_inserisciStudente.pack()

        # Creo la textbox
        self.box_visualizzaArchivio = tk.Text(self.frame, width=90, height=10)
        self.box_visualizzaArchivio.pack()

        # Creare la textbox per l'output della console
        self.console_output = scrolledtext.ScrolledText(self.frame, width=90, height=10)
        self.console_output.pack()

        # Redirect dell'output della console alla textbox
        sys.stdout = ConsoleRedirector(self.console_output)
        sys.stderr = ConsoleRedirector(self.console_output)

    def get_archivio_str(self):
        return str(self.archivio)

    def handle_bottone_visualizzaArchivio(self):
        archivio_str = self.get_archivio_str()
        self.box_visualizzaArchivio.delete("1.0", tk.END)
        self.box_visualizzaArchivio.insert(tk.END, archivio_str)

    def mostra_finestra_inserisci_studente(self):
        InserisciStudenteDialog(self.root, self.inserisci_studente_callback)

    def inserisci_studente_callback(self, studente, esami_input):
        lunghezza_archivio_prima = self.archivio.lunghezza_archivio()
        # Aggiungi lo studente all'archivio
        self.archivio.inserisci(studente, "")
        lunghezza_archivio_dopo = self.archivio.lunghezza_archivio()
        if lunghezza_archivio_dopo == lunghezza_archivio_prima:
            messagebox.showerror("Inserimento studente", "Impossibile aggiungere lo studente, controllare la correttezza dei campi.")
        elif lunghezza_archivio_dopo == lunghezza_archivio_prima + 1:
            messagebox.showinfo("Inserimento studente", "Studente inserito.")

root = tk.Tk()
app = myApp(root)
root.mainloop()
