"""
Assegnamento 1py 622AA 2023/24 svolto da:
Agnese Camici
mat. 559788
a.camici1@studenti.unipi.it
"""

#Dizionario esempio per chiamare le funzioni durante lo svolgimento dell'assegnamento
stud = {
    123456: ('Rossi', 'Mario', 123456, [("BIBL", 30), ("CGC", 28)], 'Note1'),
    789101: ('Bianchi', 'Luca', 789101, [("LC", 30), ("BIBL", 28), ("ML", 25), ("AE", 26), ("COD", 24)], ''),
    987654: ('Verdi', 'Giulia', 987654, [("LC", 29), ("BIBL", 18), ("ML", 25), ("AE", 19), ("COD", 18)], ''),
}


#Controllo sul parametro in input matricola:
#se è una stringa rappresentante un intero>0 lo restituisce
#altrimenti se il parametro input matricola è un intero lo restituisce direttamente
def str_int_mat(matricola):
  if type(matricola) == int and matricola > 0:
    return matricola
  elif type(matricola) == str:
    if matricola.isdigit():
      return int(matricola)
    else:
      print("ERRORE: il codice della matricola deve essere un intero positivo")
      return False
  else:
    print("ERRORE: il codice della matricola deve essere un intero positivo")
    return False


#Controllo validitàlistaesami: 
#una lista di coppie (codice -- str, voto--int positivo <33) senza esami duplicati
def controllo_listaesami(listaesami):
  if type(listaesami) != list:
    print("ERRORE: inserire gli esami come lista")
    return False
  else:
    codici_esami = []  #per controllare esami duplicati
    for esame in listaesami:
      if type(esame) != tuple or len(esame) != 2:
        print("ERRORE: scrivere ogni esame come coppia codice-voto")
        return False
      codice, voto = esame
      if type(codice) != str or type(voto) != int or not(18 <= voto <= 33):
        print("ERRORE: il codice degli esami deve essere una stringa, e il voto un intero compreso tra 18 e 33")
        return False
      if codice in codici_esami:
        print("ERRORE: stai cercando di inserire un esame due volte")
        return False
      codici_esami.append(codice)
    return True


#Controllo per validità parametri nome o cognome: stringhe non nulle
def controllo_nome_cog(nome):
  if type(nome) == str and nome != '':
    return True
  else:
    print("ERRORE: il nome e il cognome devono essere stringhe non vuote")
    return False

#Inserisce un nuovo studente nel dizionario
def inserisci(stud,cognome,nome,matricola,listaesami,note=""):
  #controlli sul tipo di parametri in input
  if type(stud) == dict and controllo_nome_cog(cognome) and controllo_nome_cog(nome) and (bool(str_int_mat(matricola)) != False) and controllo_listaesami(listaesami) and type(note) == str: 
    matricola = int(matricola) 
    if matricola not in stud:
      stud[matricola] = (cognome, nome, matricola, listaesami, note) #inserimento
      return True
    else: 
      print("ERRORE: matricola già presente")
      return False
  else: #listaesami non è una lista o c'è un errore di tipo in un altro parametro
    #Gli errori vengono già stampati dalle funzioni controllo_listaesami e controllo_nome_cog
    return False


#Serializza tutti gli studenti nel dizionario creando una singola stringa
#Ogni studente è separato dagli altri dal carattere \n
#Output-> Mario Rossi mat: 123456 esami: no note: Note1 \n
#         Luca Bianchi mat: 123456 esami: ('LC', 30), ('BIBL', 28), ('ML', 25), ('AE', 26), ('COD', 24) note: no
def serializza(stud):
  diz_serializzato = ""
  for matricola, dati_studente in stud.items():
    cognome, nome, matricola, listaesami, note = dati_studente
    #Serializzo listaesami
    #Output-> ('LC', 30), ('BIBL', 28), ('ML', 25)
    elementi_serializzati = []
    for codice, voto in listaesami:
      elemento_serializzato = "('" + str(codice) + "', " + str(voto) + ")"
      elementi_serializzati.append(elemento_serializzato)
    listaesami_serializzata = ", ".join(elementi_serializzati)
    #Creazione della stringa per lo studente corrente
    studente_str = nome + " " + cognome + " mat: " + str(matricola) + " esami: " + (listaesami_serializzata if listaesami else 'no') + " note: " + (note if note else 'no')
    #Aggiunta della stringa al dizionario serializzato con un carattere di \n
    diz_serializzato += studente_str + "\n"
  return diz_serializzato


#Restituisce la tupla relativa ad uno studente
def studente(stud, matricola):
  matricola = str_int_mat(matricola)
  if matricola in stud: #un controllo su matricola>0 sarebbe ridondante perché nel diz. ci sono solo matricole >0
    t = stud[matricola]
    return t
  else: #ad esempio se la matricola è int<0 / se non è nel dizionario..
    print("ERRORE: studente non presente, controllare correttezza del codice matricola")
    return None


