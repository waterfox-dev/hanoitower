def last_elt(liste : list, caractere : str):
    for i in range(1, len(liste)):
        if liste[-i] == caractere :            
            return -i
    if liste[0] == 'x' :
        return 0

print(last_elt(['x', '------', '--'], 'x'))