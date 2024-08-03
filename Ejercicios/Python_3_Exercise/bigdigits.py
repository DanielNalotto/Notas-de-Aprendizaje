"""
El ejercicio consiste en recibir un numero por consola, y dibujarlo en pantalla.
"""

zero =  ["   ***   ", " *     * ", "*       *", "*       *", "*       *", " *     * ", "   ***   "]
one =   ["    *    ", "  * *    ", "    *    ", "    *    ", "    *    ", "    *    ", "  * * *  "]
two =   ["  *****  ", "*       *", "*     *  ", "    *    ", "  *      ", "*       *", "******** "]
three = ["  *****  ", "*       *", "        *", "    ***  ", "        *", "*       *", "  *****  "]
four =  ["      *  ", "    * *  ", "  *   *  ", " *    *  ", "* * * * *", "      *  ", "      *  "]
five =  ["*********", "*        ", "*        ", "******** ", "        *", "*       *", " ******* "]
six =   [" ******* ", "*        ", "*        ", "* ****** ", "*       *", "*       *", " ******* "]
seven = ["*********", "        *", "       * ", "     *   ", "   *     ", " *       ", " *       "]
eight = ["  *****  ", "*       *", "*       *", "  *****  ", "*       *", "*       *", "  *****  "]
nine =  ["  *****  ", "*       *", "*       *", "  *****  ", "        *", "        *", "  *****  "]

dic = {'0': zero, '1': one, '2':two, '3': three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine}

def print_vertical(num):
    for n in num:
        for row in dic.get(n):
            print(row)
        print('\n')

def print_horizontal(num):
    for i in range(0,7):
        for n in num:
            print(dic.get(n)[i], end='   ')
        print()

def show_menu():
    print('\nDe que manera quiere imprimir el numero:\n\n1_Vertical\n2_Horizontal\n3_Salir')
    return int(input('\nOpcion: '))

def process_option(opc):
        num = input("Ingrese numero a mostrar: ")
        print('\n')
        if opc == 1:
            print_vertical(num)
        elif opc == 2:
            print_horizontal(num)
        else:
            print('No selecciono ninguna opcon valida')

def main():
    opc = show_menu()
    while opc!=3:
        process_option(opc)
        opc = show_menu()

main()