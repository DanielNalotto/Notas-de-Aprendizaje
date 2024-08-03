import pygame, sys, random
from pygame.locals import*

def verifSuperposicionRects(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        if ((puntoDentroDeRect(a.left, a.top, b)) or
            (puntoDentroDeRect(a.left, a.bottom, b)) or
            (puntoDentroDeRect(a.right, a.top, b)) or
            (puntoDentroDeRect(a.right, a.bottom,b))):
            return True
    return False

def puntoDentroDeRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

# Establecer el juego
pygame.init()
relojPrincipal = pygame.time.Clock()

#Establecer la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Nombre del Juego')

#Establece las variables de dirección

ABAJOIZQUIERDA = 1
ABAJODERECHA = 3
ARRIBAIZQUIERDA =7
ARRIBADERECHA = 9

VELOCIDADMOVIMIENTO = 4

#Establece los colores

NEGRO = (0,0,0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

#Establece las estructuras de datos de comida y rebotín
cotadorComida = 0
NUEVACOMIDA = 40
TAMAÑOCOMIDA = 20
rebotin = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

#Corre bucle del juego
while True:
    #Busca un evento QUIT
    if evento.type == QUIT:
        pygame.quit()
        sys.exit()

    contadorCOMIDA +=1
    if contadorComida == 0:
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    superficieVentana.fill(NEGRO)

    if rebotin['dir'] == ABAJOIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ABAJODERECHA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBAIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBADERECHA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO

    #Verificar si rebotín se movio fuera de la ventana
    if rebotin['rect'].top < 0:
        #Rebotín se movio por arriba de la ventana
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ABAJODERECHA
    if rebotin['rect'].bottom < ALTOVENTANA:
        #Rebotín se movio por debajo de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ARRIBAIZQUIERDA
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].left < 0:
        #Rebotín se movio a la izquierda de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ABAJODERECHA
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].right < ALTOVENTANA:
        #Rebotín se movio a la derecha de la ventana
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ARRIBAIZQUIERDA

    #Dibuja a rebotín en la superficie
    pygame.draw.rect(superficieVentana, BLANCO, rebotín['rect'])

    # Verifíca si rebotín intersectó algun cuadro de comida
    for comida in comida[:]:
        if verifSuperposicionRects(rebotin['rect'],comida):
            comidas.remove(comida)

    # Dibuja la comida
    for i in range(len(comidas)):
        pygame.draw.rect(superficieVentana, VERDE, comidas[i])

    # Dibuja la ventana en la pantalla
    pygame.display.update()
    relojPrincipal.tick(40)
    
