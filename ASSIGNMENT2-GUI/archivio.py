'''
Assegnamento 2py 622AA 2023/24 svolto da:
Agnese Camici
mat. 559788
a.camici1@studenti.unipi.it
'''
import re

#CLASSE STUDENTE    
class Studente:
    def __init__(self, cognome, nome, matricola, listaesami=None):      # listaesami è un parametro opzionale
        if not isinstance(cognome, str) or not isinstance(nome, str) or cognome=="" or nome=="":
            raise TypeError("Il cognome e il nome devono essere stringhe")
        if not isinstance(matricola, int) or matricola <= 0:
            raise ValueError("La matricola deve essere un numero intero positivo")
        if not isinstance(listaesami, list) and listaesami is not None:
            raise TypeError("La lista degli esami deve essere una lista")
        if listaesami is None:
            listaesami = []     # Prevengo l'errore del for su listaesami vuota nel caso di studente senza esami
        for esame in listaesami:
            if not isinstance(esame[0], str) or not isinstance(esame[1], int) or not(18 <= esame[1] < 33):
                raise ValueError("Inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 32")
        else:
            self.cognome = cognome
            self.nome = nome
            self.matricola = matricola
            if listaesami is not None:
                self.listaesami = listaesami
            else:
                self.listaesami = []

    #Getters
    def get_cognome(self):
        return self.cognome
    
    def get_nome(self):   
        return self.nome

    def get_matricola(self):
            return self.matricola
    
    def get_voto(self, codice):
        listaesami = self.listaesami
        if listaesami == []:
            print("Lo studente non ha ancora sostenuto alcun esame")
        else:
            for esame in listaesami:
                if esame[0] == codice:
                    return esame[1]
            print("Il codice non è presente nella carriera dello studente")
            return None    
            
    def get_listaesami(self):
        return self.listaesami


    #Setters
    def set_cognome(self, cognome):
        if not isinstance(cognome, str) or cognome == "":
            raise TypeError("Il cognome deve essere una stringa")
        self.cognome = cognome
        print("Cognome modificato correttamente")

    def set_nome(self, nome):
        if not isinstance(nome, str) or nome == "":
            raise TypeError("Il nome deve essere una stringa")
        self.nome = nome
        print("Nome modificato correttamente")

    def set_matricola(self, matricola): 
        if not isinstance(matricola, int):
            # Alzo un'eccezione perché nella GUI scrivendo nelle entry viene passata una stringa come matricola. Alzare ora l'eccezione mi aiuta a tenere sotto controllo quel passaggio.
            raise TypeError("La matricola deve essere un numero intero positivo")
        elif matricola <= 0:
            raise ValueError("La matricola deve essere un numero intero positivo")
        self.matricola = matricola
        print("Matricola modificata correttamente")

    def set_listaesami(self, listaesami):
        if listaesami is None:
            listaesami = [] # Serve nella GUI per creare un'istanza della classe Studente da modificare durante l'inserimento di uno studente, altrimenti avrei un errore
        if not isinstance(listaesami, list):
            raise TypeError("La lista degli esami deve essere una lista")
        for esame in listaesami:
            if not isinstance(esame[0], str):
                raise TypeError("Inserire una stringa con il codice dell'esame")
            if not isinstance(esame[1], int):
                raise TypeError("Inserire un numero intero come esame")
            if not(18 <= esame[1] < 33):
                raise ValueError("Inserire un voto compreso tra 18 e 33")
        self.listaesami = listaesami

    def __str__(self):
        if not self.listaesami:
            return self.nome + " " + self.cognome + " " + "mat: " + str(self.matricola) + " " + "esami: no"
        else:
            return self.nome + " " + self.cognome + " " + "mat: " + str(self.matricola) + " " + "esami: " + str(self.listaesami)

    def __eq__(self, altroStudente):
        if isinstance(altroStudente, Studente): 
            return self.cognome == altroStudente.cognome and self.nome == altroStudente.nome and self.matricola == altroStudente.matricola
        print("ERRORE: L'oggetto passato non è di tipo Studente")
        return False


    # Registra esame
    def registra_esame(self, codice, voto):
        if not isinstance(codice, str) or not isinstance(voto, int) or not(18 <= voto < 33):
            print("ERRORE: inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 32")
            return False
        else:
            for esame in self.listaesami:
                if esame[0] == codice:
                    print("ERRORE: lo studente ha già sostenuto l'esame")
                    return False 
            self.listaesami.append((codice, voto))
            print("Esame registrato")
            return True


    # Modifica voto
    def modifica_voto(self, codice, voto):
        if not isinstance(codice, str) or codice == "":
            print("ERRORE: inserire una stringa con il codice dell'esame")
            return False
        elif not isinstance(voto, int) or not(18 <= voto < 33):
            print("ERRORE: inserire come voto un intero compreso tra 18 e 33")
            return False
        else:
            for i in range(len(self.listaesami)):       # Scorro la lista degli esami dello studente  [('544MM', 23), ('564GG', 21)]
                esame = self.listaesami[i]                 # prendo la tupla esame (codice, voto)
                if esame[0] == codice:                     # se il codice dell'esame è uguale al codice passato
                    if esame[1] == voto:                     # se il voto è uguale al voto passato
                        print("ERRORE: inserire un voto diverso da quello assegnato")
                        return False
                    # Modifico la tupla (perché le tuple non ammettono assegnamenti di un singolo elemento della tupla, come il voto)
                    # Utilizzo l'indice per modificare il voto perché le tuple non ammettono assegnamenti di un singolo elemento (come il codice). 
                    # Se usassi variabili come voto1, codice1, voto2 e codice2 e qualcosa come voto1 == voto2 avrei una modifica della variabile voto1 locale, che è una variabile temporanea e non influisce sulla tupla reale in self.listaesami.                    
                    self.listaesami[i] = (codice, voto)    
                    print("Voto modificato correttamente")
                    return True
            print("ERRORE: esame non presente nella carriera dello studente")
            return False
            

    # Cancella esame
    def cancella_esame(self, codice):
        if not isinstance(codice, str) or codice == "":
            print("ERRORE: inserire una stringa con il codice dell'esame")
            return False
        else:
            for esame in self.listaesami:
                if esame[0] == codice:
                    self.listaesami.remove(esame)
                    print("Esame rimosso correttamente")
                    return True
            print("ERRORE: esame non presente nella carriera dello studente")
            return False


    # Media
    def media(self):
        if not self.listaesami:
            print("Lo studente " + str(self.matricola) + " non ha ancora sostenuto alcun esame")
            return None
        somma_voti = 0
        for voto in self.listaesami:
            somma_voti += voto[1]
        f = somma_voti / len(self.listaesami)
        return f
    


