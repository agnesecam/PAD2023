# Da completare con il codice

#CLASSE Studente
"""#STATO:
cognome: cognome dello studente (stringa)
nome: nome dello studente (stringa)
matricola: numero di matricola (intero positivo)
listaesami: lista di tuple (codice -- str, voto--int positivo >= 18 e <33)
"""

"""METODI da aggiungere oltre a quelli presenti:

- Costrutture: metodo che inizializza lo studente con cognome, nome e matricola presi come argomenti e inizializza listaesami con lista vuota,
    controllando che i tipi dei parametri attuali abbiano il tipo corretto altrimenti solleva un'eccezione TypeError
- Getters: metodi che restituiscono il valore di una variabile di istanza, es: get_cognome() --> restituisce il cognome
- Setters: metodi che modificano il valore di una variabile di istanza, es: set_cognome(cognome) --> modifica il cognome
    controllare che i valori inseriti siano del tipo e del valore corretto altrimenti sollevare un'eccezione TypeError o ValueError

"""

def get_voto(self,codice):
    """ Restituisce il voto dell'esame con codice "codice" se presente
    :param codice: il codice dell'esame
    :return: il voto dell'esame se presente
    :return: None se l'esame non è presente
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def __str__(self):
    """ Restituisce una stringa che rappresenta lo studente 
    esempio: Alessandro Bocci mat: 414805 esami: no
    esempio: Alessandro Bocci mat: 414805 esami: [('544MM', 23)]
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def __eq__(self,altroStudente):
    """ Restituisce True se self e altroStudente rappresentano lo stesso studente
    (stesso cognome, stesso nome, stessa matricola)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def registra_esame(self,codice,voto):
    """ Aggiunge un nuovo esame superato (codice,voto) alla lista esami
    :param codice: il codice dell'esame
    :param voto: il voto dell'esame
    :return: True se l'inserimento è andato a buon fine
    :return: False se si è verificato un errore (es. il codice è già presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def modifica_voto(self,codice,voto):
    """ Modifica il voto dell'esame con codice "codice" con il nuovo voto "voto"
    :param codice: il codice dell'esame da modificare
    :param voto: il nuovo voto dell'esame
    :return: True se la modifica è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def cancella_esame(self,codice):
    """ Cancella l'esame con codice "codice"
    :param codice: il codice dell'esame da cancellare
    :return: True se la cancellazione è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def media(self):
    """Calcola la media dei voti negli esami sostenuti
    :returns f: f è un valore float che fornisce la media dei voti negli esami sostenuti
    :returns None: se lo studente non ha sostenuto esami
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


##################################
#CLASSE Archivio
"""#STATO:
stud: dizionario degli studenti con chiave la matricola e valore una coppia oggetto studente e note (stringa)
"""

"""METODI da aggiungere oltre a quelli presenti:

- Costrutture: metodo che inizializza l'archivio con un dizionario vuoto
"""

def inserisci(self,studente,note=""):
    """ Inserisce un nuovo studente nel dizionario stud 
    :param studente: oggetto studente da inserire
    :param note: stringa (opzionale)
    :return: True se l'inserimento e' stato effettuato con successo,
    :return: False  se i parametri non hanno il tipo corretto o non sono corretti, oppure se la matricola e' gia' presente
    """
    pass #instruzione che non fa niente --> da sostituire con il codice

def elimina(self,matricola):
    """ Elimina lo studente con matricola "matricola"
    :param matricola: la matricola dello studente da eliminare
    :return: True se l'eliminazione e' stata effettuata con successo,
    :return: False se la matricola non e' presente
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def get_note(self,matricola):
    """ Restituisce le note dello studente con matricola "matricola"
    :param matricola: la matricola dello studente di cui si vogliono le note
    :return: le note dello studente
    :return: None se la matricola non e' presente
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def get_studenti(self):
    """ Restituisce la lista degli studenti
    :return: la lista delle matricole degli studenti
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def modifica_note(self,matricola,nota):
    """ Modifica le note dello studente con matricola "matricola"
    :param matricola: la matricola dello studente da modificare
    :param nota: la nuova nota da inserire (stringa)
    :return: True se la modifica e' stata effettuata con successo,
    :return: False se la matricola non e' presente
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def __str__ (self):
    """ restituisce una stringa contenente tutti gli studenti nell'archivio separati dal carattere "a capo" --> "\n"
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


def studente(self,matricola):
    """Restituisce lo studente con matricola "matricola"
    :param matricola: la matricola dello studente da estrarre
    :return s: l'oggetto studente'
    :return None: se lo studente non è presente nell'archivio"""

    pass #istruzione che non fa niente --> da sostituire con il codice

def registra_esame(self,matricola,codice,voto):
    """ Aggiunge un nuovo esame superato (codice,voto) alla lista esami dello studente con matricola "matricola" 
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame
    :param voto: il voto dell'esame
    :return: True se l'inserimento è andato a buon fine
    :return: False se si è verificato un errore (es. il codice è già presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def modifica_voto(self,matricola,codice,voto):
    """ Modifica il voto dell'esame con codice "codice" con il nuovo voto "voto" dello studente con matricola "matricola"
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame da modificare
    :param voto: il nuovo voto dell'esame
    :return: True se la modifica è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def cancella_esame(self,matricola,codice):
    """ Cancella l'esame con codice "codice" allo studente con matricola "matricola"
    :param matricola: la matricola dello studente
    :param codice: il codice dell'esame da cancellare
    :return: True se la cancellazione è andata a buon fine
    :return: False se si è verificato un errore (es. il codice non è presente)
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


def media(self, matricola):
    """Restituisce la media dello studente con matricola "matricola"
    :param stud: il dizionario degli studenti
    :param matricola: la matricola dello studente
    :returns f: f è un valore float che fornisce la media dei voti negli esami sostenuti
    :returns None: se lo studente non è presente
    """
    pass  # istruzione che non fa niente --> da sostituire con il codice

def lista_studenti_promossi(self,codice,soglia=18):
    """
    crea la lista degli studenti che hanno superato l'insegnamento "codice" con
    valutazione uguale o superiore alla soglia.
    :param codice: il codice dell'insegnamento di interesse
    :param soglia: la soglia di voto minima (>=) per essere compresi nella lista finale
    :returns lista: la lista degli studenti promossi con voto >= soglia
    """

    pass #istruzione che non fa niente --> da sostituire con il codice

def conta_studenti_promossi(self, codice, soglia=18):
        """
        conta quanti studenti hanno superato l'insegnamento "codice" con
        valutazione uguale o superiore alla soglia.
        
        :param codice: il codice dell'insegnamento di interesse
        :param soglia: la soglia di voto minima (>=) per essere compresi nel computo
        :returns n: il numero degli studenti promossi con voto >= soglia
        """
        pass #istruzione che non fa niente --> da sostituire con il codice


def lista_studenti_media(self, soglia=18):
        """
        crea la lista degli studenti che hanno una media superiore alla soglia
        :param soglia: la soglia di media minima (>=) per essere compresi nella lista finale
        :returns lista: la lista degli studenti promossi con media >= soglia
        """
        pass #istruzione che non fa niente --> da sostituire con il codice

def salva(self,nomefile):
    """
    salva l'archivio in un file di nome nomefile con un formato a piacere e gestendo eventuali eccezioni
    :param nomefile: il nome del file in cui salvare l'archivio
    :return: True se il salvataggio è andato a buon fine
    :return: False se si è verificato un errore
    """
    pass #istruzione che non fa niente --> da sostituire con il codice

def carica(self,nomefile):
    """
    carica l'archivio da un file di nome nomefile con un formato a piacere e gestendo eventuali eccezioni
    :param nomefile: il nome del file da cui caricare l'archivio
    :return: True se il caricamento è andato a buon fine
    :return: False se si è verificato un errore
    """
    pass #istruzione che non fa niente --> da sostituire con il codice





