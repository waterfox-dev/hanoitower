#Global variables 
nb_round = 0
win_state = False

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

def get_last_config(data : dict, actual_round : int):
    if list(data.keys()) == [0]:
        return data[0].copy()
    else :
        return data[actual_round - 1].copy()

def deplacer(disque : int, origine : int, destination : int):
    
    if origine not in [1,2,3] and destination not in [1,2,3]: #Vérificaiton de l'existence de la tour
        raise IndexError("This tower don't exist")
    
    else :
        global nb_round
        global dico_coups
        
        working_list = get_last_config(dico_coups, nb_round).copy()
        working_disk = first_disk(working_list[origine])
        disk_place   = last_elt(working_list[destination])
        
        working_list[destination][disk_place] = working_list[origine][working_disk]
        working_list[origine][working_disk]   = 'x'
        
                
        if nb_round + 1 not in list(dico_coups.keys()):
            nb_round += 1
            dico_coups_copy = dico_coups.copy()
            dico_coups_copy[nb_round] = working_list
            dico_coups = dico_coups_copy
            working_list = []
        
def hanoi(n, i=1, j=2, k=3):
    if n==1:
        print(f"Disque 1 de la tour {i} vers la tour {j} ")
        deplacer(0, i-1, j-1)
        return
    else:
        hanoi(n-1, i, k, j)
        print(f"Disque {n} de la tour {i} vers la tour {j} ")
        deplacer(-n, i-1, j-1)
        hanoi(n-1, k, j, i)


if __name__ == "__main__":  
    n = int(input('saisir le nombre de tours : '))
    int_tower = n
    dico_coups = initialisation(3)    
    hanoi(n)
    print(dico_coups)