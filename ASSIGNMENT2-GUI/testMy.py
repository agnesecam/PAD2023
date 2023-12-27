# test interi stringhe
def testEqual(x, y):
    """ Controlla se x e y sono uguali e restituisce 1 se non lo sono e
    0 se lo sono"""
    if x == y:
        print("Pass")
        return 0
    else:
        print("\033[31mNot passing\033[0m")
        print("\033[32mExpected:\033[0m", y, "\033[31mGot:\033[0m", x)
        return 1

def confronta_archivi(archivio1,archivio2):
    """ Controlla se archivio1 e archivio2 sono uguali e restituisce True se non lo sono e
    False se lo sono"""
    if len(archivio1.stud) != len(archivio2.stud):
        return False
    for matricola in archivio1.stud.keys():
        if matricola not in archivio2.stud.keys():
            return False
        if archivio1.stud[matricola] != archivio2.stud[matricola]:
            print(archivio1.stud[matricola], archivio2.stud[matricola])
            return False
    return True