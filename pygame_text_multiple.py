import pygame

pygame.init()
screen = pygame.display.set_mode((600,500))

done = True
font = pygame.font.SysFont("ALGERIAN",25)

heading = font.render("PROGRAMMING LANGUAGES",True,(100,100,100))
t1 = font.render("1.JAVA",True,(100,100,100))
t2 = font.render("2.PYTHON",True,(100,100,100))
t3 = font.render("3.C#.NET",True,(100,100,100))

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.fill((0,0,0))

    screen.blit(heading, (300 - heading.get_width()//2, 100 - heading.get_height()//2))
    screen.blit(t1, (280 - t1.get_width() // 2, 150 - t1.get_height() // 2))
    screen.blit(t2, (290 - t2.get_width() // 2, 200 - t2.get_height() // 2))
    screen.blit(t3, (290 - t3.get_width() // 2, 250 - t3.get_height() // 2))

    pygame.display.flip()

