import pygame,random,GameObjects
from Resources import Res
pygame.init()
Xw=Res.Xw
Yw=Res.Yw
X=Res.X
Y=Res.Y
def WINDOW(window,display,player,Ship1,Monet,Patron,big_blast,Arrow,boom,clock,Meteor_list,bg):
    text_fps = Res.font.render('FPS: ' + str(int(clock.get_fps())), 1, (255, 255, 255))
    text_score = Res.font.render('Score: ' +str(player.score), 1, (255, 100, 255))
    text_bullets = Res.font.render('Bullets: ' + str(Ship1.bullet), 1, (255, 100, 255))
    text_monets = Res.font.render('Monets: ' + str(player.monets), 1, (255, 100, 255))
    display.blit(window, (0, 0))
    display.blit(bg,(0,0))
    display.blit(text_fps, (Xw-150, Yw-45))
    display.blit(text_score, (0 , Yw-45))
    display.blit(text_bullets, (Xw-600, Yw - 45))
    display.blit(text_monets, (Xw - 450, Yw - 45))
    if player.pos > 120:
        player.score+=1
        player.pos = 0
    Ship1.Show()

    if len(Meteor_list)<7:
        if player.pos == 73:
            k = GameObjects.Meteor(Res.meteorImage,display)
            Meteor_list.append(k)

    for m in Meteor_list:
        m.place = m.place.move(m.speed, 0)
        m.Show()

    if random.randint(0,10)==5:
        Patron.run=True


    if Patron.run==True:
        Patron.place=Patron.place.move(Patron.speed,0)
        Patron.Show(Meteor_list)

    if random.randint(0, 300) == 150:
        Monet.run = True

    if Monet.run==True:
        Monet.place=Monet.place.move(Monet.speed,0)
        Monet.Show(Meteor_list)

    if big_blast.boom == False:
        if random.randint(0,300)==7:
            big_blast.boom = True
            Res.Start_boom.play()

    if big_blast.boom == True:
        big_blast.Show()

    if boom.fire==True and Res.boom_time+500>pygame.time.get_ticks():
        boom.Show()
    elif boom.fire ==True:
        boom.fire=False



    if Ship1.fire==True:
        Arrow.Show()
        Arrow.place=Arrow.place.move(Arrow.speed,0)
        if Arrow.place.x>X :
            Arrow.place.y=-60
            Ship1.fire =False
    player.pos+=1
    pygame.display.update()

