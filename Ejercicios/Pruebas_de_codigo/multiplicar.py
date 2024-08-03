#Realiza una funcion que multiplique dos numeros, sin usar la operación de multiplicación

def multiplication(a: int, b: int):
    r = 0
    for i in range (0,b):
        r = r + a
        #print(r)
    return r

#multiplication(1,2)
print(multiplication(1,2)) # res=2
print(multiplication(12,0)) # res=0
print(multiplication(1,1)) # res=1
print(multiplication(0,2)) # res=0
print(multiplication(5,2)) # res=10
print(multiplication(-5,2)) # res=-10
print(multiplication(7,-8)) # res=-56

