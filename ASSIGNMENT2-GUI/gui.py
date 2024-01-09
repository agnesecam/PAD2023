from archivio import *
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage # Per il bottone Chiudi
from tkinter import filedialog as fd # Per il caricamento e il salvataggio dell'archivio da file

import re 
from datetime import datetime # Per salvare un archivio con il nome della data di oggi alla chiusura dell'applicazione

class myApp:
    def __init__(self, root):
        self.root = root
        root.config(background='#FAE5E8')
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.root)
        contenitore1.pack()
        contenitore1.config(background='#FAE5E8', pady=20)

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
        self.archivio.inserisci(stud4)
        self.archivio.inserisci(stud5, "nota5")

        # Creo i bottoni
        # Visualizza archivio
        self.pulsante_visualizzaArchivio = tk.Button(contenitore1, text="Visualizza archivio", background="#F7CAD0", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_visualizzaArchivio.grid(row=1, column=0, padx=10, pady=2)
        self.pulsante_visualizzaArchivio.bind("<Button-1>", self.finestra_visualizzaArchivio)
        self.pulsante_visualizzaArchivio.focus()
        # Inserisci studente
        self.pulsante_inserisciStudente = tk.Button(contenitore1, text="Inserisci studente", background="#F9BEC7", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_inserisciStudente.grid(row=2, column=0, padx=10, pady=2)
        self.pulsante_inserisciStudente.bind("<Button-1>", self.finestra_inserisciStudente)
        # Modifica studente
        self.pulsante_modificaStudente = tk.Button(contenitore1, text="Modifica studente", background="#FBB1BD", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_modificaStudente.grid(row=3, column=0, padx=10, pady=2)
        self.entry_matricola_modificaStudente = EntryWithPlaceholder(contenitore1, placeholder="549245",  placeholder_color='grey', width=18, border=0)
        self.entry_matricola_modificaStudente.grid(row=3, column=1)
        CreateToolTip(self.entry_matricola_modificaStudente, text = 'Inserire la matricola dello studente di cui modificare i dati')
        self.pulsante_modificaStudente.bind("<Button-1>", self.on_pulsante_modificaStudente) #on_pulsante_modificaStudente serve a passare il valore della matricola da modificare
        # Cancella studente
        self.pulsante_cancellaStudente = tk.Button(contenitore1, text="Cancella studente", background="#FF99AC", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_cancellaStudente.grid(row=4, column=0, padx=10, pady=2)
        self.entry_matricola_cancellaStudente = EntryWithPlaceholder(contenitore1, placeholder="549245",  placeholder_color='grey', width=18, border=0)
        self.entry_matricola_cancellaStudente.grid(row=4, column=1)
        CreateToolTip(self.entry_matricola_cancellaStudente, text = 'Inserire la matricola dello studente da cancellare')
        self.pulsante_cancellaStudente.bind("<Button-1>", self.on_pulsante_cancellaStudente) #on_pulsante_cancellaStudente serve a passare il valore della matricola da cancellare
        # Media
        self.pulsante_mediaStudente = tk.Button(contenitore1, text="Calcola la media", background="#FF85A1", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_mediaStudente.grid(row=5, column=0, padx=10, pady=2)
        self.entry_matricola_mediaStudente = EntryWithPlaceholder(contenitore1, placeholder="549245",  placeholder_color='grey', width=18, border=0)
        self.entry_matricola_mediaStudente.grid(row=5, column=1)
        CreateToolTip(self.entry_matricola_mediaStudente, text = 'Inserire la matricola dello studente di cui calcolare la media del libretto')
        self.pulsante_mediaStudente.bind("<Button-1>", self.on_pulsante_mediaStudente) #on_pulsante_mediaStudente serve a passare il valore della matricola di cui calcolare la media
        # Carica l'archivio da file
        self.pulsante_caricaArchivio = tk.Button(contenitore1, text="Carica archivio da file", background="#FF7096", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_caricaArchivio.grid(row=6, column=0, padx=10, pady=2)
        self.pulsante_caricaArchivio.bind("<Button-1>", self.carica_archivio)
        # Salva archivio su file
        self.pulsante_salvaArchivio = tk.Button(contenitore1, text="Salva archivio su file", background="#FF5C8A", foreground="#000000", border=0, width=18, cursor="hand2")
        self.pulsante_salvaArchivio.grid(row=7, column=0, padx=10, pady=2)
        self.pulsante_salvaArchivio.bind("<Button-1>", self.salva_archivio)
        self.entry_salvaArchivio = EntryWithPlaceholder(contenitore1, placeholder="archivio0901.txt",  placeholder_color='grey', width=18, border=0)
        self.entry_salvaArchivio.grid(row=7, column=1)
        CreateToolTip(self.entry_salvaArchivio, text = "Scrivere il nome e l'estensione del file da creare in cui salvare l'archivio. \nEs: filename.txt")
        # Chiudi
        self.immagineX = tk.PhotoImage(file="immagineX.png", width=20, height=20)
        self.pulsante_chiudi = tk.Button(contenitore1, image=self.immagineX, text="Chiudi", background="#FAE5E8", activebackground="#FAE5E8", border=0, width=50, cursor="hand2")
        self.pulsante_chiudi.grid(row=0, column=2, padx=10, pady=2)
        CreateToolTip(self.pulsante_chiudi, text = "Chiudi l'applicazione")
        self.pulsante_chiudi.bind("<Button-1>", self.chiudi)
        
    ######### METODI UTILI sfruttati dagli handler ##########
    def contiene_solo_caratteri(self, campo, caratteri_validi, etichetta):
        pattern = "^[{}]+$".format(re.escape(caratteri_validi))
        if (re.match(pattern, campo)):
            return True
        else:
            messagebox.showerror("Errore", "Il campo " + str(etichetta) + " deve contenere solo questi caratteri: " + str(caratteri_validi))
            return 
        
    def chiudi_finestra(self):
        self.dialog.destroy()
        
        

    ######### HANDLER ##########
    def finestra_visualizzaArchivio(self, event):
        # Creo una nuova finestra per la visualizzazione dell'archivio
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Visualizza archivio")
        self.dialog.config(background='#FAE5E8')

        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)  
        contenitore1.pack()
        # Creo la textbox
        self.box_visualizzaArchivio = tk.Text(contenitore1, width=90, height=10, background='#FAE5E8', border=0, font=("Arial", 9), pady=10, padx=10)
        self.box_visualizzaArchivio.pack()
        self.box_visualizzaArchivio.delete("1.0", tk.END)
        self.box_visualizzaArchivio.insert(tk.END, str(self.archivio))
        self.box_visualizzaArchivio.configure(state="disabled")


    # Inserisci studente
    def finestra_inserisciStudente(self, event):
        # Creo una nuova finestra per gestire l'inserimento di un nuovo studente
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Inserisci studente")
        self.dialog.geometry("400x170")
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)
        contenitore1.pack()
        contenitore1.config(background='#FAE5E8')
        self.dialog.config(background='#FAE5E8')
        # Creo le etichette per i campi di input
        self.label_cognome = tk.Label(contenitore1, text="Cognome", background='#FAE5E8')
        self.label_cognome.grid(row=0, column=0, pady=(8,2))
        self.label_nome = tk.Label(contenitore1, text="Nome", background='#FAE5E8')
        self.label_nome.grid(row=1, column=0, pady=2)
        self.label_matricola = tk.Label(contenitore1, text="Matricola", background='#FAE5E8')
        self.label_matricola.grid(row=2, column=0, pady=2)
        self.label_esami = tk.Label(contenitore1, text="Esami", background='#FAE5E8')
        self.label_esami.grid(row=3, column=0, pady=2)
        self.label_note = tk.Label(contenitore1, text="Note", background='#FAE5E8')
        self.label_note.grid(row=4, column=0, pady=2)
        # Creo i campi di input
        self.entry_cognome = tk.Entry(contenitore1, width=50, border=0)
        self.entry_cognome.grid(row=0, column=1, pady=(8,2))
        self.entry_cognome.focus()
        CreateToolTip(self.entry_cognome, text = 'Inserire il cognome dello studente utilizzando solo lettere, spazi e apostrofi.')
        self.entry_nome = tk.Entry(contenitore1, width=50, border=0)
        self.entry_nome.grid(row=1, column=1, pady=2)
        CreateToolTip(self.entry_nome, text = 'Inserire il nome dello studente utilizzando solo lettere, spazi e apostrofi.')
        self.entry_matricola = tk.Entry(contenitore1, width=50, border=0) 
        self.entry_matricola.grid(row=2, column=1, pady=2)
        CreateToolTip(self.entry_matricola, text = 'Inserire la matricola dello studente come numero intero positivo.') 
        self.entry_esami = EntryWithPlaceholder(contenitore1, placeholder="Nel formato 544MM-30, 564GG-22, 241SS-25...",  placeholder_color='grey', width=50, border=0) # Inserire gli esami nel campo nel formato CODICE-VOTO, separati da virgola e spazio
        self.entry_esami.grid(row=3, column=1, pady=2)
        CreateToolTip(self.entry_esami, text = 'Scrivere gli esami nel formato CODICE-VOTO, separati da virgola e spazio. \nEs: 544MM-30, 564GG-22, 241SS-25')
        self.entry_note = tk.Entry(contenitore1, width=50, border=0)
        self.entry_note.grid(row=4, column=1, pady=2)
        CreateToolTip(self.entry_note, text = 'Inserire le note dello studente.')         
        # Creo il pulsante per l'inserimento
        pulsante_inserisci = tk.Button(contenitore1, text="Inserisci", background="#F7CAD0", border=0)
        pulsante_inserisci.grid(row=5, column=1, pady=5)
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
        if self.contiene_solo_caratteri(cognome, chars_nomecognome, "cognome") and self.contiene_solo_caratteri(nome, chars_nomecognome, "nome") and self.contiene_solo_caratteri(matricola, numeri, "matricola") and self.contiene_solo_caratteri(input_esami, numeri + lettere + " " + "-" + ",", "esami"):
            # Se il campo esami non è stato completato lista_esami rimane una lista vuota
            if not (input_esami is None or input_esami == "" or input_esami == self.entry_esami.placeholder): #Dato che ho inserito i placeholder devo considerare che esami_input sia uguale al placeholder            
                # Estrapolo il codice e il voto di ciascun esame inserito nel campo, e li aggiungo come tupla alla lista_esami                
                for esame in input_esami.split(','):
                    try:
                        esame = esame.strip().split('-')
                        if esame and len(esame) == 2:
                            codice, voto = esame
                            voto = int(voto)
                            lista_esami.append((codice, voto))
                        else:
                            messagebox.showerror("Errore", "Inserire gli esami nel formato CODICE-VOTO, separati da virgola e spazio. Es: 544MM-30, 564GG-22, 241SS-25")
                            return 
                    except ValueError:
                        messagebox.showerror("Errore", "Controllare il fomrmato e la correttezza dei dati nella lista degli esami.")
                        return

            # Creo un nuovo studente di esempio per poter usare i metodi setter
            nuovo_studente = Studente("Nuovo", "Studente", 999999, [])
            nuovo_studente.set_cognome(cognome) # Il cognome e il nome saranno una stringa perché l'inserimento avviene tramite un campo di testo, quindi devo usare un controllo sui caratteri inseriti nella stringa (contiene_solo_caratteri)
            nuovo_studente.set_nome(nome)
            nuovo_studente.set_matricola(int(matricola))    
            nuovo_studente.set_listaesami(lista_esami)
            # Inserisco lo studente nell'archivio assieme alle note
            risposta = messagebox.askokcancel("Conferma", "Inserire lo studente " + str(nuovo_studente) + "?", default="cancel")
            if risposta == True:
                self.archivio.inserisci(nuovo_studente, note)
                # Controllo se l'inserimento è avvenuto
                if len(self.archivio.stud) > lunghezza_archivio:
                    messagebox.showinfo("Inserimento avvenuto", "Lo studente è stato inserito correttamente.")
                    self.chiudi_finestra()
                else:
                    messagebox.showerror("Errore", "Inserimento non avvenuto: studente già presente nell'archivio.")
                    return
                    
                    

    # Modifica studente
    def on_pulsante_modificaStudente(self, event):
        matricola = self.entry_matricola_modificaStudente.get()
        if (matricola is None or matricola == "" or matricola == self.entry_matricola_modificaStudente.placeholder):
            messagebox.showerror("Errore", "Inserire la matricola dello studente da modificare.")
        elif self.contiene_solo_caratteri(matricola, "1234567890", "matricola"):
            if not (int(matricola) in self.archivio.get_studenti()):
                messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
                return
            # Eseguo la funzione di modifica, passando il valore dell'entry come parametro
            self.finestra_modificaStudente(int(matricola))


    def pulsante_salva_modifiche_handler(self, event):
        matricola = self.readOnlyText.get(1.0, tk.END).strip()
        self.salvaModifiche(event, matricola)


    def finestra_modificaStudente(self, matricola):
        # Creo una nuova finestra per gestire l'inserimento di un nuovo studente
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Modifica studente con matricola " + str(matricola))
        self.dialog.geometry("400x300")
        self.dialog.config(background='#FAE5E8')
        # Creo il frame contenitore
        contenitore1 = tk.Frame(self.dialog)
        contenitore1.pack()
        contenitore1.config(background='#FAE5E8')

        # Recupero i vecchi dati dello studente
        cognome_vecchio = self.archivio.studente(matricola).get_cognome()
        nome_vecchio = self.archivio.studente(matricola).get_nome()
        lista_esami_vecchi = self.archivio.studente(matricola).get_listaesami()
        note_vecchie = self.archivio.get_note(matricola)
        stringa_esami_vecchi = []
        for tupla_esame in lista_esami_vecchi:
            codice, voto = tupla_esame
            stringa_esame = codice + '-' + str(voto)
            stringa_esami_vecchi.append(stringa_esame)
        esami_vecchi_formattati = ', '.join(stringa_esami_vecchi)


        # Creo le label per i campi di input
        self.label_cognome_nuovo = tk.Label(contenitore1, text="Cognome", background='#FAE5E8')
        self.label_cognome_nuovo.grid(row=0, column=0, pady=(8,2))
        self.label_nome_nuovo = tk.Label(contenitore1, text="Nome", background='#FAE5E8')
        self.label_nome_nuovo.grid(row=1, column=0, pady=2)
        self.label_matricola = tk.Label(contenitore1, text="Matricola", background='#FAE5E8')
        self.label_matricola.grid(row=2, column=0, pady=2)
        self.label_esami_nuovi = tk.Label(contenitore1, text="Esami", background='#FAE5E8')
        self.label_esami_nuovi.grid(row=3, column=0, pady=2)
        self.label_note_nuove = tk.Label(contenitore1, text="Note", background='#FAE5E8')
        self.label_note_nuove.grid(row=4, column=0, pady=2)
        # Creo i campi di input
        self.entry_cognome = tk.Entry(contenitore1, width=50, border=0)
        self.entry_cognome.grid(row=0, column=1, pady=2)
        self.entry_cognome.focus()
        self.entry_cognome.delete(0, tk.END)
        self.entry_cognome.insert(0, cognome_vecchio)
        self.entry_nome = tk.Entry(contenitore1, width=50, border=0)
        self.entry_nome.grid(row=1, column=1, pady=2)
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, nome_vecchio)
        self.entry_esami = tk.Entry(contenitore1, width=50, border=0)
        CreateToolTip(self.entry_esami, text = "Scrivere gli esami nel formato CODICE-VOTO, separati da virgola e spazio o come lista di tuple. \nEs: 544MM-30, 564GG-22, 241SS-25\nEs: [('544MM'-30), ('564GG'-22), ('241SS'-25)]")
        self.entry_esami.grid(row=3, column=1, pady=2)
        self.entry_esami.delete(0, tk.END)
        
        self.entry_esami.insert(0, esami_vecchi_formattati)
        self.entry_note = tk.Entry(contenitore1, width=50, border=0)            
        self.entry_note.grid(row=4, column=1, pady=2)
        self.entry_note.delete(0, tk.END)
        self.entry_note.insert(0, note_vecchie)         
        #La matricola non sarà modificabile, quindi uso una casella di testo con lo stato disabilitato
        self.readOnlyText = tk.Text(contenitore1, width=40, height=1, border=0, font=("Arial", 9), background='#FAE5E8')
        self.readOnlyText.insert(1.0, matricola)
        self.readOnlyText.configure(state="disabled")
        self.readOnlyText.grid(row=2, column=1, pady=2)

        # Creo il pulsante per l'inserimento
        pulsante_salva_modifiche = tk.Button(contenitore1, text="Salva", border=0, background="#F7CAD0")
        pulsante_salva_modifiche.grid(row=6, column=1, pady=2)
        pulsante_salva_modifiche.bind("<Button-1>", self.pulsante_salva_modifiche_handler)


    def salvaModifiche (self, event, matricola):
        risposta = messagebox.askokcancel("Conferma", "Salvare le modifiche allo studente con matricola " + matricola + "?", default="cancel")
        matricola = int(matricola)
        if risposta == True:
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
                # Se il campo esami non è stato completato lista_esami rimane una lista vuota
                if (input_esami is None or input_esami == ""):
                    self.archivio.modifica_note(int(matricola), note)
                    messagebox.showinfo("Modifica avvenuta", "Lo studente è stato modificato correttamente.")
                    self.chiudi_finestra()
                else:
                    # Estrapolo il codice e il voto di ciascun esame inserito nel campo, e li aggiungo come tupla alla lista_esami                
                    for esame in input_esami.split(','):
                        esame = esame.strip().split('-')
                        if esame and len(esame) == 2:
                            codice, voto = esame
                            voto = int(voto)
                            lista_esami.append((codice, voto))
                        else:
                            messagebox.showerror("Errore", "Inserire gli esami nel formato CODICE-VOTO, separati da virgola e spazio. Es: 544MM-30, 564GG-22, 241SS-25")
                            return 
                try:
                    studente.set_listaesami(lista_esami)
                except ValueError:
                    messagebox.showerror("Errore", "Impossibile salvare: controllare la formattazione e la correttezza del campo lista esami.")
                    return
                self.archivio.modifica_note(int(matricola), note)
                messagebox.showinfo("Modifica avvenuta", "Lo studente è stato modificato correttamente.")
                self.chiudi_finestra()
            

    # Cancella studente
    def on_pulsante_cancellaStudente(self, event):
        matricola = self.entry_matricola_cancellaStudente.get()
        if (matricola is None or matricola == "" or matricola == self.entry_matricola_cancellaStudente.placeholder):
            messagebox.showerror("Errore", "Inserire la matricola dello studente da cancellare.")
            return
        if self.contiene_solo_caratteri(matricola, "1234567890", "matricola"):
            if not (int(matricola) in self.archivio.get_studenti()):
                messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
                return
            # Eseguo la funzione di cancellazione, passando il valore dell'entry come parametro
            risposta = messagebox.askquestion("Conferma", "Cancellare lo studente con matricola " + matricola + "?", default="no")
            if risposta == "yes":
                self.archivio.elimina(int(matricola))
                messagebox.showinfo("Cancellazione avvenuta", "Lo studente " + matricola + " è stato cancellato correttamente.")
            else:
                messagebox.showinfo("Cancellazione annullata", "Lo studente " + matricola + " non è stato cancellato.")


    # Media studente
    def on_pulsante_mediaStudente(self, event):
        matricola = self.entry_matricola_mediaStudente.get()
        if (matricola is None or matricola == "" or matricola == self.entry_matricola_mediaStudente.placeholder):
            messagebox.showerror("Errore", "Inserire la matricola dello studente di cui calcolare la media.")
            return
        if self.contiene_solo_caratteri(matricola, "1234567890", "matricola"):
            if not (int(matricola) in self.archivio.get_studenti()):
                messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
                return
            # Eseguo la funzione di calcolo della media, passando il valore dell'entry come parametro
            if self.archivio.media(int(matricola)) is None:
                messagebox.showinfo("Media", "Lo studente " + matricola + " non ha esami registrati.")
            else:
                messagebox.showinfo("Media", "La media dello studente " + matricola + " è " + str(self.archivio.media(int(matricola))))


    # Carica archivio da file
    def carica_archivio(self, event):
        filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
        )
        # Apro una finestra di dialogo per selezionare il file (non è possibile selezionare più di un file, quindi non occorre che gestisca questo caso)
        path = fd.askopenfilename(
            title="Seleziona il file contenente l'archivio",
            initialdir='/',
            filetypes=filetypes)
        # Apro una messagebox che mostra il nome del file selezionato
        if path is None or path == "":
            messagebox.showinfo("Caricamento annullato", "Nessun file selezionato.")
            return
        else:
            filename = path.split('/')[-1]  # Voglio solo il nome del file, non il path completo
            risposta = messagebox.askquestion("Conferma", "Caricare l'archivio dal file " + filename + "?", default="no")
            if risposta == "yes":
                # Carico l'archivio dal file selezionato
                lunghezza_archivio = len(self.archivio.stud)
                try:    # Se viene scelto un file che può essere interpretato da archivio.py come archivio, viene caricato, altrimenti viene mostrato il messaggio di errore seguente e annullata l'azione
                    self.archivio.carica(filename)
                except ValueError:
                    messagebox.showerror("Errore", "Il file selezionato non è un archivio nel formato corretto. Caricamento non riuscito.")
                    return
                if lunghezza_archivio < len(self.archivio.stud):
                    messagebox.showinfo("Caricamento avvenuto", "L'archivio è stato caricato correttamente.")
                else:
                    messagebox.showwarning("Errore", "Tutti gli studenti sono già presenti nell'archivio.")
            else:
                messagebox.showinfo("Caricamento annullato", "L'archivio non è stato caricato.")
    
    # Salva archivio su file
    """
    In tkinter è possibile utilizzare la "asksaveasfilename" per salvare il contenuto dell'archivio. 
    L'operazione sarebbe gestita in modo più sicuro e completo, generando una finestra dialog che permette di selezionare il percorso e il nome del file da salvare.
    Tuttavia, avendo già implementato la funzione di salvataggio in archivio.py, ho deciso di sfruttarla quella.
    """
    def salva_archivio(self, event):
        filename = self.entry_salvaArchivio.get()
        if (filename is None or filename == "" or filename == self.entry_salvaArchivio.placeholder):
            messagebox.showerror("Errore", "Inserire il nome del file in cui salvare l'archivio.")
            return
        else:
            caratteri_validi = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890.-_()"
            if self.contiene_solo_caratteri(filename, caratteri_validi, "nome file"):
                self.archivio.salva(filename)
                messagebox.showinfo("Salvataggio completato", "L'archivio è stato salvato correttamente nel file " + filename + ".")


    # Chiudi
    def chiudi(self, event):
        risposta = messagebox.askyesnocancel("Chiudi l'applicazione", "Vuoi salvare l'archivio prima di arrestare l'applicazione?", default="cancel")
        if risposta == True:
            oggi = datetime.now()
            filenameOggi = "archivio_" + oggi.strftime("%Y%m%d%H%M%S") + ".txt"
            self.archivio.salva(filenameOggi)
            root.destroy()
        elif risposta == False:
            root.destroy()





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


# Classe per mostrare un testo quando faccio hover su un bottone per dare indicazioni all'utente
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 15
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                    background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                    font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



root = tk.Tk()
app = myApp(root)
root.mainloop()
