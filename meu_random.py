from random import randrange

def get_random_lista(inicial,final,tam):
    lista= []
    for numero in range(0,tam):
        numero = randrange(inicial,final)
        lista.append(numero)
    return lista

