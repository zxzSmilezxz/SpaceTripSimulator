import pygame
pygame.init()
class Res():
    file_max_score = "max_score.txt"
    file_score = "score.txt"
    spaceImage = "Images\space.jpg"
    shipImage = "Images\ship.png"
    meteorImage = "Images\Meteor.png"
    arrowImage = "Images\Arrow1.png"
    bigBlastImage = "Images\Big_blaster.png"
    bigBlastWarningImage = "Images\Big_blaster_warning.png"
    monetImage = "Images\\bb.png"
    patronImage = "Images\patron.png"
    boomImage = "Images\\boom.png"

    font = pygame.font.SysFont("ZOMBIE.TTF", 40)
    font1 = pygame.font.SysFont("ZOMBIE.TTF", 37)
    font2 = pygame.font.SysFont("ZOMBIE.TTF", 30)

    lazer_sound = pygame.mixer.Sound('Sounds\lazer_musik.WAV')
    boom_sound = pygame.mixer.Sound('Sounds\\boom_musik.WAV')
    Start_boom = pygame.mixer.Sound('Sounds\Start_boom.WAV')
    Xw = int(900)
    Yw = int(650)
    X = int(900)
    Y = int(600)
    boom_time=0