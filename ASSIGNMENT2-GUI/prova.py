archivio = """Carlo Rossi mat: 345655 esami: [('544MM', 30), ('564GG', 22)] nota1
Luigi Bianchi mat: 123456 esami: no nota2
Giulia Verdi mat: 987654 esami: [('564GG', 18), ('241SS', 30), ('544MM', 26)] nota3
Giorgio Neri mat: 789101 esami: [('671IF', 25), ('410SS', 18), ('388LL', 29)] nota4
Giorgio Gialli mat: 549245 esami: no nota5"""

righe = archivio.split('\n')

for riga in righe:
    if not riga:
        continue  # Salta righe vuote

    # Dividi la riga in parti usando "split"
    parti = riga.split()

    # Estrai le informazioni desiderate
    nome = parti[0] + " " + parti[1]
    matricola = parti[3]
    
    # Trova l'indice di "esami:"
    esami_index = parti.index('esami:')

    # Se "esami:" è seguito da "[", allora c'è una lista di esami
    if parti[esami_index + 1] == '[':
        # Trova la parte della stringa con la lista degli esami
        esami_str = " ".join(parti[esami_index + 1:])
        # Estrai solo la lista degli esami
        esami = eval(esami_str)  # Utilizza eval per convertire la stringa in una lista
        # Estrai la nota
        nota = parti[-1]
    else:
        # Se non c'è una lista di esami, imposta esami come None
        esami = None
        # Estrai la nota dalla parte corrispondente
        nota = parti[esami_index + 1]

    print(f"Nome: {nome}, Matricola: {matricola}, Esami: {esami}, Nota: {nota}")
