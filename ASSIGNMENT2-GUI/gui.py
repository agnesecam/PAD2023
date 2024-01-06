'''
[x] visualizzare il contenuto del archivio,
[x] inserire un nuovo studente nell'archivio,
[x] modificare i dati di uno studente,

[  ] cancellare uno studente dall'archivio,
[  ] calcolare la media dei voti di uno studente,
[  ] caricare l'archivio da file,
[  ] salvare l'archivio su file,
[  ] uscire dall'applicazione.
'''

from archivio import *
import tkinter as tk
from tkinter import messagebox
import re 

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
        self.pulsante_visualizzaArchivio.grid(row=0, column=0)
        self.pulsante_visualizzaArchivio.bind("<Button-1>", self.finestra_visualizza_archivio)
        # Inserisci studente
        self.pulsante_inserisciStudente = tk.Button(contenitore1, text="Inserisci studente")
        self.pulsante_inserisciStudente.grid(row=1, column=0)
        self.pulsante_inserisciStudente.bind("<Button-1>", self.finestra_inserisci_studente)
        # Modifica studente
        self.pulsante_modificaStudente = tk.Button(contenitore1, text="Modifica studente")
        self.pulsante_modificaStudente.grid(row=2, column=0)
        self.entry_matricola_modificaStudente = tk.Entry(contenitore1, width=20)
        self.entry_matricola_modificaStudente.grid(row=2, column=1)
        self.pulsante_modificaStudente.bind("<Button-1>", self.on_pulsante_modificaStudente) #on_pulsante_modificaStudente serve a passare il valore della matricola da modificare

    def contiene_solo_caratteri(self, campo, caratteri_validi, etichetta):
        pattern = "^[{}]+$".format(re.escape(caratteri_validi))
        if (re.match(pattern, campo)):
            return True
        else:
            messagebox.showerror("Errore", "Il campo " + str(etichetta) + " deve contenere solo questi caratteri: " + str(caratteri_validi))
            return 
        


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
        self.label_cognome = tk.Label(contenitore1, text="Cognome")
        self.label_cognome.grid(row=0, column=0)
        self.label_nome = tk.Label(contenitore1, text="Nome")
        self.label_nome.grid(row=1, column=0)
        self.label_matricola = tk.Label(contenitore1, text="Matricola")
        self.label_matricola.grid(row=2, column=0)
        self.label_esami = tk.Label(contenitore1, text="Esami")
        self.label_esami.grid(row=3, column=0)
        self.label_note = tk.Label(contenitore1, text="Note")
        self.label_note.grid(row=4, column=0)
        # Creo i campi di input
        self.entry_cognome = tk.Entry(contenitore1, width=50)
        self.entry_cognome.grid(row=0, column=1)
        self.entry_nome = tk.Entry(contenitore1, width=50)
        self.entry_nome.grid(row=1, column=1)
        self.entry_matricola = tk.Entry(contenitore1, width=50)
        self.entry_matricola.grid(row=2, column=1)
        self.entry_esami = EntryWithPlaceholder(contenitore1, placeholder="Nel formato 544MM-30, 564GG-22, 241SS-25...",  placeholder_color='grey', width=50) # Inserire gli esami nel campo nel formato CODICE-VOTO, separati da virgola e spazio
        self.entry_esami.grid(row=3, column=1)
        self.entry_note = tk.Entry(contenitore1, width=50)
        self.entry_note.grid(row=4, column=1)        
        # Creo il pulsante per l'inserimento
        pulsante_inserisci = tk.Button(contenitore1, text="Inserisci")
        pulsante_inserisci.grid(row=5, column=1)
        pulsante_inserisci.bind("<Button-1>", self.inserimento_studente)

    def inserimento_studente(self, event):
        # Variabile per controllare sia avvenuto l'effettivo inserimento
        lunghezza_archivio = len(self.archivio.stud)

        # Prendo i dati in input
        cognome = self.entry_cognome.get()
        nome = self.entry_nome.get()
        matricola = self.entry_matricola.get()
        input_esami = self.entry_esami.get()
        lista_esami = []
        note = self.entry_note.get()

        #Caratteri ammessi nei campi
        lettere_base = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        lettere_accentate = "éèòçàùìÉÈÒÇÀÙÌ"
        lettere = lettere_base + lettere_accentate
        chars_nomecognome = lettere + " " + "'"
        numeri = "1234567890"
        
        # Controllo che i caratteri inseriti nei campi siano adeguati (solo lettere per nome e cognome, solo numeri per la matricola)
        if self.contiene_solo_caratteri(cognome, chars_nomecognome, "cognome") and self.contiene_solo_caratteri(nome, chars_nomecognome, "nome") and self.contiene_solo_caratteri(matricola, numeri, "matricola"):
            # Se il campo esami non è stato completato lista_esami rimane una lista vuota
            if not (input_esami is None or input_esami == "" or input_esami == self.entry_esami.placeholder): #Dato che ho inserito i placeholder devo considerare che esami_input sia uguale al placeholder            
                # Estrapolo il codice e il voto di ciascun esame inserito nel campo, e li aggiungo come tupla alla lista_esami
                for esame in input_esami.split(','):
                        esame = esame.strip().split('-')
                        if esame and len(esame) == 2:
                            codice, voto = esame
                            voto = int(voto)
                            lista_esami.append((codice, voto))
                        else:
                            messagebox.showerror("Errore", "Inserire gli esami nel formato CODICE-VOTO, separati da virgola e spazio. Es: 544MM-30, 564GG-22, 241SS-25")
                            return # Esco dalla funzione inserimento_studente altrimenti lo studente viene inserito con esami vuoti
            
            # Creo un nuovo studente di esempio per poter usare i metodi setter
            nuovo_studente = Studente("Nuovo", "Studente", 999999, [])
            nuovo_studente.set_cognome(cognome) # Il cognome e il nome saranno una stringa perché l'inserimento avviene tramite un campo di testo, quindi devo usare un controllo sui caratteri inseriti nella stringa (contiene_solo_caratteri)
            nuovo_studente.set_nome(nome)
            nuovo_studente.set_matricola(int(matricola))
            nuovo_studente.set_listaesami(lista_esami)
            # Inserisco lo studente nell'archivio assieme alle note 
            self.archivio.inserisci(nuovo_studente, note)

        # Controllo se l'inserimento è avvenuto
        if len(self.archivio.stud) > lunghezza_archivio:
            messagebox.showinfo("Inserimento avvenuto", "Lo studente è stato inserito correttamente.")
        else:
            messagebox.showerror("Errore", "Lo studente non è stato inserito: riferirsi alla console per maggiori informazioni.")

    def on_pulsante_modificaStudente(self, event):
        matricola = self.entry_matricola_modificaStudente.get()
        if matricola is None or matricola == "":
            messagebox.showerror("Errore", "Inserire la matricola dello studente da modificare.")
            return
        elif not (int(matricola) in self.archivio.get_studenti()):
            messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
            return
        # Eseguo la funzione di modifica, passando il valore dell'entry come parametro
        self.finestra_modifica_studente(int(matricola))

    def finestra_modifica_studente(self, matricola):
        # Creo una nuova finestra per gestire l'inserimento di un nuovo studente
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Modifica studente con matricola " + str(matricola))
        self.dialog.geometry("400x300")
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)
        contenitore1.pack()

        # Recupero i vecchi dati dello studente
        if matricola in self.archivio.get_studenti():
            cognome_vecchio = self.archivio.studente(matricola).get_cognome()
            nome_vecchio = self.archivio.studente(matricola).get_nome()
            esami_vecchi = self.archivio.studente(matricola).get_listaesami()
            note_vecchie = self.archivio.get_note(matricola)
        else:
            messagebox.showerror("Errore", "La matricola inserita non è presente nell'archivio.")
            return
        
        # Creo le label per i campi di input
        self.label_cognome_nuovo = tk.Label(contenitore1, text="Cognome")
        self.label_cognome_nuovo.grid(row=0, column=0)
        self.label_nome_nuovo = tk.Label(contenitore1, text="Nome")
        self.label_nome_nuovo.grid(row=1, column=0)
        self.label_matricola = tk.Label(contenitore1, text="Matricola")
        self.label_matricola.grid(row=2, column=0)
        self.label_esami_nuovi = tk.Label(contenitore1, text="Esami")
        self.label_esami_nuovi.grid(row=3, column=0)
        self.label_note_nuove = tk.Label(contenitore1, text="Note")
        self.label_note_nuove.grid(row=4, column=0)
        # Creo i campi di input
        self.entry_cognome = tk.Entry(contenitore1, width=50)
        self.entry_cognome.grid(row=0, column=1)
        self.entry_cognome.delete(0, tk.END)
        self.entry_cognome.insert(0, cognome_vecchio)
        self.entry_nome = tk.Entry(contenitore1, width=50)
        self.entry_nome.grid(row=1, column=1)
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, nome_vecchio)
        self.entry_esami = tk.Entry(contenitore1, width=50)
        self.entry_esami.grid(row=3, column=1)
        self.entry_esami.delete(0, tk.END)
        self.entry_esami.insert(0, str(esami_vecchi))
        self.entry_note = tk.Entry(contenitore1, width=50)            
        self.entry_note.grid(row=4, column=1)
        self.entry_note.delete(0, tk.END)
        self.entry_note.insert(0, note_vecchie)         
        #La matricola non sarà modificabile, quindi uso una casella di testo con lo stato disabilitato
        self.readOnlyText = tk.Text(contenitore1, width=37, height=1)
        self.readOnlyText.insert(1.0, matricola)
        self.readOnlyText.configure(state="disabled")
        self.readOnlyText.grid(row=2, column=1)

        # Creo il pulsante per l'inserimento
        pulsante_salva_modifiche = tk.Button(contenitore1, text="Salva")
        pulsante_salva_modifiche.grid(row=6, column=1)
        pulsante_salva_modifiche.bind("<Button-1>", lambda event, matricola=matricola: self.on_pulsante_salvaModifiche_wrapper(event, matricola))


    def on_pulsante_salvaModifiche_wrapper(self, event, matricola):
        self.salva_ModificheStudente(matricola)
        
    def salva_ModificheStudente(self, matricola):
        studente = self.archivio.studente(matricola)

        # Prendo i dati in input
        cognome = self.entry_cognome.get()
        nome = self.entry_nome.get()
        matricola = self.readOnlyText.get(1.0, tk.END)
        input_esami = self.entry_esami.get()
        note = self.entry_note.get()

        # Caratteri ammessi nei campi
        lettere_base = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        lettere_accentate = "éèòçàùìÉÈÒÇÀÙÌ"
        lettere = lettere_base + lettere_accentate
        chars_nomecognome = lettere + " " + "'"
        numeri = "1234567890"

        # Controllo che i caratteri inseriti nei campi siano adeguati (solo lettere per nome e cognome, solo numeri per la matricola)
        if self.contiene_solo_caratteri(cognome, chars_nomecognome, "cognome") and self.contiene_solo_caratteri(nome, chars_nomecognome, "nome") and self.contiene_solo_caratteri(matricola, numeri, "matricola"):            
            studente.set_cognome(cognome)
            studente.set_nome(nome)
            lista_esami = []
            if not(input_esami is None or input_esami == ""):
                # Per la modifica degli esami vengono accettati due formati: la lista di tuple oppure il formato per l'inserimento (CODICE-VOTO, separati da virgola e spazio)
                if input_esami[0] == '[': # Se l'utente non modifica gli esami già presenti, o se lascia il formato di lista di tuple
                    # input esami [('564GG', 18), ('241SS', 30), ('544MM', 26)] è una stringa, e lista_esami deve essere una lista di tuple
                    cleaned_input_esami = input_esami.replace("[", "").replace("]", "").replace("(", "").replace(")", "")
                    # cleaned_input_esami  '564GG', 18, '241SS', 30, '544MM', 26
                    elements = cleaned_input_esami.split(', ')
                    # I valori in posizione dispari sono i voti, quelli in posizione pari sono i codici, sfrutto questa cosa per creare due liste che poi unisco per ottenere la lista_esami
                    codici = []
                    voti = []
                    pari = True
                    for element in elements:
                        if pari:
                            codice = element.strip("'")
                            codici.append(codice)
                        else:
                            voto = int(element)
                            if voto > 33 or voto < 18:
                                messagebox.showerror("Errore", "I voti devono essere compresi tra 18 e 33")
                                return
                            voti.append(voto)
                        pari = not pari
                    # Unisci le due liste alternando codice e voto
                    lista_esami = [(codice, voto) for codice, voto in zip(codici, voti)]
                else: # Se l'utente inserisci esami nel formato CODICE-VOTO, separati da virgola e spazio, oppure se lascia il campo vuoto, oppure se sbaglia formato
                    if not (input_esami is None or input_esami == ""):
                        # Estrapolo il codice e il voto di ciascun esame inserito nel campo, e li aggiungo come tupla alla lista_esami
                        for esame in input_esami.split(','):
                                esame = esame.strip().split('-')
                                if esame and len(esame) == 2:
                                    codice, voto = esame
                                    voto = int(voto)
                                    lista_esami.append((codice, voto))
                                else:
                                    messagebox.showerror("Errore", "Inserire gli esami nel formato CODICE-VOTO, separati da virgola e spazio. Es: 544MM-30, 564GG-22, 241SS-25")
                                    return # Esco dalla funzione inserimento_studente altrimenti lo studente viene inserito con esami vuoti
            studente.set_listaesami(lista_esami)

            self.archivio.modifica_note(int(matricola), note)


            

        

            
        

        

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




root = tk.Tk()
app = myApp(root)
root.mainloop()
