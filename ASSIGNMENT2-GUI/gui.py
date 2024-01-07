'''
[x] visualizzare il contenuto del archivio,
[x] inserire un nuovo studente nell'archivio,
[x] modificare i dati di uno studente,
[x] cancellare uno studente dall'archivio,
[x] calcolare la media dei voti di uno studente,
[x] caricare l'archivio da file,
[ ] salvare l'archivio su file,
[ ] uscire dall'applicazione.
'''

from archivio import *
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import re 
from tkinter import filedialog as fd # Per il caricamento e il salvataggio dell'archivio da file

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
        self.pulsante_visualizzaArchivio.bind("<Button-1>", self.finestra_visualizzaArchivio)
        # Inserisci studente
        self.pulsante_inserisciStudente = tk.Button(contenitore1, text="Inserisci studente")
        self.pulsante_inserisciStudente.grid(row=1, column=0)
        self.pulsante_inserisciStudente.bind("<Button-1>", self.finestra_inserisciStudente)
        # Modifica studente
        self.pulsante_modificaStudente = tk.Button(contenitore1, text="Modifica studente")
        self.pulsante_modificaStudente.grid(row=2, column=0)
        self.entry_matricola_modificaStudente = tk.Entry(contenitore1, width=20)
        self.entry_matricola_modificaStudente.grid(row=2, column=1)
        CreateToolTip(self.entry_matricola_modificaStudente, text = 'Inserire la matricola dello studente di cui modificare i dati')
        self.pulsante_modificaStudente.bind("<Button-1>", self.on_pulsante_modificaStudente) #on_pulsante_modificaStudente serve a passare il valore della matricola da modificare
        # Cancella studente
        self.pulsante_cancellaStudente = tk.Button(contenitore1, text="Cancella studente")
        self.pulsante_cancellaStudente.grid(row=3, column=0)
        self.entry_matricola_cancellaStudente = tk.Entry(contenitore1, width=20)
        self.entry_matricola_cancellaStudente.grid(row=3, column=1)
        CreateToolTip(self.entry_matricola_cancellaStudente, text = 'Inserire la matricola dello studente da cancellare')
        self.pulsante_cancellaStudente.bind("<Button-1>", self.on_pulsante_cancellaStudente) #on_pulsante_cancellaStudente serve a passare il valore della matricola da cancellare
        # Media
        self.pulsante_mediaStudente = tk.Button(contenitore1, text="Media studente")
        self.pulsante_mediaStudente.grid(row=4, column=0)
        self.entry_matricola_mediaStudente = tk.Entry(contenitore1, width=20)
        self.entry_matricola_mediaStudente.grid(row=4, column=1)
        CreateToolTip(self.entry_matricola_mediaStudente, text = 'Inserire la matricola dello studente di cui calcolare la media del libretto')
        self.pulsante_mediaStudente.bind("<Button-1>", self.on_pulsante_mediaStudente) #on_pulsante_mediaStudente serve a passare il valore della matricola di cui calcolare la media
        # Caricare l'archivio da file
        self.pulsante_caricaArchivio = tk.Button(contenitore1, text="Carica archivio da file")
        self.pulsante_caricaArchivio.grid(row=5, column=0)
        self.pulsante_caricaArchivio.bind("<Button-1>", self.seleziona_file)


    def contiene_solo_caratteri(self, campo, caratteri_validi, etichetta):
        pattern = "^[{}]+$".format(re.escape(caratteri_validi))
        if (re.match(pattern, campo)):
            return True
        else:
            messagebox.showerror("Errore", "Il campo " + str(etichetta) + " deve contenere solo questi caratteri: " + str(caratteri_validi))
            return 
        


    ######### HANDLER ##########
    def finestra_visualizzaArchivio(self, event):
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

    def finestra_inserisciStudente(self, event):
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
        CreateToolTip(self.entry_cognome, text = 'Inserire il cognome dello studente utilizzando solo lettere, spazi e apostrofi.')
        self.entry_nome = tk.Entry(contenitore1, width=50)
        self.entry_nome.grid(row=1, column=1)
        CreateToolTip(self.entry_nome, text = 'Inserire il nome dello studente utilizzando solo lettere, spazi e apostrofi.')
        self.entry_matricola = tk.Entry(contenitore1, width=50)
        self.entry_matricola.grid(row=2, column=1)
        CreateToolTip(self.entry_matricola, text = 'Inserire la matricola dello studente come numero intero positivo.')
        self.entry_esami = EntryWithPlaceholder(contenitore1, placeholder="Nel formato 544MM-30, 564GG-22, 241SS-25...",  placeholder_color='grey', width=50) # Inserire gli esami nel campo nel formato CODICE-VOTO, separati da virgola e spazio
        self.entry_esami.grid(row=3, column=1)
        CreateToolTip(self.entry_esami, text = 'Scrivere gli esami nel formato CODICE-VOTO, separati da virgola e spazio. \nEs: 544MM-30, 564GG-22, 241SS-25')
        self.entry_note = tk.Entry(contenitore1, width=50)
        self.entry_note.grid(row=4, column=1)
        CreateToolTip(self.entry_note, text = 'Inserire le note dello studente.')         
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
        if self.contiene_solo_caratteri(matricola, "1234567890", "matricola"):
            if not (int(matricola) in self.archivio.get_studenti()):
                messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
                return
            # Eseguo la funzione di modifica, passando il valore dell'entry come parametro
            self.finestra_modificaStudente(int(matricola))

    def finestra_modificaStudente(self, matricola):
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

    def on_pulsante_cancellaStudente(self, event):
        matricola = self.entry_matricola_cancellaStudente.get()
        if matricola is None or matricola == "":
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

    def on_pulsante_mediaStudente(self, event):
        matricola = self.entry_matricola_mediaStudente.get()
        if matricola is None or matricola == "":
            messagebox.showerror("Errore", "Inserire la matricola dello studente di cui calcolare la media.")
            return
        if self.contiene_solo_caratteri(matricola, "1234567890", "matricola"):
            if not (int(matricola) in self.archivio.get_studenti()):
                messagebox.showerror("Errore", "Matricola non presente nell'archivio.")
                return
            # Eseguo la funzione di calcolo della media, passando il valore dell'entry come parametro
            messagebox.showinfo("Media", "La media dello studente " + matricola + " è " + str(self.archivio.media(int(matricola))))

    def seleziona_file(self, event):
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
                    messagebox.showerror("Errore", "L'archivio non è stato aggiornato: riferirsi alla console per maggiori informazioni.")
            else:
                messagebox.showinfo("Caricamento annullato", "L'archivio non è stato caricato.")

            

        

            
        

        

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
