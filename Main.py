import pygame,sys,WindowDrow
import Save,GameObjects,Player,FileWorker,Game_Over
from Resources import Res
import Game_Over
pygame.init()
clock=pygame.time.Clock()
Xw=Res.Xw
Yw=Res.Yw
X=Res.X
Y=Res.Y

window=pygame.Surface((Xw,Yw))
display=pygame.display.set_mode((Xw,Yw))#screen=display
pygame.display.set_caption("Space_trip_simulator")
bg = pygame.image.load(Res.spaceImage).convert_alpha()

#======================================================
#announcement Game_Objects
boom=GameObjects.Boom(Res.boomImage,display)
big_blast=GameObjects.Big_blaster(Res.bigBlastImage,Res.bigBlastWarningImage,display)
Meteor_list = []
k = GameObjects.Meteor(Res.meteorImage,display)
Meteor_list.append(k)
Monet=GameObjects.Prize(Res.monetImage,display)
Patron=GameObjects.Prize(Res.patronImage,display)
Arrow=GameObjects.Arrow(Res.arrowImage,display)
Ship1=GameObjects.Ship(Res.shipImage,display)

player = Player.Playmen()

u=True

#======================================================================
class Menu():
    def __init__(self,player,window,display,puncts=[400,200,"Punct",(0,0,0),(250,250,250),6],puncts2=[400,200,"Punct",(0,0,0),(250,250,250),6]):
        self.puncts=puncts
        self.puncts2 = puncts2
        self.player=player
        self.display = display
        self.window = window

    def render(self,surface,num_point,puncts=[400,200,"Punct",(0,0,0),(250,250,250),6]):
        for i in puncts:
            if num_point==i[5]:
                surface.blit(pygame.font.SysFont("ZOMBIE.TTF", i[6]).render(i[2],1,i[4]),(i[0],i[1]))
            else:
                surface.blit(pygame.font.SysFont("ZOMBIE.TTF", i[6]).render(i[2], 1, i[3]), (i[0], i[1]))

    def instructions(self):
        D=True
        while D:
            self.window.fill((0, 0, 0))
            GO = Res.font1.render('Avoid meteors, collect bullets (green ones) and monets', 1, (200, 155, 77))
            self.window.blit(GO, (1, 150))
            GO = Res.font1.render(' Use keys UP,DOWN,LEFT,RIGHT to move', 1, (200, 155, 77))
            self.window.blit(GO, (1, 250))
            GO = Res.font1.render(' Use Space to fire', 1, (100, 45, 87))
            self.window.blit(GO, (1, 350))
            GO = Res.font1.render('Press ESCAPE to return to the main menu', 1, (255, 100, 77))
            self.window.blit(GO, (1, 450))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key==pygame.K_ESCAPE:
                        D = False
            self.display.blit(self.window, (0, 0))
            pygame.display.update()

    def table(self):
        global Meteor_list,Ship1
        pygame.mixer.music.load("Musik\menu_musik.mp3")
        pygame.mixer.music.play(999999)
        done=True
        punct=0
        while done:
            self.window.fill((0,0,0))
            self.render(self.window, punct, self.puncts)
            for e in pygame.event.get():
                if e.type==pygame.QUIT :
                    return
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP:
                        if punct>0:
                            punct-=1
                        else:
                            punct=len(self.puncts)-1

                    if e.key==pygame.K_DOWN:
                        if punct<len(self.puncts)-1:
                            punct+=1
                        else:
                            punct=0

                    if e.key==pygame.K_RETURN:
                        if punct==0:
                            self.player.score = 0
                            self.player.monets = 0
                            Meteor_list = []
                            k = GameObjects.Meteor(Res.meteorImage,self.display)
                            Meteor_list.append(k)
                            Ship1 = GameObjects.Ship(Res.shipImage,self.display)
                            self.main()
                        elif punct==1:
                            self.main()
                        elif punct==2:
                            self.instructions()
                        elif punct==3:
                            Save.Score.showScore(Res.font1,self.display,self.window)
                        elif punct==4:
                            return

            self.display.blit(self.window,(0,0))
            pygame.display.update()

    def table2(self):
        global  Meteor_list,Ship1
        done=True
        punct=0
        pygame.mixer.music.load("Musik\menu_musik.mp3")
        pygame.mixer.music.play(9999)
        while done:
            self.window.fill((25,25,112))
            self.render(self.window,punct,self.puncts2)
            for e in pygame.event.get():
                if e.type==pygame.QUIT :
                    sys.exit()
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP:
                        if punct>0:
                            punct-=1
                        else:
                            punct=len(self.puncts2)-1

                    if e.key==pygame.K_DOWN:
                        if punct<len(self.puncts2)-1:
                            punct+=1
                        else:
                            punct=0

                    if e.key==pygame.K_RETURN:
                        if punct==0:
                            self.player.monets -= 1
                           # done = False
                            return True


                        elif punct==1:
                            self.player.score += self.player.monets * 10
                            self.player.monets = 0
                            return False

            self.display.blit(self.window,(0,0))
            pygame.display.update()




    def main(self):
        pygame.mixer.music.load('Musik\game_musik.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(999999)
        global u, Ship1, Meteor_list

        while u:
            clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    u = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and Ship1.place.x > 0:
                Ship1.place = Ship1.place.move(-int(Ship1.speed), 0)
            elif keys[pygame.K_RIGHT] and Ship1.place.x < X - 50:
                Ship1.place = Ship1.place.move(Ship1.speed, 0)

            if keys[pygame.K_UP] and Ship1.place.y > 0:
                Ship1.place = Ship1.place.move(0, -int(Ship1.speed))
            elif keys[pygame.K_DOWN] and Ship1.place.y < Y - 50:
                Ship1.place = Ship1.place.move(0, int(Ship1.speed))

            if keys[pygame.K_SPACE] and Ship1.bullet > 0 and Ship1.fire == False:
                Ship1.fire = True
                Res.lazer_sound.play()
                Ship1.bullet -= 1
                Arrow.place.y = 0
                Arrow.place.x = 0
                Arrow.place.move_ip(Ship1.place.x + 50 + 10, Ship1.place.y)
            if keys[pygame.K_ESCAPE]:
                return
            if Ship1.place.colliderect(big_blast.place) and pygame.time.get_ticks() - big_blast.big_boom_time > 3000:
                if self.Death() == False:
                    return

            for m in Meteor_list:
                if Ship1.place.colliderect(m.place):
                    if self.Death() == False:
                        return

                if m.place.colliderect(Arrow.place):
                    Res.boom_sound.play()
                    Ship1.fire = False
                    boom.fire = True
                    boom.place.x = m.place.x
                    boom.place.y = m.place.y
                    Res.boom_time = pygame.time.get_ticks()
                    Arrow.place.y = -100
                    Meteor_list.remove(m)
                    break

            if Ship1.place.colliderect(Patron.place):
                Ship1.bullet += 1
                Patron.place.move_ip(0, -1000)

            if Ship1.place.colliderect(Monet.place):
                player.monets += 1
                Monet.place.move_ip(0, -1000)
            WindowDrow.WINDOW(window, display, player, Ship1, Monet, Patron, big_blast, Arrow, boom, clock, Meteor_list,bg)
#==============================================================

    def Death(self):
        global Meteor_list
        life=False
        Meteor_list = []
        big_blast.boom = False
        big_blast.place.y=-60
        big_blast.big_boom_time = 0
        k = GameObjects.Meteor(Res.meteorImage,display)
        Meteor_list.append(k)
        if player.monets >= 1:
            life = menu.table2()
            pygame.mixer.music.load("Musik\game_musik.mp3")
            pygame.mixer.music.play(999999)

        if life == False:
            nik = str(Save.Score.putName(Res.font1, display, window))
            FileWorker.Writer.write(Res.file_score,player.score,nik,"a")
            if player.score > player.max_score:
                FileWorker.Writer.write(Res.file_max_score,player.score,nik,"w")
                player.max_score = player.score

            Game_Over.GameOver(window,display,player)
            return False
        return True

#===================================================






player.max_sxore = FileWorker.Writer.read(Res.file_max_score)
puncts=[(250,50,"New game",(50,4,78),(123,255,14),0,75),(250,125,"Continue",(50,4,78),(123,255,14),1,75),(250,200,"Options",(50,4,78),(123,255,14),2,75),(250,275,"Scores",(50,4,78),(123,255,14),3,75),(250,350,"Quit",(50,4,78),(123,255,14),4,75)]
puncts2=[(0,150,"Buy 1 life for 1 monet",(178,34,34),(123,255,14),0,50),(0,300,"Game over (every monet will become 10 score points)",(178,34,34),(123,255,14),1,50)]
menu=Menu(player,window,display,puncts,puncts2)
menu.table()
