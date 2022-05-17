import pygame

pygame.init()
screen=pygame.display.set_mode((600,400))

done = True

#Load the Fonts
font = pygame.font.SysFont("Valorant",25)

#render the text in the new surface
text = font.render("LET ME SHOW YOU HOW THE BOSS DOES IT",True,(100,100,100))

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        screen.fill((255,255,255))

        screen.blit(text, (300-text.get_width()//2,200-text.get_height()//2)) #blit will place text from one surface to other surface

        pygame.display.flip()