#Aggiunge un nuovo esame superato (codice,voto) alla lista esami per lo studente con matricola "matricola"
def registra_esame(stud, matricola, codice, voto):
  matricola = str_int_mat(matricola)
  if matricola in stud:
    info_studente = stud[matricola] #informazioni dello studente
    lista_esami = info_studente[3] #lista degli esami dello studente
    for esame in lista_esami: 
      if esame[0] == codice: #esame già presente nell'elenco della matricola
        print("ERRORE: esame già presente nella carriera dello studente")
        return False
    if type(codice) != str:
      print("ERRORE: il codice degli esami deve essere una stringa, e il voto un intero compreso tra 18 e 33")
      return False
    if type(voto) != int or not(18 <= voto <= 33):
      print("ERRORE: inserire solo voti interi tra 18 e 33")
      return False
    lista_esami.append((codice, voto))
    return True
  else:
    print("ERRORE: matricola non presente")
    return False


#Calcola la media dello studente con matricola "matricola"
def media(stud, matricola):
  matricola = str_int_mat(matricola)
  if matricola not in stud: 
    return None
  lista_esami = stud[matricola][3]
  if not lista_esami: #studente senza esami
    return None
  somma_voti = 0
  numero_esami = len(lista_esami)
  for voto in lista_esami:
    somma_voti += voto[1]
  f = somma_voti / numero_esami
  return f
  

#Modifica il voto di un esame per lo studente con matricola "matricola"
def modifica_voto(stud, matricola, codice, voto):
  matricola = str_int_mat(matricola)
  if matricola not in stud:   #controllo che include quelli sulla correttezza del dato inserito
    print("ERRORE: matricola non presente")
    return False
  if type(voto) != int or voto < 18 or voto > 33:
    print("ERRORE: inserire solo voti compresi tra 18 e 33")
    return False
  lista_esami = stud[matricola][3]
  for i in range(len(lista_esami)): #qui non faccio la copia perché la lunghezza degli elementi rimarrà uguale anche dopo la modifica
    codice_esame, voto_esame = lista_esami[i]
    if codice == codice_esame: #non ho messo un controllo all'inizio della funzione sulla presenza del codice in stud perché qua viene cercato
      if lista_esami[i][1] == voto:
        print("ERRORE: inserire un voto differente da quello già presente")
        return False
      lista_esami[i] = codice_esame, voto
      return True
  print("ERRORE: esame non presente nella carriera dello studente")
  return False #restituisce False se non trova il codice dato nella lista_esami


#Cancella un esame per lo studente con matricola "matricola"
def cancella_esame(stud,matricola,codice):
  matricola = str_int_mat(matricola)
  if matricola not in stud:
    print("ERRORE: matricola non presente")
    return False
  lista_esami = stud[matricola][3] 
  for esame in lista_esami.copy(): #uso una copia di lista_esami per iterare perché la modifico nel frattempo
    codice_esame, voto_esame = esame
    if codice == codice_esame:
      lista_esami.remove(esame)
      return True
  print("ERRORE: esame non presente nella carriera dello studente")
  return False #se la lista è vuota, o se non trova l'esame dopo il ciclo (codice non in stud)


#Crea la lista degli studenti che hanno superato 
#l'insegnamento "codice" con valutazione uguale o superiore alla soglia
def lista_studenti_promossi(stud, codice, soglia=18):
  lista_promossi = []
  esame_presente = False
  for matricola, (cognome, nome, matricola, esami, note) in stud.items(): #restituisce una vista delle coppie chiave-valore (righe studenti)
    for insegnamento, voto in esami:
      if insegnamento == codice:
        esame_presente = True
        if voto >= soglia:
          lista_promossi.append((matricola, cognome, nome, voto)) #[(789101, 'Bianchi', 'Luca', 24), (987654, 'Verdi', 'Giulia', 19)]
  if not esame_presente:
    print("L'esame", codice, "non è stato ancora sostenuto da nessuno studente")
    return False
  return lista_promossi


#Conta quanti studenti hanno superato l'insegnamento "codice" con
#valutazione uguale o superiore alla soglia
def conta_studenti_promossi(stud, codice, soglia=18):
  promossi = lista_studenti_promossi(stud, codice, soglia)
  return len(promossi)


#Crea la lista degli studenti che hanno una media superiore alla soglia
def lista_studenti_media (stud, soglia=18):
  lista_media_promossi = []
  for matricola, (cognome, nome, matricola, esami, note) in stud.items():
    voti_studente = []
    for insegnamento, voto in esami:
      voti_studente.append(voto)    
    if len(voti_studente) > 0:
      media = sum(voti_studente) / len(voti_studente)
    else:
      media = 0
    if media >= soglia:
      lista_media_promossi.append((matricola, cognome, nome, media))
  return lista_media_promossi
