# https://www.youtube.com/watch?v=Y_Gej0lbfD0
""" 
Recibes un string como parametro, el cual contiene llaves ()[]{}
Si todos los pares de llaves se abren y cierran correctamente, la funcion debería
devolver True, un elemento vacío también retorna True
Si esto no se cumpliera, la función devolvería False.
"""

def correct_brackets(sequence):
    brackets_type = ['()', '[]', '{}']
    while sequence != '':
        for br in sequence:
            sequence.(br)
    if sequence == '':
        return True
    else:
        return False

correct_brackets("()")

    