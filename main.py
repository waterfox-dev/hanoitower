def initialisation(number_of_disk : int):
    tower_dict    = {}
    tower_dict[0] = [[], [], []]
    for i in range(3):
        for j in range(0,number_of_disk) :
            if i == 0  : #On traite le premier piquet
                string = str((number_of_disk - j) * "-" )+ ((number_of_disk - j) * "-")
                tower_dict[0][0].insert(0, string)
            else : #On traite les autres piquets qui sont vides
                tower_dict[0][i].append('x')
    return tower_dict

def last_elt(piquet : list, caractere : str = 'x'):
    for i in range(1, len(piquet)):
        if piquet[-i] == caractere:
            return -i
    if piquet[0] == caractere : #On traite le premier élement du piquet
        return 0

def first_disk(piquet : list, piquet_symbol : str = '-'):
    for i in range(len(piquet)):
        if piquet_symbol in piquet[i] :
            return i

def deplacer(disque : int, origine : int, destination : int):
    if origine not in [1,2,3] and destination not in [1,2,3]: #Vérificaiton de l'existence de la tour
        raise IndexError("This tower don't exist")
    else :
        try :
            last_config                                    = list(dico_coups.keys())[-1]
            disk                                           = first_disk(dico_coups[last_config][origine])            
            position                                       = last_elt(dico_coups[last_config][destination])
            dico_coups[last_config][destination][position] = dico_coups[last_config][origine][disk]
            dico_coups[last_config][origine][disk]         = 'x'
            a = dico_coups[last_config].copy()
            dico_coups[last_config + 1]                    = a
        except IndexError :
            print(f"disque : {disque}\norigine : {origine}\ndestination : {destination}")

def hanoi(n, i=1, j=2, k=3):
    if n==1:
        print(f"Disque 1 de la tour {i} vers la tour {j} ")
        deplacer(0, i-1, j-1)
        return 
    hanoi(n-1, i, k, j)
    print(f"Disque {n} de la tour {i} vers la tour {j} ")
    deplacer(-n, i-1, j-1)
    hanoi(n-1, k, j, i)

# Programme principal :
if __name__ == "__main__":  
    n = int(input('saisir le nombre de tours : '))
    dico_coups = initialisation(3)    
    hanoi(n)
    print(dico_coups)