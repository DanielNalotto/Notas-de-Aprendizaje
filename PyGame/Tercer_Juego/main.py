import pygame
import os

#Screen size
WIN = pygame.display.set_mode((900,500))
#title
pygame.display.set_caption("Io: The first")

#frames per second
FPS = 60
VEL = 5

# Colores
GRAY = (100, 100, 100)
RED = (250, 5, 5)

# Rectangulo del borde
LOW_BORDER = pygame.Rect(0,0, 900, 10)
TOP_BORDER = pygame.Rect(0,490, 900, 10)
LEFT_BORDER = pygame.Rect(0,0, 10, 500)
RIGHT_BORDER = pygame.Rect(890,0, 10, 500)

#Imagen de fondo
BACKGROUND =pygame.image.load(os.path.join('Assets', 'Paisaje.png'))
Y_DERECHA_MOV_0 =pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Yus_perfil_derecha_0.png')), (50, 50))

def draw_window(yus_square):
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, GRAY, LOW_BORDER)
    pygame.draw.rect(WIN, GRAY, TOP_BORDER)
    pygame.draw.rect(WIN, GRAY, LEFT_BORDER)
    pygame.draw.rect(WIN, GRAY, RIGHT_BORDER)
    WIN.blit(Y_DERECHA_MOV_0, (yus_square.x, yus_square.y))
    pygame.display.update()

def yus_handle_movement(key_pressed, yus_square):
    if key_pressed[pygame.K_a] and yus_square.x - VEL > 0: #LEFT
        yus_square.x -= VEL
    if key_pressed[pygame.K_d] and yus_square.x + yus_square.width + VEL < RIGHT_BORDER: #RIGHT
        yus_square.x += VEL
    if key_pressed[pygame.K_w] and yus_square.y - VEL > 0: #UP
        yus_square.y -= VEL
    if key_pressed[pygame.K_s] and yus_square.y + yus_square.height + VEL < 400: #DOWN
        yus_square.y += VEL

#Main function
def main():

    #Rectangulo de Yusuke
    yus_square = pygame.Rect(400,50, 50, 50)

    clock=pygame.time.Clock()
    run=True

    while run:
        clock.tick(FPS)

        #Events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
        
        key_pressed = pygame.key.get_pressed()
        yus_handle_movement(key_pressed, yus_square)

        draw_window(yus_square)
    main()

#--------------------------------------------------------
if __name__=="__main__":
    main()
