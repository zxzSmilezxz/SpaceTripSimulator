import pygame,FileWorker,sys,GameObjects
from Resources import Res
pygame.init()
def GameOver(window,display,player):
    global Ship1
    D=True
    guy=FileWorker.Writer.nameRead(Res.file_max_score)
    pygame.mixer.music.load("Musik\menu_musik.mp3")
    pygame.mixer.music.play(999999)
    while D:
        window.fill((0, 0, 0))
        GO = Res.font1.render(" GAME OVER ", 1, (200, 155, 77))
        window.blit(GO, (350, 50))
        GO = Res.font1.render("The best was " + guy[1][0:-1]+" with score : "+ guy[0][0:-1] ,1, (200, 155, 77))
        window.blit(GO, (150, 150))
        GO = Res.font1.render(' Your Score: ' + str(player.score), 1, (200, 155, 77))
        window.blit(GO, (150, 250))
        GO = Res.font1.render('  Press any key to continue', 1, (55, 155, 77))
        window.blit(GO, (150, 350))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN or e.type==pygame.KEYDOWN:
                Ship1 = GameObjects.Ship(Res.shipImage,display)
                player.score = 0
                player.monets = 0
                D = False

        display.blit(window, (0, 0))
        pygame.display.update()