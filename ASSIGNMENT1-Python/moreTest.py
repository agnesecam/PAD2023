from testMy import *
from stud import *

def controllo2():
  testFalliti2 = 0
  x = {}
  y = {
      123456: ('Rossi', 'Mario', 123456, [("BIBL", 30), ("CGC", 28)], 'Note1'),
      789101: ('Bianchi', 'Luca', 789101, [("LC", 30), ("BIBL", 28), ("ML", 25), ("AE", 26), ("COD", 24)], ''),
      987654: ('Verdi', 'Giulia', 987654, [("LC", 29), ("BIBL", 18), ("ML", 25), ("AE", 19), ("COD", 18)], ''),
      830292: ('Cordini', 'Giuseppe', 830292, [], ''),
  }

  print("---TEST A - str_int_matricola---")
  #mat int>0
  testFalliti2 += testEqual(str_int_mat(345655), 345655)
  #mat str digit
  testFalliti2 += testEqual(str_int_mat("345655"), 345655)
  #mat int<0
  testFalliti2 += testEqual(str_int_mat(-345655), False)
  #mat str non digit
  testFalliti2 += testEqual(str_int_mat("abcdef"), False)
  #mat str digit <0
  testFalliti2 += testEqual(str_int_mat("-345655"), False)

  print("---TEST B - controllo_listaesami---")
  #listaesami non è una lista
  testFalliti2 += testEqual(controllo_listaesami((18, 33, 25, 27, 28)), False)
  #listaesami è una lista ma non di coppie
  testFalliti2 += testEqual(controllo_listaesami([("CGC", 18, 345655), ("ING", 32, 345655), ("TAD", 25, 345655), ("LI2", 27, 345655), ("ML", 28, 345655)]), False)
  #uno degli esami è fuori range 18-33
  testFalliti2 += testEqual(controllo_listaesami([("CGC", 18), ("ING", 34), ("TAD", 25), ("LI2", 27), ("ML", 28)]), False)
  #un codice esame non è una stringa
  testFalliti2 += testEqual(controllo_listaesami([("CGC", 18), ("ING", 33), ("TAD", 25), (12345, 27), ("ML", 28)]), False)
  #un codice esame appare due volte
  testFalliti2 += testEqual(controllo_listaesami([("CGC", 18), ("ING", 33), ("TAD", 25), ("ING", 27), ("ML", 28)]), False)
  #listaesami lista di tuple coppia codice(str)-voto(int 18-33)
  testFalliti2 += testEqual(controllo_listaesami([("CGC", 18), ("ING", 33), ("TAD", 25), ("LI2", 27), ("ML", 28)]), True)

  print("---TEST C - controllo_nome_cog---")
  #nome o cognome NULL
  testFalliti2 += testEqual(controllo_nome_cog(""), False)
  #nome o cognome non str
  testFalliti2 += testEqual(controllo_nome_cog(123456), False)
  #nome o cognome stringhe
  testFalliti2 += testEqual(controllo_nome_cog("Mario"), True)

  print("---TEST D - inserisci---")
  #nome o cognome NULL, oppure nome o cognome non str
  testFalliti2 += testEqual(inserisci(x, "", "Luigi", 528611, [("544MM", 23)]), False)
  testFalliti2 += testEqual(inserisci(x, "Bianchi", 123456, 528611, [("544MM", 23)]), False)
  #matricola str <0
  testFalliti2 += testEqual(inserisci(x, "Bianchi", "Luigi", "-528611", [("544MM", 23)]), False)
  #listaesami non lista o con tuple non coppia codice(str)-voto(int 18-33)
  testFalliti2 += testEqual(inserisci(x, "Bianchi", "Luigi", 528611, ("544MM", 23)), False)
  testFalliti2 += testEqual(inserisci(x, "Bianchi", "Luigi", 528611, [("544MM", 23, "Mario")]), False)
  #note non stringa
  testFalliti2 += testEqual(inserisci(x, "Bianchi", "Luigi", "-528611", [("544MM", 23, "Mario", 123456789)]), False)
  #matricola stringa già in dizionario
  testFalliti2 += testEqual(inserisci(y, "Bianchi", "Luigi", "987654", [("544MM", 23, "Mario")]), False)
  

  print("---TEST E - studente---")
  #matricola stringa non in dizionario
  testFalliti2 += testEqual(studente(y, "51423"), None)
  #matricola stringa in dizionario
  testFalliti2 += testEqual(studente(y, "987654"), ('Verdi', 'Giulia', 987654, [("LC", 29), ("BIBL", 18), ("ML", 25), ("AE", 19), ("COD", 18)], ''))

  print("---TEST F - registra_esame---")
  #matricola stringa non in dizionario
  testFalliti2 += testEqual(registra_esame(y, "782910", 'CGC', 19), False)
  #matricola stringa in dizionario
  testFalliti2 += testEqual(registra_esame(y, "789101", 'CGC', 19), True)
  #esame non intero 18-33
  testFalliti2 += testEqual(registra_esame(y, "789101", 'CGC', 16), False)
  
  print("---TEST G - media---")
  #matricola stringa non in dizionario
  testFalliti2 += testEqual(media(y, "782910"), None)
  #matricola stringa in dizionario
  testFalliti2 += testEqual(media(y, "987654"), 21.8)
  print(media(y, "789101"))
  #matricola stringa senza esami
  testFalliti2 += testEqual(media(y, "830292"), None)


  print("---TEST H - modifica_voto---")
  #matricola stringa e codice in dizionario
  testFalliti2 += testEqual(modifica_voto(y, "123456", "BIBL", 21), True)
  #matricola stringa non in dizionario
  testFalliti2 += testEqual(modifica_voto(y, "121456", "BIBL", 21), False)
  #voto inserito uguale a quello già presente
  testFalliti2 += testEqual(modifica_voto(y, 123456, "CGC", 28), False)
  #voto inserito uguale a quello già presente e matricola str
  testFalliti2 += testEqual(modifica_voto(y, "123456", "CGC", 28), False)

  print("---TEST I - cancella_esame---")
  #matricola stringa e codice in dizionario
  testFalliti2 += testEqual(cancella_esame(y, "123456", "BIBL"), True)
  #matricola stringa non in dizionario
  testFalliti2 += testEqual(cancella_esame(y, "121456", "BIBL"), False)


  print("---TEST L - lista_studenti_promossi---")
  #esame non sostenuto da nessuno studente
  testFalliti2 += testEqual(lista_studenti_promossi(y, "ITC"), False)
  



  
  if testFalliti2 == 0:
    print("\n\nOK!")
  else:
    print("Test falliti: ",testFalliti2)

  
controllo2()