#CLASSE ARCHIVIO
class Archivio:
    def __init__(self):
        self.stud = {} # Inizializzo l'archivio come dizionario vuoto
        if not isinstance(self.stud, dict):
            raise TypeError("L'archivio deve essere un dizionario")

    # Getters
    def get_note(self, matricola):
        if matricola in self.stud:                
            return self.stud[matricola][1]  # Ricorda che la tupla è (studente, note)
        return None 

    def get_studenti(self):
        return list(self.stud.keys())
    
    def __str__(self):
        stampa = ""
        for matricola, (studente, note) in self.stud.items():
            if note == "":
                stampa += str(studente) + "\n"
            else:
                stampa += str(studente) + ' ' + str(note) + "\n"
        return stampa
        

    # Inserisci studente
    def inserisci(self, studente, note = ""):
        if not isinstance(studente, Studente):
            print("ERRORE: L'oggetto inserito non è di tipo Studente")
            return False
        if studente.matricola in self.stud:
            print("ERRORE: studente già presente nell'archivio")
            return False
        if not isinstance(note, str) and note is not None:
            print("ERRORE: Le note devono essere una stringa")
            return False
            # L'ultimo controllo sulle note non è molto utile: nella GUI i campi passano necessariemente una stringa. Lascio comunque questo controllo per sicurezza nel caso in cui venga passato un archivio già esistente (come da un file di testo) e le note non siano stringhe.
        self.stud[studente.matricola] = (studente, note) # Inserisco la matricola come chiave e la tupla (studente, note) come valore
        return True


    # Elimina studente
    def elimina(self, matricola):
        if matricola in self.stud:
            del self.stud[matricola]
            print("Studente eliminato correttamente")
            return True
        print("ERRORE: matricola non presente nell'archivio")
        return False
    

    # Modifica note
    def modifica_note(self, matricola, nota):
        if matricola in self.stud:
            if not isinstance(nota, str):
                print("ERRORE: inserire una nota valida come stringa")
                return False
            self.stud[matricola] = (self.stud[matricola][0], nota) #modifico la tupla (studente, note) perché le tuple non ammettono assegnamenti di un singolo elemento della tupla (come la nota)
            if nota == "": 
                print("Hai eliminato il contenuto della nota senza inserire un nuovo testo")
            return True
        print("ERRORE: matricola non presente nell'archivio")
        return False


    # Studente
    def studente(self, matricola):
        if matricola in self.stud:
            s = self.stud[matricola][0]
            return s
        return None


    # Registra esame
    def registra_esame(self, matricola, codice, voto):
        if matricola in self.stud:
            if isinstance(codice, str) and isinstance(voto, int) and 18 <= voto < 33:
                (studente, note) = self.stud[matricola]
                studente.registra_esame(codice, voto)
                return True
            else:
                print("ERRORE: inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 32")
                return False
        print("ERRORE: matricola non presente nell'archivio")
        return False


    # Modifica voto
    def modifica_voto(self, matricola, codice, voto):
        #controlli dentro studente.modifica_voto
        #non controllo che la matricola sia un intero positivo perché se è all'interno di self.stud è sicuramente un intero positivo
        if matricola in self.stud:
            (studente, note) = self.stud[matricola]
            if studente.modifica_voto(codice, voto):
                studente.modifica_voto(codice, voto)
                return True
            return False        
        print("ERRORE: matricola non presente nell'archivio")
        return False
    

    # Cancella esame
    def cancella_esame(self, matricola, codice):
        if matricola in self.stud:
            studente, note = self.stud[matricola]
            if not studente.get_voto(codice): # Uso il metodo get_voto di Studente per verificare la presenza del codice nella lista esami dello studente. Se non lo trova, get_voto restituisce False, che viene preso dall'if
                print("ERRORE: codice non presente nella carriera dello studente")
                return False
            studente.cancella_esame(codice)
            return True
        print("ERRORE: matricola non presente nell'archivio")
        return False


    # Media studente
    def media(self, matricola):
        if matricola in self.stud:
            (studente, note) = self.stud[matricola]
            f = studente.media()
            return f
        print("ERRORE: matricola non presente nell'archivio")
        return None


    # Lista studenti promossi ad un esame
    def lista_studenti_promossi(self, codice, soglia=18):
        matricole_promosse = []
        #self.stud è un dizionario (Studente, note), quindi per scorrerlo devo usare items()
        for matricola, (studente, note) in self.stud.items():
            for esame in studente.listaesami:
                if esame[0] == codice and esame[1] >= soglia:
                    matricole_promosse.append(studente.get_matricola())
                    break
        return matricole_promosse
    

    # Conta studenti promossi ad un esame
    def conta_studenti_promossi(self, codice, soglia=18):
        n = len(self.lista_studenti_promossi(codice, soglia))
        return n
    

    # Lista studenti con una certa media
    def lista_studenti_media(self, soglia=18):
        matricole_selezionate = []
        if not isinstance(soglia, int) or not(18 <= soglia < 33):
            print("ERRORE: inserire un intero compreso tra 18 e 33")
            return None
        for matricola, (studente, note) in self.stud.items():
            if studente.media() is not None and studente.media() >= soglia:
                matricole_selezionate.append(matricola)
        if matricole_selezionate == []:
            print("Nessuno studente ha una media superiore a " + str(soglia))
        return matricole_selezionate
        ''' 
        Mi dà un outuput del tipo:
            Lo studente 123456 non ha ancora sostenuto alcun esame
            Lo studente 549245 non ha ancora sostenuto alcun esame
            [345655, 987654, 789101]
        poiché stud2 e stud5 non hanno esami, quindi non hanno media, quindi non vengono inseriti nella lista, ma ho messo una stampa che dice che non hanno esami
        '''

    # Salva su file
    def salva(self, nomefile):
        try:
            with open(nomefile, "w") as f:
                for matricola, (studente, note) in self.stud.items():
                    f.write(str(matricola) + "; " + str(studente) + ";" + str(note) +"\n")
        except FileExistsError as e:
            print("ERRORE: File " +str(nomefile)+" già esistente. Impossibile sovrascrivere.")
            return False
        except IOError as e:
            print("ERRORE durante il salvataggio del file " + str(nomefile) + ": " + str(e))
            return False
        else:
            print("Archivio salvato con successo in " + str(nomefile))
            return True

    # Carica da file
    def carica(self,nomefile):
        try:
            with open(nomefile, "r") as f:
                # Formato gestito: 987654; Giulia Verdi mat: 987654 esami: [('564GG', 18), ('241SS', 30), ('544MM', 26)];nota3
                for line in f:
                    matricola, studente, note = line.split(";")
                    matricola = int(matricola)
                    nome = studente.split(" ")[1]
                    cognome = studente.split(" ")[2]
                    lista_esami = []
                
                    if studente[len(studente)-1] == "]":
                        esami_str = (studente.split("[")[1])[:-1]
                        pattern = r"\('(\w+)', (\d+)\)"
                        matches = re.findall(pattern, esami_str)
                        for codice, voto in matches:
                            lista_esami.append((codice, int(voto)))

                    stud = Studente(cognome, nome, matricola, lista_esami)
                    #print(stud)
                    if note[len(note)-1] == "\n":
                        note = note[:-1]
                    self.inserisci(stud, note)
                print(self)
                return True
        except IOError as e:
            print("ERRORE durante il caricamento del file " + str(nomefile) + ":" + str(e))
            return False
