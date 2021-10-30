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


def hanoi(n, origine = 1, destination = 2, pivot = 3):
    last_config = list(dico_coups.keys())[-1]
    if n == 1 :
        # print(f"Disk 1 from {origine} to {destination}")
        deplacer(0, dico_coups[last_config][origine-1], dico_coups[last_config][destination-1])
        return None
    else :

        hanoi(n-1, origine, pivot, destination)
        deplacer(n-1, dico_coups[last_config][origine-1], dico_coups[last_config][destination-1])

        # print(f"Disk {n} from {origine} to {destination}")       
        hanoi(n-1, pivot, destination, origine)  

if __name__ == "__main__":
    n = int(input('saisir le nombre de tours : '))
    dico_coups = initialisation()
    print(dico_coups)
    hanoi(n)
    print(dico_coups)