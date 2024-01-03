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
            listaesami = []     #Mi serve perché altrimenti se metto uno studente senza listaesami, il programma mi da errore perché non può fare il for esame in listaesami
        for esame in listaesami:
            if not isinstance(esame[0], str) or not isinstance(esame[1], int) or not(18 <= esame[1] <= 33):
                raise ValueError("Inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 33")
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
    def set_cognome(self, cognome):  #TODO controlla che non possa farlo con if else
        if not isinstance(cognome, str) or cognome == "":
            raise TypeError("Il cognome deve essere una stringa")
        self.cognome = cognome
        print("Cognome modificato correttamente")

    def set_nome(self, nome): #TODO controlla che non possa farlo con if else
        if not isinstance(nome, str) or nome == "":
            raise TypeError("Il nome deve essere una stringa")
        self.nome = nome
        print("Nome modificato correttamente")

    def set_matricola(self, matricola): #TODO controlla che non possa farlo con if else
        if not isinstance(matricola, int) or matricola <= 0:
            raise TypeError("La matricola deve essere un numero intero positivo")
        self.matricola = matricola
        print("Matricola modificata correttamente")

    def set_listaesami(self, listaesami): 
        if not isinstance(listaesami, list):
            raise TypeError("La lista degli esami deve essere una lista")
        for esame in listaesami:
            if not isinstance(esame[0], str):
                raise TypeError("Inserire una stringa con il codice dell'esame")
            if not isinstance(esame[1], int):
                raise TypeError("Inserire un numero intero come esame")
            if not(18 <= esame[1] <= 33):
                raise ValueError("Inserire un voto compreso tra 18 e 33")
        self.listaesami = listaesami

    def __str__(self):
        if not self.listaesami:
            return self.nome + " " + self.cognome + " " + "mat: " + str(self.matricola) + " " + "esami: no"
        else:
            return self.nome + " " + self.cognome + " " + "mat: " + str(self.matricola) + " " + "esami: " + str(self.listaesami)

    def __eq__(self, altroStudente):
        return self.cognome == altroStudente.cognome and self.nome == altroStudente.nome and self.matricola == altroStudente.matricola

    def registra_esame(self, codice, voto):
        if not isinstance(codice, str) or not isinstance(voto, int) or not(18 <= voto <= 33):
            print("ERRORE: inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 33")
            return False
        else:
            for esame in self.listaesami:
                if esame[0] == codice:
                    print("ERRORE: lo studente ha già sostenuto l'esame")
                    return False 
            self.listaesami.append((codice, voto))
            print("Esame registrato")
            return True

    def modifica_voto(self, codice, voto):
        if not isinstance(codice, str) or codice == "":
            print("ERRORE: inserire una stringa con il codice dell'esame")
            return False
        elif not isinstance(voto, int) or not(18 <= voto <= 33):
            print("ERRORE: inserire come voto un intero compreso tra 18 e 33")
            return False
        else:
            for i in range(len(self.listaesami)):       #scorro la lista degli esami dello studente  [('544MM', 23), ('564GG', 21)]
                esame = self.listaesami[i]                #prendo la tupla esame (codice, voto)
                if esame[0] == codice:                     #se il codice dell'esame è uguale al codice passato
                    if esame[1] == voto:                    #se il voto è uguale al voto passato
                        print("ERRORE: inserire un voto diverso da quello assegnato")
                        return False
                    self.listaesami[i] = (codice, voto)    #modifico la tupla perché le tuple non ammettono assegnamenti di un singolo elemento della tupla (come il codice)
                    print("Voto modificato correttamente")
                    return True
            print("ERRORE: esame non presente nella carriera dello studente")
            return False
    #Nota: utilizzo l'indice per modificare il voto perché le tuple non ammettono assegnamenti di un singolo elemento (come il codice)''. Se usassi variabili come voto1, codice1, voto2 e codice2 e qualcosa come voto1 = voto2 avrei una modifica della variabile  variabile voto1 locale, che è una variabile temporanea e non influisce sulla tupla reale in self.listaesami.
        
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

    def media(self):
        if not self.listaesami:
            print("Lo studente non ha ancora sostenuto alcun esame")
            return None
        somma_voti = 0
        for voto in self.listaesami:
            somma_voti += voto[1]
        f = somma_voti / len(self.listaesami)
        return f
    


