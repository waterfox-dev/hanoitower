def initialisation() :
    return {
        0: [['--', '----', '------'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    }

def last_elt(liste : list, caractere : str):
    for i in range(1, len(liste)):
        if liste[-i] == caractere :
            return -i
    if liste[0] == 'x' :
        return 0
        

def deplacer(a : int, b : list, c : list):
    try :
        temp = b[a]
        b[a] = 'x'
        pos = last_elt(c, 'x')
        c[pos] = temp
        print(dico_coups)
    except Exception as e :
        print(pos, a, b, c, e)


def hanoi(disque, source = 1, destination = 2, pivot = 3):
    if disque == 0 :
        print(f"Déplacer le disque {disque} de {source} vers {destination}")
    else :
        hanoi(disque-1, source, pivot, destination)
        print(f"Déplacer le disque {disque} de {source} vers {destination}")
        hanoi(disque-1, pivot, destination, source)
            
if __name__ == "__main__":
    n = int(input('saisir le nombre de tours : '))
    dico_coups = initialisation()
    print(dico_coups)
    hanoi(n)
    print(dico_coups)