#CLASSE ARCHIVIO
class Archivio:
    def __init__(self):
        self.stud = {} #inizializzo l'archivio come dizionario vuoto
        if not isinstance(self.stud, dict):
            raise TypeError("L'archivio deve essere un dizionario") #TODO non so quanto sia utile questo controllo

    def inserisci(self, studente, note=""):
        if not isinstance(studente, Studente):
            print("ERRORE: L'oggetto inserito non è di tipo Studente")
            return False
        if studente.matricola in self.stud:
            print("ERRORE: studente già presente nell'archivio")
            return False
        if not isinstance(note, str) and note is not None:
            print("ERRORE: Le note devono essere una stringa")
            return False
            #utile solo in caso il dizionario venga fornito a mano già popolato, ma non è il caso, se nella chiamata archivio.inserisci(stud1, "nota1") non viene passata una stringa, viene stampato l'errore NameError nota1 is not defined 
        self.stud[studente.matricola] = (studente, note) #inserisco la matricola come chiave e la tupla (studente, note) come valore
        return True

    def __str__(self):
        stampa = ""
        for matricola, (studente, note) in self.stud.items():
            if note == "":
                stampa += str(studente) + "\n"
            else:
                stampa += str(studente) + ' ' + str(note) + "\n"
        return stampa

    def elimina(self, matricola):
        if matricola in self.stud:
            del self.stud[matricola]
            print("Studente eliminato correttamente")
            return True
        print("ERRORE: matricola non presente nell'archivio")
        return False

    def get_note(self, matricola):
        if matricola in self.stud:                
            return self.stud[matricola][1]  #ricorda che la tupla è (studente, note)
        return None 

    def get_studenti(self):
        return list(self.stud.keys())

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

        #TODO Vuoi creare un metodo in cui cancelli la nota con i relativi test?

    def studente(self, matricola):
        if matricola in self.stud:
            s = self.stud[matricola][0]
            return s
        return None

    def registra_esame(self, matricola, codice, voto):
        if matricola in self.stud:
            if isinstance(codice, str) and isinstance(voto, int) and 18 <= voto <= 33:
                (studente, note) = self.stud[matricola]
                studente.registra_esame(codice, voto)
                return True
            else:
                print("ERRORE: inserire una stringa con il codice dell'esame, e come voto un intero compreso tra 18 e 33")
                return False
        print("ERRORE: matricola non presente nell'archivio")
        return False

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

    def media(self, matricola):
        if matricola in self.stud:
            (studente, note) = self.stud[matricola]
            f = studente.media()
            return f
        print("ERRORE: matricola non presente nell'archivio")
        return None

    def lista_studenti_promossi(self, codice, soglia=18):
        matricole_promosse = []
        #self.stud è un dizionario (Studente, note), quindi per scorrerlo devo usare items()
        for matricola, (studente, note) in self.stud.items():
            for esame in studente.listaesami:
                if esame[0] == codice and esame[1] >= soglia:
                    matricole_promosse.append(studente.get_matricola())
                    break
        return matricole_promosse
    
    def conta_studenti_promossi(self, codice, soglia=18):
        n = len(self.lista_studenti_promossi(codice, soglia))
        return n
    
    def lista_studenti_media(self, soglia=18):
        matricole_selezionate = []
        if not isinstance(soglia, int) or not(18 <= soglia <= 33):
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
        Lo studente non ha ancora sostenuto alcun esame
        Lo studente non ha ancora sostenuto alcun esame
        [345655, 987654, 789101]
    perché stud2 e stud5 non hanno esami, quindi non hanno media, quindi non vengono inseriti nella lista, ma ho messo una stampa che dice che non hanno esami
    '''


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

    def carica(self,nomefile):
        try:
            with open(nomefile, "r") as f:
                #987654; Giulia Verdi mat: 987654 esami: [('564GG', 18), ('241SS', 30), ('544MM', 26)];nota3
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
















'''stud1 = Studente("Rossi", "Carlo", 345655, [('544MM', 30), ('564GG', 22)])
stud2 = Studente("Bianchi", "Luigi", 123456, [])
stud3 = Studente("Verdi", "Giulia", 987654, [('564GG', 18), ('241SS', 30), ('544MM', 26)])
stud4 = Studente("Neri", "Giorgio", 789101, [('671IF', 25), ('410SS', 18), ('388LL', 29)])
stud5 = Studente("Gialli", "Giorgio", 549245)



archivio = Archivio()

archivio.inserisci(stud1, "nota1")
archivio.inserisci(stud2, "nota2")
archivio.inserisci(stud3, "nota3")
archivio.inserisci(stud4, "nota4")
archivio.inserisci(stud5, "nota5")

archivio.carica("archivio2.txt")'''
'''
studenti = {
    345655: (stud1, 'nota1'),
    123456: (stud2, 'nota2'),
    987654: (stud3, 3),
    789101: (stud4, 'nota2')
}
'''
